"""A minimal hello world CLI."""

import argparse


def main():
    parser = argparse.ArgumentParser(description="Print hello world.", add_help=False)
    parser.add_argument("--help", action="help", help="show this help message and exit")
    parser.parse_args()
    print("hello world")


if __name__ == "__main__":
    main()
