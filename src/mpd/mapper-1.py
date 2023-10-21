import sys
import math
import os

def read_input(file):
    for line in file:
        yield line.strip()

def main():
    n = os.environ["n"]
    for line in read_input(sys.stdin):
        i, pi = line.split()
        xi,yi = map(int,pi.split(","))
        sqrt_n = int(math.sqrt(int(n)))
        for j in range(sqrt_n):
            print(f"{i},{j}\t{xi},{yi}")

if __name__ == "__main__":
    main()