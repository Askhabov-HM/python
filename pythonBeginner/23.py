# exceptions and error catching

def getValues():
    x = input('x: ')
    y = input('y: ')
    try:
        x = int(x)
        y = int(y)
        return x,y
    except ValueError as v:
        print(v)
        return 0,0
    finally:
        print('finally we print this')

x,y = getValues()
print(x,y)