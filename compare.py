import de_bruijn_sequence as db
import rotate_resistant_de_bruijn_sequence as dbrr

print db.de_bruijn(2, 3)
print dbrr.de_bruijn_rotate_resistant(2, 3)

k = 4
for n in range(2, 10):
    de_bruijn_rr = dbrr.de_bruijn_rotate_resistant(k, n)
    lenght = len(de_bruijn_rr)
    var = k ** (n-1) + n - 1
    print "n = %d, length = %d, k ** (n-1) + n - 1 = %d, result = %s" % (n, lenght, var, lenght == var)