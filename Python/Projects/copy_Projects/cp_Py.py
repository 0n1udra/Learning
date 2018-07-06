#!/usr/bin/bash/env python
import sys
import os
import time

def timingFunc(func):
    def timing(*args, **kwargs):
        a = time.time()
        func(*args, **kwargs)
        print(f"{func.__name__}{args}: {time.time() - a:.8f} ")
        return func(*args, **kwargs)
    return timing

@timingFunc
def test_Func(x, y):
    return x * y

print(test_Func(10, 10))
