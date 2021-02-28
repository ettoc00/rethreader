from time import sleep
from rethreader._rethreader import KeyThread


def action():
    for i in range(10):
        print(i)
        sleep(0.4)


if __name__ == '__main__':
    kt = KeyThread(None, action).start()
    sleep(1)
    print(1)
    kt.kill()
