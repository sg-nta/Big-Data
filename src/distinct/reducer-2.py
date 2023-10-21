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
            for _, value in group:
                print(f"{key}{separator}{value}")
                break
        except ValueError:
            pass

if __name__ == "__main__":
    main()





