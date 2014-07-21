import sys

def unwrap(matrix):
    spiral = []
    while matrix:
        spiral.extend( matrix[0] )
        matrix = list( reversed( zip( *matrix[1:] ) ) )

    return spiral





if __name__ == '__main__':
    with open(sys.argv[1]) as fp:
        for line in fp:
            line = line.strip().split(';')
            n,m, li = int(line[0].strip()), int(line[1].strip()), line[2]

            matrix = [[0 for j in xrange(m)] for i in xrange(n)]

            li = [i for i in li.strip().split()]
            count = 0
            for i in xrange(n):
                for j in xrange(m):
                    matrix[i][j] = li[count]
                    count += 1


            # print matrix
            print ' '.join( unwrap( matrix ) )



