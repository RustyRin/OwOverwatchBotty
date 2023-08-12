'''
Function to print in a predictable and readable format
'''

import time

def bot_log(
        func1: str,
        func2: str = None,
        func3: str = None,
        desc: str = None):

    # I need to learn inline if else
    string = func1
    if func2 is not None:
        string += "\n\t" + func2
    if func3 is not None:
        string += "\n\t" + func3
    if desc is not None:
        string += "\n\t" + desc

    print(time.time(), string)
