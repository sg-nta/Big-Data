

import sys
import math
import os

def read_input(file):
    for line in file:
        yield line.strip()

def main():
    for line in read_input(sys.stdin):
        words = line.split()
        for word in words:
            print(f"{word}\t{1}")

if __name__ == "__main__":
    main()