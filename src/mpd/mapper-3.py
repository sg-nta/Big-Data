import sys
import math
import os

def read_input(file):
    for line in file:
        yield line.strip()

def main():
    for line in read_input(sys.stdin):
        ij, pi = line.split()
        i,j = map(int,ij.split(","))
        xi,yi = map(int,pi.split(","))
        print(f"{min(i,j)},{max(i,j)}\t{xi},{yi}")
if __name__ == "__main__":
    main()