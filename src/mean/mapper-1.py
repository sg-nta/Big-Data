

import sys
import math
import os

def read_input(file):
    for line in file:
        yield line.strip()

def main():
    n = int(os.environ["n"])
    for line in read_input(sys.stdin):
        i, xi = map(int, line.split())
        sqrt_n = int(math.sqrt(n))
        key = i % sqrt_n
        print(f"{key}\t{xi}")

if __name__ == "__main__":
    main()