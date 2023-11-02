import argparse
from . import commands

command_list = ["checkport"]


def setup_parser():
    parser = argparse.ArgumentParser(
        description="A utility to run OS specific commands."
    )
    # parser.add_argument('-c', '--command', type=str, help='The command to run.')
    # parser.add_argument('-os', '--operating-system', type=str, choices=['windows', 'linux', 'mac'], help='The operating system.')
    parser.add_argument(
        "command", type=str, help="The command to run.", choices=command_list
    )
    parser.add_argument(
        "parameters", type=str, nargs="*", help="The parameters of the command."
    )
    return parser


def main():
    parser = setup_parser()
    args = parser.parse_args()

    command = args.command

    if command == "checkport":
        parser = argparse.ArgumentParser(
            description="A utility to run OS specific commands."
        )
        parser.add_argument("command", type=str, help="The command to run.")
        parser.add_argument("port", type=int, help="port to check.")
        args = parser.parse_args()
        commands.check_port(args.port)


if __name__ == "__main__":
    main()
