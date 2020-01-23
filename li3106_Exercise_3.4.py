#define a function with two arguments: a function and a value
def do_twice(fun, val):
    for times in range(2):
        fun(val)
#define a function with a value for print twice
def print_twice(St):
    for times in range(2):
        print(St)
do_twice(print_twice, 'spam')