import sys
import os
    
from itertools import groupby
from operator import itemgetter


def read_mapper_output(file, separator='\t'):
    for line in file:
        yield line.rstrip().split(separator, 1)

def main(separator='\t'):
    n = int(os.environ["n"])
    data = read_mapper_output(sys.stdin, separator=separator)
    total_sum = 0

    for key, group in groupby(data, itemgetter(0)):
        try:
            total_sum = sum(int(count) for _, count in group)/n
            print(f"{0}{separator}{total_sum}")
        except ValueError:
            pass
if __name__ == "__main__":
    main()
