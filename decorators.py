import functools
import time


def debugger(f):
    """Prints the input arguments and output provided to f.

    Args:
        f (Callable): any Python function

    Returns:
        Any: f(*args,**kwargs)
    """

    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        name = f.__name__
        unnamed = [repr(arg) for arg in args]
        named = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(unnamed + named)
        result = f(*args, **kwargs)
        if isinstance(result, tuple):
            res = [repr(r) for r in result]
        else:
            res = repr(result)
        print(f"{name}({signature}) = {res}")

        return result

    return wrapper


def delayer(wait=1):
    """Waits wait seconds before executing the function.

    Args:
        wait (int, optional): Seconds to wait before executing the function. Defaults to 1.

    Returns:
        Callable: Wrapper that waits wait seconds, then executre the function.
    """

    def delay_wrapper(f):
        time.sleep(wait)

        @functools.wraps(f)
        def wrapper(*args, **kwargs):
            r = f(*args, **kwargs)
            return r

        return wrapper

    return delay_wrapper


def cacher(f):
    """Caches the input and output provided to f.

    Args:
        f (Callable): any Python function

    Returns:
        Any: f(*args,**kwargs)
    """
    cache = {}

    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        unnamed = [repr(arg) for arg in args]
        named = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(unnamed + named)
        if signature not in cache:
            cache[signature] = f(*args, **kwargs)
        return cache[signature]

    return wrapper


### Examples
@debugger
def a_sum(a, b, c, d):

    return a + b, c + d


a = a_sum(0, 1, c=1, d=2)


@delayer(wait=5)
def another_sum(a, b):
    return a + b


b = another_sum(0, 1)


@cacher
def usual_sum(a, b):
    print(f"Computing {a} + {b}")
    return a + b


usual_sum(0, 1)
usual_sum(2, 1)
usual_sum(0, 1)
usual_sum(2, 1)
