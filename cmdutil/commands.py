import enum
import platform
import subprocess


class OperatingSystem(enum.Enum):
    WINDOWS = "Windows"
    LINUX = "Linux"
    MACOS = "macOS"
    OTHER = "Other"


def check_os():
    system = platform.system()
    if system == "Windows":
        return OperatingSystem.WINDOWS
    elif system == "Linux":
        return OperatingSystem.LINUX
    elif system == "Darwin":
        return OperatingSystem.MACOS
    else:
        return OperatingSystem.OTHER


def execute_command(command):
    try:
        process = subprocess.Popen(
            command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        stdout, stderr = process.communicate()
        if process.returncode != 0:
            print(f"Error: {stderr.decode()}")
        else:
            print(stdout.decode())
    except Exception as e:
        print(f"Error: {str(e)}")


def print_not_implemented():
    print("Not implemented.")


def check_port(port: int):
    os = check_os()
    if os == OperatingSystem.WINDOWS:
        execute_command(f"netstat -ano | findstr :{port}")
    elif os == OperatingSystem.LINUX:
        execute_command(f' netstat -tuln | grep ":{port} "')
    elif os == OperatingSystem.MACOS:
        execute_command(f'lsof -i -P | grep LISTEN | grep ":{port} "')
    else:
        print_not_implemented()
