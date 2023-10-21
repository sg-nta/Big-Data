import sys
import math
import os

def read_input(file):
    for line in file:
        yield line.strip()

def main():
    n = int(os.environ["n"])
    for line in read_input(sys.stdin):
        ij, pi = line.split()
        i,j = map(int,ij.split(","))
        xi,yi = map(int,pi.split(","))
        sqrt_n = int(math.sqrt(n))
        
        for k in range(sqrt_n):
            print(f"{i},{j*sqrt_n+k}\t{xi},{yi}")
        if math.sqrt(n) - sqrt_n > 0 and j == sqrt_n-1:
            print(f"{i},{n-1}\t{xi},{yi}")
if __name__ == "__main__":
    main()