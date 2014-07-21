import sys
from math import sqrt

def doublesquare(i):
    count = 0
    valuesArr = []
    for x in range(int(sqrt(int(i)))+1):
        y = sqrt(int(i) - x*x)
        if y == int(y):
            if x*x == y:
                count += 2
            else:
                count += 1
    print str(count/2)

    # inputf.close()




# doublesquare(5)
# doublesquare(10)
# doublesquare(25)
# doublesquare(3)
# doublesquare(0)
# doublesquare(1)

if __name__ == '__main__':
    with open(sys.argv[1]) as fp:
        for line in fp:
            break
        for line in fp:
            doublesquare(int(line.strip()))
