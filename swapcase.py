import sys

with open(sys.argv[1]) as fp:
    for line in fp:
        li = line.strip().split()
        f = lambda x: x if x.isdigit() else x.upper() if x.islower() else \
        x.lower()
        print "".join(["".join(map(f,word)) for word in line]).strip()

fp.close()
