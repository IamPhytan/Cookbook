import argparse
from os import O_APPEND
import sys


def parse_arguments(args_to_parse):
    """Parse arguments given during the execution of the script"""
    parser = argparse.ArgumentParser(description="Args test : Show args that are given on script execution")

    # Required argument, can have multiple words
    parser.add_argument("-n", "--name", nargs="+", help="User name", required=True)

    # Argument with default value
    parser.add_argument("-f", "--file", help="Filename", default="testfile.txt")

    # Optional argument
    parser.add_argument("-o", "--optional", help="Optional parameter")

    # Parameter with a type and a value
    parser.add_argument("-N", "--num", help="Number", type=int, default=42)

    # Store an argument as a bool
    parser.add_argument("-p", "--pythonic", help="Is the code pythonic ?", action="store_true")

    # Append different arguments to a list
    parser.add_argument("-l", "--list", help="Append to list", action="append", type=int)

    return parser.parse_args(args_to_parse.split())


def run_parser(args_to_parse):
    print(f"{sys.executable} {__file__} {args_to_parse}")
    args = parse_arguments(args_to_parse)

    # Greet with name (yes, name is required)
    # If name has multiple words, join them together / convert to string
    name = " ".join(args.name)
    print(f"Hello {name} !")

    # Maximal length of key in args
    args_dict = args.__dict__
    argkeymax = len(max(args_dict.keys(), key=lambda x: len(x)))

    # Print args
    for k, v in args_dict.items():
        print(f"{k.ljust(argkeymax)} : {v}")

    # File content (yes, file had a default value)
    with open(args.file, "r") as f:
        content = [line.strip("\n") for line in f.readlines()]
    print("\nFile content :", *content, sep="\n")
    print("-" * 80, end="\n\n")


if __name__ == "__main__":
    run_parser("-n Alice -f testfile.txt --optional 2 --pythonic")
    run_parser("-n Bob --optional 2")
    run_parser("-n Charlie --pythonic")
    run_parser("-n King Arthur --pythonic -l 1 -l 2 -l 3 -l 54")
    run_parser("-n Sir Lancelot -f testfile.txt --optional -N 28 --pythonic")
