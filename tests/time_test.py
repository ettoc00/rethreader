from rethreader import Rethreader

if __name__ == '__main__':

    from time import time, sleep
    from random import random

    f = lambda x: x * x * x - x
    s = []
    s_c, s_p, s_q = 0, 0, 0
    for _ in range(1, 2000):
        k = int(random() * 20000) + 1
        a = time()
        p = [f(x) for x in range(k)]
        b = time()
        q = Rethreader(f, list(range(k))).run().results
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
                print('\r', '\t', s_q / s_c, end='')
        sleep(0.1)
    print()