"""Implementing the head shell command in python."""
"""
Imports system library so that we can use functions in it
"""
import sys
"""
from lib.helper class imports head and readfile functions
"""
from lib.helper import head, readfile
"""
Value None is assigned to the variable URL of NoneType
"""
TEXT = None
"""
The number of commond-line arguments in the list is decremented
by 1 and the value is assigned to ARG_CNT variable
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
Prints string argument in the print function if value of ARG_CNT variable is
greater than 1
"""
if ARG_CNT > 1:
    print("Usage: head.py <file>")
"""
Head function is called with TEXT variable as argument and retunrn value is
printed
"""
print(head(TEXT))
