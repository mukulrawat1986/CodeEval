from itertools import permutations
import sys

def stringpermutations(s):
    perms = [''.join(p) for p in permutations(s)]
    perms = sorted(perms)
    return ",".join(perms)


# print stringpermutations('hat')
# print stringpermutations('abc')
# print stringpermutations('Zu6')


if __name__ == '__main__':
    with open(sys.argv[1]) as fp:
        for line in fp:
            print stringpermutations(line.strip())
    fp.close()
