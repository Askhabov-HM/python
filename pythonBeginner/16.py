# was lambda function
# it is not interesting for me
# will learn when it will need

def recursionFunc(a,b):
    if(b == 0):
        return 1
    else:
        return (a * recursionFunc(a, b-1))

print(recursionFunc(2, 10))

x, *y = 1,2,3,4,5 #остаточный параметр


def someFuncWithProps(y2):
    for x2 in range(*y2):
        print(x2)
    
someFuncWithProps([1,5])

def namedProps(**args):
    print(args) # выводит словарь

namedProps(arg1=1, arg2=2, arg3=3)

def funcWithCallback(param, callback):
    if callback():
        print('param ' + str(param))
    else:
        print('callback is failed')

def likeCallback():
    print('callback is called')
    return True

funcWithCallback(10, likeCallback)