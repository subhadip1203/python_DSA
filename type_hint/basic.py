'''
    in python : type hint is just hint , it doesnot effect code
    means , if we gave wrong type , it will work without any error

    to get error report , we need mypy 
    pip install mypy
    run : mypy basic.py
'''

def something (x: str , y: int) -> str :
    print(y)
    # return x
    return y
print(something ('test' ,2))