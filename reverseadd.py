import sys

def findIteration(n):

    count = 0

    while str(n) != str(n)[::-1]:
        count += 1
        n = n + int(str(n)[::-1])

    return " ".join([str(count), str(n)])



if __name__ == "__main__":

    filename = sys.argv[1]

    f = open(filename)

    for line in f:
        print findIteration(int(line.split()[0]))

    f.close()

