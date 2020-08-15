from rethreader import Rethreader
from time import sleep

if __name__ == '__main__':
    print("Test 1: 0123456789")

    print("0#", end='')
    Rethreader(print, [(i, {'end': ''}) for i in range(10)]).run()
    print()

    print("1#", end='')
    Rethreader(print, [((i,), {'end': ''}) for i in range(10)]).run()
    print()

    print("2#", end='')
    Rethreader(queue=[(print, i, {"end": ''}) for i in range(10)]).run()
    print()

    print("3#", end='')
    Rethreader(queue=[(print, (i,), {"end": ''}) for i in range(10)]).run()
    print()

    print("4#", end='')
    t = Rethreader(print).start()
    for i in range(10):
        t.add(i, end='')
    while not t.is_empty():
        pass
    t.quit()
    print()

    print("5#", end='')
    t = Rethreader(print).start()
    for i in range(10):
        t.add((i,), end='')
    while not t.is_empty():
        pass
    t.quit()
    print()

    print("6#", end='')
    t = Rethreader(print).start()
    for i in range(10):
        t.add(i, {"end": ''})
    while not t.is_empty():
        pass
    t.quit()
    print()

    print("7#", end='')
    t = Rethreader(print).start()
    for i in range(10):
        t.add((i,), {"end": ''})
    while not t.is_empty():
        pass
    t.quit()
    print()

    print("8#", end='')
    t = Rethreader().start()
    for i in range(10):
        t.add(print, i, end='')
    while not t.is_empty():
        pass
    t.quit()
    print()

    print("9#", end='')
    t = Rethreader().start()
    for i in range(10):
        t.add(print, (i,), end='')
    while not t.is_empty():
        pass
    t.quit()
    print()

    print()

    print("Test 2: 0 11 22 33 44 55 66 77 88 9")

    print("0#", end='')
    Rethreader(print, [(i, i + 1, {'end': ''}) for i in range(9)]).run()
    print()

    print("1#", end='')
    Rethreader(print, [((i, i + 1), {'end': ''}) for i in range(9)]).run()
    print()

    print("2#", end='')
    Rethreader(queue=[(print, i, i + 1, {"end": ''}) for i in range(9)]).run()
    print()

    print("3#", end='')
    Rethreader(queue=[(print, (i, i + 1), {"end": ''}) for i in range(9)]).run()
    print()

    print("4#", end='')
    with Rethreader(print) as t:
        for i in range(9):
            t.add(i, i + 1, end='')
        while not t.is_empty():
            sleep(0.1)
    print()

    print("5#", end='')
    with Rethreader(print) as t:
        for i in range(9):
            t.add((i, i + 1), end='')
        while not t.is_empty():
            sleep(0.1)
    print()

    print("6#", end='')
    with Rethreader(print) as t:
        for i in range(9):
            t.add(i, i + 1, {"end": ''})
        while not t.is_empty():
            sleep(0.1)
    print()

    print("7#", end='')
    with Rethreader(print) as t:
        for i in range(9):
            t.add((i, i + 1), {"end": ''})
        while not t.is_empty():
            sleep(0.1)
    print()

    print("8#", end='')
    with Rethreader() as t:
        for i in range(9):
            t.add(print, i, i + 1, end='')
        while not t.is_empty():
            sleep(0.1)
    print()

    print("9#", end='')
    with Rethreader() as t:
        for i in range(9):
            t.add(print, (i, i + 1), end='')
        while not t.is_empty():
            sleep(0.1)
    print()

    print("0#", end='')
    with Rethreader() as t:
        for i in range(9):
            t.add(print, i, i + 1, {"end": ''})
        while not t.is_empty():
            sleep(0.1)
    print()

    print("1#", end='')
    with Rethreader() as t:
        for i in range(9):
            t.add(print, (i, i + 1), {"end": ''})
        while not t.is_empty():
            sleep(0.1)
    print()

    print()

    print("Test 3")

    t = Rethreader().start()
    for i in range(3):
        t.add(print, (i, "test"))
    while not t.is_empty():
        sleep(0.1)
    t.quit()
    print()

    t = Rethreader().start()
    for i in range(3):
        t.add(print, i, "test")
    while not t.is_empty():
        sleep(0.1)
    t.quit()
    print()

    t = Rethreader().start()
    for i in range(3):
        t.add(print, "test")
    while not t.is_empty():
        sleep(0.1)
    t.quit()
    print()

    t = Rethreader().start()
    for i in range(3):
        t.add(print, i)
    while not t.is_empty():
        sleep(0.1)
    t.quit()
    print()
