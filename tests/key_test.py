from rethreader import Rethreader

if __name__ == '__main__':
    print()
    a = 0, (0, 1), 1, {'0': 0, '1': 1}
    print(a)
    ua = Rethreader()._unpack(a)
    print(ua)
    uua = Rethreader()._unpack(ua)
    print(uua)
    print(ua == uua)
    print()
