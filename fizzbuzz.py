import sys

def fizzbuzz(a, b, n):
    return " ".join(["FB" if i%a==0  and i%b ==0 else "F" if i%a==0 else "B" \
    if i%b==0 else str(i) for i in xrange(1, n+1)])


if __name__ == '__main__':

    filename = sys.argv[1]
    f = open(filename)
    for line in f:
        a, b, n = [int(i) for i in line.split()]
        print fizzbuzz(a, b, n)
    f.close()



