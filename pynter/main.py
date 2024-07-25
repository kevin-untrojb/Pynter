#!/usr/bin/env python3
import argparse

def main():
    parser = argparse.ArgumentParser(description="Pynter: A Python linter example")

    parser.add_argument('input', type=str, help='Input file')
    parser.add_argument('--output', type=str, help='Ouput lof file (optional)')
    parser.add_argument('--verbose', action='store_true', help='Details')

    args = parser.parse_args()

    if args.verbose:
        print("Details mode actived")
    print(f"Input file: {args.input}")
    if args.output:
        print(f"Output file: {args.output}")

if __name__ == "__main__":
    main()