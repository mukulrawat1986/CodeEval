import sys

def hidden(s):
    di = dict(zip([i for i in 'abcdefghij'], [str(i) for i in xrange(10)]))

    res = []

    for element in s:
        if element.isalpha() and element.islower() and element in di:
            res.append(di[element])
        if element.isdigit():
            res.append(element)
    # print res
    return "".join(res)

def test():

    assert hidden('abcdefghik') == '012345678'
    assert hidden('Xa,}A#5N}{xOBwYBHIlH,#W') == '05'
    assert hidden("(ABW>'yy^'M{X-K}q,") == ''
    assert hidden('6240488') == '6240488'
    print 'tests cleared'



if __name__ == '__main__':
    with open(sys.argv[1]) as fp:
        for line in fp:
            s = line.strip()
            res = hidden(s)
            if len(res) == 0:
                print 'NONE'
            else:
                print res

    fp.close()


# test()
