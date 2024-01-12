# useful-decorators
Random vaguely useful decorators.
The main idea of decorators is to wrap a function, adding some functionality. This leverages Python's implementation of functions as first-class citizens.

Some notes:
- The `functools.wraps` is used to make sure our wrapper functions do not overwrite important attributes of the function we are decorating, such as the name, docstring etc. 
- The following two syntaxes are equivalent:
```
@decorator
def f():
    print("Hello world!")

f = decorator(f)
```
- When using additional arguments to the decorator, the syntax is evaluated as:
```
@decorator(wait=1)
def f():
    print("Hello world!")

f = decorator(wait=1)(f)
```



Inspired from https://realpython.com/primer-on-python-decorators.