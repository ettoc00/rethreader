from rethreader import Rethreader

"""
A Rethreader is not faster than a map, if the function does not require to wait for something.
"""


if __name__ == '__main__':

    from time import time, sleep
    from random import random

    f = lambda x: x * x * x - x
    s = []
    s_c, s_p, s_q = 0, 0, 0
    for _ in range(20):
        k = int(random() * 20000) + 1
        r = list(range(k))
        a = time()
        p = list(map(f, r))
        b = time()
        q = Rethreader(f, r).run().results
        c = time()
        if p == q:
            try:
                t = (c - b) / (b - a)
                s_c += 1
                s_p += k
                s_q += t
            except ZeroDivisionError:
                t = 0
            s.append((k, t))
            print('\r', k, '\t', t)
            if s_c:
                print('\r', '\t', '%.5f' % (s_q / s_c), "times slower than calling a map", end='')
        sleep(0.1)
    print()
