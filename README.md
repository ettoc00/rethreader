# Rethreader

# Intro & Examples

Rethreader is born as a thread pool for a function:
```Python
rt = Rethreader(sum)
rt.start()              # Start the thread pool
rt.add([1, 2, 3])       # Add sum([1, 2, 3]) to the queue
rt.add(range(10))       # Add sum(range(10)) to the queue
rt.quit()               # Quit the thread pool
rt.results              # Return the results
>> [6, 45]
```
But it could be used as a generic thread pool:
```Python
rt = Rethreader()
rt.start()
rt.add(sum, [1, 2, 3])                      # Add sum([1, 2, 3]) to the queue
rt.add(sum, range(10))                      # Add sum(range(10)) to the queue
rt.add(sorted, [3, 9, 6], reverse=True)     # Add sorted([3, 9, 6], reverse=True) to the queue
rt.quit()
rt.results
>> [6, 45, [9, 6, 3]]
```
It also supports the "with" statement:
```Python
with Rethreader(sum) as rt:         # Implicit rt.start()
    rt.add([1, 2, 3])
    rt.add(range(10))
                                    # Implict rt.quit() at exit
rt.results
>> [6, 45] 
```
It can aslo recieve the list of the different arguments at the initialization:
```Python
rt = Rethreader(sum, [[1, 2, 3], range(10)])
rt.add([2, 4, 8])
rt.start()
rt.add([8, 9, 10])
rt.quit()
rt.results
>> [6, 45, 14, 27] 
```
If all the queue is passed before the thread pool starts, the rethreader can simply be run:
```Python
list_of_args = [
    [1, 2, 3], 
    range(10), 
    [2, 4, 8]
]

rt = Rethreader(sum, list_of_args)
rt.run()                                        # rt.start() & rt.quit()
rt.results
>> [6, 45, 14] 
```
Most of the class functions return the rethread itself, so they can be chained:
```Python
Rethreader(sum, [[1, 2, 3], range(10)]).add([2, 4, 8]).run().results
>> [6, 45, 14] 
```
It has a lot of keyword arguments to be personalized with:
```Python
from urllib.request import urlretrieve

with Rethreader(urlretrieve, max_threads=4, clock_delay=2, save_results=False) as rt:
    for url, file in [...]:
        rt.add(url, file)
```
Note that it is much slower than mapping for fast offline functions:
```Python
squares = [x*x for x in range(999)]                             # ~0.5 milliseconds
squares = list(map(lambda x: x*x, range(999)))                  # ~1 millisecond
squares = Rethreader(lambda x: x*x, range(999)).run().results   # ~1 second
squares = Rethreader(lambda x: x*x, range(999), 
           clock_delay=0).run().results                         # ~120 milliseconds

```
However, it's more userful with internet requests

```Python
# Headlines from newspapers example
from requests_html import HTMLSession

session = HTMLSession()

def get_headlines(url):
    request = session.get(url)
    h3_tags = request.html.find('h3')
    h3_texts = [h3.text for h3 in h3_tags]
    return h3_texts
    
news = ['https://www.nytimes.com/',     'http://www.asahi.com/ajw/',
        'https://www.theguardian.com/', 'https://www.wsj.com/',
        'https://www.bbc.com/',         'https://www.smh.com.au/']

headlines = [get_headlines(url) for url in news]           # ~4.5 seconds
headlines = Rethreader(get_headlines, news).run().results  # ~0.75 seconds
```

# Usage 
## Initialization
Every parameter is optional at the initialization.

 
 
Rethreader(target, queue, max_threads, clock_delay, auto_quit, daemon)

 

- target (function): the target of the treads

- queue (iterable): list of the arguments of the threads

- max_threads (integer): the maximum number of running threads (default: 16)

- clock_delay (float): the speed of the clock (default: 0.01)

- auto_quit: whether the rethreader stops after completing the queue (default: True if there's a queue, else False)

- save_results: whether the rethreader has to save the returns of the functions (default: True)

- daemon: whether the threads are daemonic (default: None, handled by the threading library)


Compatible with the "with" statement

## Properties

- finished: (int) number of finished threads

- in_queue: (int) number of threads in the queue

- remaining: (int) number of remaining threads (active and in queue)

- results: (list) list of the returns of the functions (for not finished threads, inserts a None)

## Functions

If not specified, the function returns the rethreader.

 Basic functions:

- add(*args*): appends to the queue
  
- extend(iterable: *args*): extends the queue

- remove(*args*): removes from the queue or the running threads

- auto_quit(bool): whether the rethreader stops after finishing the queue (True if not specified)

- run: runs the rethreader (if auto_quit is not enabled, this will run until killed)

- start: starts the rethreader in a thread

- quit: finish the queue, then stops the rethreader

- kill: empties the queue and stops immediatly the rethreader

- is_alive: (bool) whether the rethreader is running

- is_empty: (bool) whether there are not remaining threads

Advanced functions:

- postpone(delay: float, *args*): removes *args*, then appends to the queue after the delay 

- insert(*args*): insterts at the start of the queue

- prioritize(iterable: *args*): extends the start the queue

- find(*args*): (Key/KeyThread) returns the thread or its info

- task(*args*): appends to the queue and waits until returned

- execute(*args*): inserts into the start of the queue and waits until returned



## Argument input

The list of arguments can be passed both initially and after the declaration of the rethreader


```Python
rt = Rethreader(print, range(10))
# rt.run()
```
```Python
with Rethreader(print) as rt:
    rt.extend(range(10))
```
```Python
with Rethreader(print) as rt:
    for i in range(10):
        rt.add(i)
```
```Python
rt = Rethreader(print)
# rt.start()
for i in range(10):
    rt.add(i)
# rt.quit()
```
Keywords arguments could be passed also through a dictionary.

```Python
with Rethreader(print) as rt:
    for i in range(10):
        rt.add(i, end='')
```
```Python
with Rethreader(print) as rt:
    for i in range(10):
        rt.add(i, {"end": ''})
```