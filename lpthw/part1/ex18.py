def print2(*args):
    arg1,arg2 = args
    print("arg1:%r, arg2:%r" %(arg1,arg2))

def print1(arg1):
    print("arg1: %r" % arg1)

def print_none():
    print("I have no args")

print2(1,2)
print1(34)
print_none()