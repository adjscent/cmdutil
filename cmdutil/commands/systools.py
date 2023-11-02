from .util import OperatingSystem, execute_command, print_not_implemented, check_os


def check_port(port: int) -> None:
    os = check_os()
    if os == OperatingSystem.WINDOWS:
        """
        """
        execute_command(f"netstat -ano | findstr :{port}")
    elif os == OperatingSystem.LINUX:
        """
        tcp        0      0 0.0.0.0:8000            0.0.0.0:*               LISTEN
        """
        execute_command(f'netstat -tuln | grep ":{port} "')
    elif os == OperatingSystem.MACOS:
        """
        """
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
        execute_command(f"free -mh")
    else:
        print_not_implemented()
