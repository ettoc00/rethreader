from rethreader import Rethreader

if __name__ == '__main__':
    f = lambda x: x * x - 34 * x + 36
    print([f(x) for x in range(40)])
    print(Rethreader(f, range(40)).run().results)
    print(Rethreader(f, range(41)).remove(40).run().results)
    r = Rethreader(f).start()
    print(r.multi_task(range(40)))
    print(r.multi_execute(range(40)))
    r.quit()
    print([f(x) for x in range(400)] == Rethreader(f, range(400)).run().results)
