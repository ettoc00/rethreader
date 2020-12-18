from rethreader._rethreader import Rethreader, ThreadInfo

if __name__ == '__main__':
    print()
    a = print, (0, 1), 1, {'0': 0, '1': 1}
    print(a)
    ua = Rethreader()._unpack(a)
    print(ua)
    uua = Rethreader()._unpack(ua)
    print(uua)
    print(ua == uua)
    print()
    thi_1 = ThreadInfo(ua)
    print(thi_1)
    print(thi_1.string)
    thi_2 = ThreadInfo(thi_1.key())
    print(thi_1 == thi_2)
    thi_3 = ThreadInfo(thi_1.key())
    print(thi_3 == thi_2)
