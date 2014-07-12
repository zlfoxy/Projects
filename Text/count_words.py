def count_words():
    filename = raw_input('input a file name:')
    alist = open(filename).read().strip().split(' ')
    print "Thera're %d words" % len(alist)
count_words()
