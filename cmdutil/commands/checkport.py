from .util import OperatingSystem, execute_command, print_not_implemented, check_os


def check_port(port: int) -> None:
    os = check_os()
    if os == OperatingSystem.WINDOWS:
        execute_command(f"netstat -ano | findstr :{port}")
    elif os == OperatingSystem.LINUX:
        execute_command(f'netstat -tuln | grep ":{port} "')
    elif os == OperatingSystem.MACOS:
        execute_command(f'lsof -i -P | grep LISTEN | grep ":{port} "')
    else:
        print_not_implemented()
