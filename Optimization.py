# Decorator
from threading import Thread
import time
from functools import lru_cache


def my_decorator(func):
    def wrapper():
        print(f"Running {func.__name__}")
        func()
        print("Complete")
    return wrapper


@my_decorator
def do_this():
    print('Donig This')


@my_decorator
def do_that():
    print('Doing That')


do_this()
do_that()


# Threating functions


t1 = Thread(target=do_this)
t1.start()

t2 = Thread(target=do_that)
t2.start()
