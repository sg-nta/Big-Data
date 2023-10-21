from itertools import groupby
from operator import itemgetter
import sys
def read_mapper_output(file, separator='\t'):
    for line in file:
        yield line.rstrip().split(separator)

def main(separator='\t'):
    data = read_mapper_output(sys.stdin, separator=separator)
    data = sorted(data, key=itemgetter(0))
    for key, group in groupby(data, itemgetter(0)):
        try:
            distinct_lists = set(map(tuple, list(group)))
            distinct_lists = [list(elem) for elem in distinct_lists]
            for _, value in distinct_lists:
                print(f"{key}{separator}{value}")
        except ValueError:
            pass

if __name__ == "__main__":
    main()





