import enum
import platform
import subprocess
import sys
from typing import Optional

from .config import get_debug


class OperatingSystem(enum.Enum):
    WINDOWS = "Windows"
    LINUX = "Linux"
    MACOS = "macOS"
    OTHER = "Other"


def check_os() -> OperatingSystem:
    system = platform.system()
    if system == "Windows":
        return OperatingSystem.WINDOWS
    elif system == "Linux":
        return OperatingSystem.LINUX
    elif system == "Darwin":
        return OperatingSystem.MACOS
    else:
        return OperatingSystem.OTHER


def execute_command(command: str, input_data: Optional[str] = None) -> int:
    if get_debug():
        print(f"Executing command: {command}")

    # Start the subprocess
    process = subprocess.Popen(
        command,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,  # Use text mode (decodes the bytes to str)
        shell=True,  # Be cautious with shell=True, it's a security hazard if combined with untrusted input
    )

    # Send input_data to stdin if provided
    if input_data is not None:
        process.stdin.write(input_data)
        process.stdin.close()

    # Read the output line by line as it is generated
    while True:
        output = process.stdout.readline()
        if output == "" and process.poll() is not None:
            break
        if output:
            print(output.strip())

    # After the process ends, get the rest of the output if any
    remainder_output, errors = process.communicate()
    if remainder_output:
        print(remainder_output.strip())

    # Print errors if there are any
    if errors:
        print(f"Errors:\n{errors.strip()}", file=sys.stderr)

    # Return the exit code of the process
    return process.returncode


def print_not_implemented() -> None:
    print("Not implemented.")
