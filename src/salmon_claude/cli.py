import argparse

from salmon_claude import __version__


def main() -> None:
    parser = argparse.ArgumentParser(prog="salmon")
    parser.add_argument("--version", action="version", version=f"salmon {__version__}")
    parser.parse_args()
