"""The python code helps to read the command line input for curl method."""
"""
Imports the sys library so that we can use the functions in it.
"""
import sys
"""
from lib.helper class imports curl function
"""
from lib.helper import curl
"""
Value None is assigned to the variable URL of NoneType
"""
URL = None
"""
The number of commond-line arguments in the list is decremented
by 1 and the value is assigned to ARG_CNT variable
"""
ARG_CNT = len(sys.argv) - 1
"""
Prints the String in the print funtion if ARG_CNT value is not equal to 1
"""
if ARG_CNT != 1:
    print('Usage: curl [URL]...')
"""
Second argument on the console is stored in to URL variable if ARG_CNT 
variable value is 1 and if http is not the start of second argument,
https:// is appended before the second argument and is stored in URL variable.
Curl function is called with URL variable as argument and return value is printed
on the terminal.
"""
if ARG_CNT == 1:
    URL = sys.argv[1]
    if 'http' not in URL[:5]:
        URL = "http://"+URL
    print(curl(URL))
