import sys

def reversegroup(li, n):

    res = []

    if n <= len(li):
        while n <= len(li) and n>0:
            res.extend(li[:n][::-1])
            li = li[n:]

    res.extend(li)
    return ",".join([str(i) for i in res])



# print reversegroup([1,2,3,4,5], 2)
# print reversegroup([1,2,3,4,5], 3)
# print reversegroup([1,2,3,4,5], 0)
# print reversegroup([1,2,3,4,5], 6)


if __name__ == "__main__":

    filename = sys.argv[1]
    f = open(filename)

    for line in f:
        x, k = line.split(";")
        li = x.split(',')
        # print li, k
        print reversegroup(li, int(k))

    f.close()
