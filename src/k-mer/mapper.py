

import sys
import math
import os

def read_input(file, kmer):
    for line in file:
        line = line.strip()
        if '>gi' not in line: #ignore line contain '>gi'
            try:
                yield [line[i:i+kmer] for i in range(len(line)-kmer+1)]
            except: 
                continue
def main():
    k = int(os.environ["k"])
    for kmers in read_input(sys.stdin, k):
        for kmer in kmers:
            print(f"{kmer}\t{1}")

if __name__ == "__main__":
    main()