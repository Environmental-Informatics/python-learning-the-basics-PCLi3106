"""
Header Comments
File created on 02/05/2020 by Pin-Ching Li for ABE65100

This script is written to do the function twice.

The function we are going to feed is a function to print string twice
 
"""

#define a function with two arguments: a function and a value

def do_twice(fun, val):
    # do the function with the input of argument for twice
    for times in range(2):
        fun(val)
#define a function with a value for print twice
def print_twice(St):
    # print St twice
    for times in range(2):
        print(St)
# do the function print_twice twice with the argument: spam string
=======
#define a function with two arguments: a function and a value
def do_twice(fun, val):
    for times in range(2):
        fun(val)
#define a function with a value for print twice
def print_twice(St):
    for times in range(2):
        print(St)
>>>>>>> 70899d371d4aee8548849a4f7f9dc9444e0bc68f
do_twice(print_twice, 'spam')