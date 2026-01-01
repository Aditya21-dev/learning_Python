# Create a class where a decorator logs every time a method is called.

def log_call(func):
    def wrapper(self):
        print(f"Method {func.__name__} is called")
        func(self)
    return wrapper


class Robot:
    
    @log_call
    def activate(self):
        print("Robot activated successfully")





# Create a decorator that measures execution time of a class method.

import time

def time_check(func):
    def wrapper(self):
        start = time.time()
        func(self)
        end = time.time()
        print("Execution time:", end - start)
    return wrapper


class Task:
    
    @time_check
    def run(self):
        for i in range(1000000):
            pass
