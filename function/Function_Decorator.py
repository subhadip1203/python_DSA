# def decor(func):
#     def innerFunc():
#         print("inner function start" )
#         func()
#         print("inner function ends" )
#     return innerFunc

# def num():
#     print("inside num func")

# newfunc = decor(num)
# newfunc()


def decor(func):
    def innerFunc():
        print("inner function start" )
        func()
        print("inner function ends" )
    return innerFunc

@decor
def num():
    print("inside num func")

num()