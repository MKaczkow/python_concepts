# Profiling Code
* way to measure the performance of your code
* params like: execution time, memory usage, CPU usage, etc.
* identify bottlenecks and optimization opportunities

## cProfile
* built-in Python module for profiling code
* usage: `python -m cProfile main.py`
* expect results like:
```
7 function calls in 45.005 seconds

Ordered by: cumulative time

ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    1    0.000    0.000   45.005   45.005 {built-in method builtins.exec}
    1    0.000    0.000   45.005   45.005 main.py:1(<module>)
    1   45.005   45.005   45.005   45.005 main.py:10(factorial)
    2    0.000    0.000    0.000    0.000 {built-in method builtins.print}
    1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    1    0.000    0.000    0.000    0.000 main.py:3(add)
```

## Scalene
* ... is also cool
* `scalene main.py`

## Visualization
* `tuna`
* `snakeviz`

## References
* [quick yt tutorial](https://www.youtube.com/watch?v=BZzb_Wpag_M)
* 