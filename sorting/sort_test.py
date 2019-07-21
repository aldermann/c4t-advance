# import your sort functions here
from bubblesort import bubble_sort
from quicksort import quick_sort
from selectionsort import selection_sort

import random
import time as timePackage
import signal

random.seed()

def gen_list(ln):
    res = [None] * ln
    for id in range(ln):
        res[id] = random.randint(-ln, ln)
    return res


# include your functions here, in form of ("function name", function`)
funcs = [("bubble sort", bubble_sort), ("selection sort", selection_sort), ("quick sort", quick_sort)]
len_list = [1, 10, 100, 1000, 10000, 20000, 50000, 100000]
def time_out():
    raise Exception("timeout")

signal.signal(signal.SIGALRM, time_out)

def execute_test(ln, sort_func):
    total_time = 0
    for _ in range(5):
        ls = gen_list(ln)
        signal.alarm(1)
        start = timePackage.perf_counter_ns()
        try:
            sort_func(ls)
            signal.alarm(0)
        except Exception as exc:
            pass
        elapsed = timePackage.perf_counter_ns() - start
        if elapsed >= 1e9:
            return None
        total_time += elapsed
    return total_time

for name, sort_func in funcs:
    print("testing", name)
    test_pass = 0
    for ln in len_list:
        print("testing with lists of length", ln)
        time = execute_test(ln, sort_func)
        if time is None:
            print("time out")
            break
        else:
            print("average time:", time / 5000, "microsecond")
        test_pass += 1
    print("test passed:", test_pass, "/8")
    print("-----------------------")
