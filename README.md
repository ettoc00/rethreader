# Rethreader


# Usage 
## Initialization
Every parameter is optional at the initialization.

 
 
Rethreader(target, queue, max_threads, clock_delay, auto_quit, daemon)

 

- target (function): the target of the treads

- queue (iterable): list of the arguments of the threads

- max_threads (integer): the maximum number of running threads (default: 16)

- clock_delay (float): the speed of the clock (default: 0.01)

- auto_quit: whether the rethreader stops after completing the queue (default: True if there's a queue, else False)

- daemon: whether the threads are daemonic (default: None, handled by the threading library)


Compatible with the "with" statement

## Properties

- finished: (int) number of finished threads

- in_queue: (int) number of threads in the queue or waiting to be appended to the queue

- remaining: (int) number of remaining threads

- results: (list) list of the returns of the functions

## Functions

If not specified, the function returns the rethreader.

 

- add(*args*): appends to the queue

- extend(iterable: *args*): extends the queue

- remove(*args*): removes from the queue or the running threads

- postpone(delay: float, *args*): removes *args*, then appends to the queue after the delay 

 

- run: runs the rethreader

- start: starts the rethreader

- quit: stops the rethreader

- is_alive: (bool) whether the rethreader is running

- is_empty: (bool) whether there are not remaining threads

## Argument input

If the target was specified in the initialization, append the arguments and the keyword arguments of the function, 
else the target must be the first element of the arguments.

```Python
with Rethreader(print) as rt:
    for i in range(10):
        rt.add(i)
```
```Python
with Rethreader() as rt:
    for i in range(10):
        rt.add(print, i)
```
Keywords arguments could be passed also through dictionaries.

```Python
with Rethreader(print) as rt:
    for i in range(10):
        rt.add(i, {"end": ''})
```
```Python
with Rethreader(print) as rt:
    for i in range(10):
        rt.add(i, end='')
```
The queue could already be passed in the initialization as a list of the arguments.

```Python
Rethreader(print, [(i, {"end": ''}) for i in range(10)]).start()
```
