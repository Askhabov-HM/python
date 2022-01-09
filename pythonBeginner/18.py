#local and global varibles

# nonlocal

a = 10

def someFunc(value):
    global a
    a = value
    b = value
    print('a: %s'%a)
    def innerFunc(innerValue):
        nonlocal b
        b = innerValue + ' :b' 
        print('inner func: %s'%b)
    innerFunc(b)

someFunc('20')