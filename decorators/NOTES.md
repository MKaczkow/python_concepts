# Closures and decorators

## Closure
Closure is an inner function that has access and remembers to variables
in local scope in which it was created, even after the outer function 
has finished executing - "closes" free variables from outer function.  

## Decorators 
Decorator is a function that takes some function as argument, 
adds some functionality and returns given function, all without changing
it's source code.  

### Syntax 
@decorator_function
def sample_function():
    print('Hello World')

is equivalent to

sample_function = decorator_function(display)  

### Chaining decorators
Chaining decorators (and not getting unexpected results) requires using
  
from functools import wraps  
  
and then putting   
@ wraps  
befor wrapper_function(*args, **kwargs)