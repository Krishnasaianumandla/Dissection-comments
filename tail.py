"""Implementing the tail shell command in python."""
"""
Imports the sys library so that we can use the fuctions in it
"""
import sys
"""
from lib.helper module imports tail and readfile libraries
"""
from lib.helper import tail, readfile
"""
Value None is assigned to the variable TEXT of NoneType
"""
TEXT = None
"""
Number of command line arguments in the list is decremented by 1 and the value is
assigned to ARG_CNT variable
"""
ARG_CNT = len(sys.argv) - 1
"""
sys.stdin.read function reads lines from the console and assignes
them to TEXT variable if ARG_CNT = 0
"""
if ARG_CNT == 0:
    TEXT = sys.stdin.read()
"""
Second argument on the command line is assigned to filename variable,
readfile function takes filename as argument and return value is
assigned to TEXT variable if ARG_CNT = 1
"""
if ARG_CNT == 1:
    filename = sys.argv[1]
    TEXT = readfile(filename)
"""
Prints the string argument in the print function if ARG_CNT is greater than 1
"""
if ARG_CNT > 1:
    print("Usage: tail.py <file>")
"""
Calls the tail function with TEXT variable as argument and return value is printed
"""
print(tail(TEXT))
