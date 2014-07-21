import sys



if __name__ == '__main__':

    filename = sys.argv[1]
    f = open(filename)

    for line in f:
        li, m = line.split()[:-1], int(line.split()[-1])
        # print li,m
        if m <= len(li):
            print li[-m]

    f.close()





