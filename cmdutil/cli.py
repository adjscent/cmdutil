import argparse

from . import commands

command_list = ["version", "update", "checkport", "process", "memory"]


def setup_parser():
    parser = argparse.ArgumentParser(
        prog="cmdutil", description="A utility to run OS specific commands."
    )
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug mode")
    subparsers = parser.add_subparsers(help=f"command to execute", dest="command")
    for cmd in command_list:
        subparsers.add_parser(cmd)
    parser_checkport = subparsers.add_parser("checkport")
    parser_checkport.add_argument("port", type=int, help="port number to check")

    return parser


def main():
    parser = setup_parser()
    args = parser.parse_args()

    command = args.command
    commands.set_debug(args.debug)

    if command == "version":
        commands.print_not_implemented()
    elif command == "update":
        commands.print_not_implemented()
    elif command == "checkport":
        commands.check_port(args.port)
    elif command == "process":
        commands.process()
    elif command == "memory":
        commands.memory()


if __name__ == "__main__":
    main()
