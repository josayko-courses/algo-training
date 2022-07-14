from timeit import default_timer as timer
from datetime import timedelta
from collections import namedtuple

Result = namedtuple("Result", "time rval")


def chrono(func: callable, *args) -> Result:
    start = timer()
    rval = func(*args)
    end = timer()
    return Result(timedelta(seconds=end - start), rval)
