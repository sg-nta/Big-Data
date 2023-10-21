

import sys
import math
import os

def read_input(file):
    for line in file:
        yield line.strip()

def main():
    for line in read_input(sys.stdin):
        i, xi = map(int, line.split())
        print(f"{xi}\t{i}")

if __name__ == "__main__":
    main()