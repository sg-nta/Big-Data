from itertools import groupby
from operator import itemgetter
import sys
import os
def read_mapper_output(file, sep='\t'):
    for line in file:
        yield line.rstrip().split(sep)
        
def main(sep='\t'):
    n = int(os.environ["n"])
    data = sorted(read_mapper_output(sys.stdin,sep = sep), key=itemgetter(0))
    for key, group in groupby(data, itemgetter(0)):
        try:
            group_list = list(group)
            if len(group_list) > 1:
                (i, j), (x1, y1), (x2, y2) = \
                    map(lambda x: x[1].split(','), group_list[:2])
                distance = (int(x1) - int(x2))**2 + (int(y1) - int(y2))**2
                print(f"{int(i) * n + int(j)}{sep}{distance}")
        except ValueError:
            pass
if __name__ == "__main__":
    main()
    