"""
Header Comments
File created on 02/05/2020 by Pin-Ching Li for ABE65100
This script is created to print a box with +,-,|
"""

# We use the same function for all questions
def print_border(columns):
    for i in range(columns):
        print ("+", "- " * 4,end ="")
    print("+")
def print_row(columns):
    for i in range(4):
        for j in range(columns):
            print ('|'," "*8,end ="")
        print ('|\n')

def block(rows,columns):
    for i in range(rows):
        print_border(columns)
        print_row(columns)
    print_border(columns)
# Two rows and two columns
block(3,3)
# Four rows and four columns
block(4,4)