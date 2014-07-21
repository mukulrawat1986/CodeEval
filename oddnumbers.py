# Print the odd numbers from 1 to 99, one per line

print "\n".join([str(i) for i in xrange(1,100,2) if i%2!=0])
