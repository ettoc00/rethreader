from time import sleep
from rethreader._rethreader import KeyThread


def action():
    for i in range(10):
        print(i)
        sleep(4)


if __name__ == '__main__':
    kt = KeyThread.of(action).start()
    sleep(10)
    print(10)
    kt.kill()
