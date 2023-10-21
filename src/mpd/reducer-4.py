import sys
import os
    
from itertools import groupby
from operator import itemgetter


def read_mapper_output(file, separator='\t'):
    for line in file:
        yield line.rstrip().split(separator, 1)

def main(separator='\t'):
    # input comes from STDIN (standard input)
    data = read_mapper_output(sys.stdin, separator=separator)
    data = sorted(data, key=itemgetter(0))
    for key, group in groupby(data, itemgetter(0)):
        try:
            max_val = max(int(count) for _, count in group)
            print(f"{key}{separator}{max_val}")
        except ValueError:
            pass
if __name__ == "__main__":
    main()
