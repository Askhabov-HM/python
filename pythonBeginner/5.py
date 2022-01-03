x = int(input('input the x: '))

if(x > 0):
    if(x >= 1 and x <= 9):
        print('x is a digit: %d'%x)
    else:
        print('x is a number: %d'%x)
elif(x < 0):
    print('x is less than 0')
else:
    print('x is equal zero')