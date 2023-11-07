import re
import subprocess

from .util import (OperatingSystem, check_os, execute_command,
                   print_not_implemented)


def check_port(port: int) -> None:
    os = check_os()
    if os == OperatingSystem.WINDOWS:
        """ """
        execute_command(f"netstat -ano | findstr :{port}")
    elif os == OperatingSystem.LINUX:
        """
        tcp        0      0 0.0.0.0:8000            0.0.0.0:*               LISTEN
        """
        execute_command(f'netstat -tuln | grep ":{port} "')
    elif os == OperatingSystem.MACOS:
        """ """
        execute_command(f'lsof -i -P | grep LISTEN | grep ":{port} "')
    else:
        print_not_implemented()


def process() -> None:
    os = check_os()
    if os == OperatingSystem.WINDOWS:
        execute_command(f"tasklist")
    elif os == OperatingSystem.LINUX:
        execute_command(f"top -b -n 1")
    elif os == OperatingSystem.MACOS:
        execute_command(f'ps -A -o %cpu,comm | grep -v "^ 0.0"')
    else:
        print_not_implemented()


def memory() -> None:
    os = check_os()
    if os == OperatingSystem.WINDOWS:
        execute_command(
            f'systeminfo | findstr /C:"Total Physical Memory" /C:"Available Physical Memory"'
        )
    elif os == OperatingSystem.LINUX:
        execute_command(f"free -mh")
    elif os == OperatingSystem.MACOS:
        # Get process info
        ps = (
            subprocess.Popen(["ps", "-caxm", "-orss,comm"], stdout=subprocess.PIPE)
            .communicate()[0]
            .decode()
        )
        vm = (
            subprocess.Popen(["vm_stat"], stdout=subprocess.PIPE)
            .communicate()[0]
            .decode()
        )

        # Iterate processes
        processLines = ps.split("\n")
        sep = re.compile("[\s]+")
        rssTotal = 0.0  # kB
        for row in range(1, len(processLines)):
            rowText = processLines[row].strip()
            rowElements = sep.split(rowText)
            try:
                rss = float(rowElements[0]) * 1024
            except:
                rss = 0  # ignore...
            rssTotal += rss

        # Process vm_stat
        vmLines = vm.split("\n")
        sep = re.compile(":[\s]+")
        vmStats = {}
        for row in range(1, len(vmLines) - 2):
            rowText = vmLines[row].strip()
            rowElements = sep.split(rowText)
            vmStats[(rowElements[0])] = int(rowElements[1].strip("\.")) * 4096

        print("Wired Memory:\t\t%d MB" % (vmStats["Pages wired down"] / 1024 / 1024))
        print("Active Memory:\t\t%d MB" % (vmStats["Pages active"] / 1024 / 1024))
        print("Inactive Memory:\t%d MB" % (vmStats["Pages inactive"] / 1024 / 1024))
        print("Free Memory:\t\t%d MB" % (vmStats["Pages free"] / 1024 / 1024))
        print("Real Mem Total (ps):\t%.3f MB" % (rssTotal / 1024 / 1024))
    else:
        print_not_implemented()
