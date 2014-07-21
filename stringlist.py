import itertools
import sys

def permutations(n,s):
    li = list(set([''.join(i) for i in itertools.product(s,repeat=n)]))
    return ",".join(sorted(li))



if __name__ == '__main__':
    with open(sys.argv[1]) as fp:
        for line in fp:
            n,s = line.strip().split(',')
            n = n.strip()
            s = s.strip()
            print permutations(int(n), s)
    fp.close()

