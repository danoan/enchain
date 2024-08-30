import argparse
import json
import sys
from typing import Any, List, TextIO


def list_to_dict(obj: List[Any], list_name: str):
    return {list_name: obj}


def _list_to_dict(data: TextIO, list_name: str, *args, **kwargs):
    obj = json.loads(data.read())
    if not isinstance(obj, list):
        print("Data is not a list")
        exit(1)

    json.dump(list_to_dict(obj, list_name), sys.stdout)


def main():
    command = "convert-json"
    parser = argparse.ArgumentParser(command, description="Convert json structures among them")

    subparser = parser.add_subparsers()
    # to_dict subparser
    sub_to_dict = subparser.add_parser("to-dict")
    sub_to_dict.add_argument("list_name", type=str, help="Name of the list")
    sub_to_dict.add_argument("data", nargs="?", type=argparse.FileType(
        "r"), default=sys.stdin, help="JSON data to convert")
    sub_to_dict.set_defaults(func=_list_to_dict, subcommand_help=sub_to_dict.print_help)

    args = parser.parse_args()
    if "func" in args:
        args.func(**vars(args))
    elif "subcommand_help" in args:
        args.subcommand_help()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
