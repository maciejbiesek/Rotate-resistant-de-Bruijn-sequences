import rotate_resistant_de_bruijn_sequence as dbrr

f = open("output", "a")
for k in range(2, 11):
    for n in range(2, 10):
        de_bruijn_rr = dbrr.de_bruijn_rotate_resistant(k, n)
        lenght = len(de_bruijn_rr)
        var = k ** (n-1) + n - 1
        print "k = %d, n = %d, sequence: %s, length = %d, k ** (n-1) + n - 1 = %d, result = %s" % (k, n, de_bruijn_rr, lenght, var, lenght == var)
		
	f.write("k = %d, n = %d, sequence: %s, length = %d, k ** (n-1) + n - 1 = %d, result = %s \n" % (k, n, de_bruijn_rr, lenght, var, lenght == var))

f.close()
