import sys
import math
import os

def read_input(file):
    for line in file:
        yield line.strip()

def main():
    n = int(os.environ["n"])
    for line in read_input(sys.stdin):
        print(line)

if __name__ == "__main__":
    main()