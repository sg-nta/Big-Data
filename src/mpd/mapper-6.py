import sys
import math
import os

def read_input(file):
    for line in file:
        yield line.strip()

def main():
    n = int(os.environ["n"])
    for line in read_input(sys.stdin):
        k, d = map(int, line.split())
        k_ = k % (int(math.sqrt(n)))
        print(f"{k_}\t{d}")
if __name__ == "__main__":
    main()