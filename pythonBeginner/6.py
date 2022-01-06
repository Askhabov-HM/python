i = 0 
while i < 5:
    
    if i == 0:
        print('warning the i is: %d'%i)
        i=i+1
        continue
    print('i is %d'%i)

    for x in range(1,11,1):
        print('nested cycle value: %d'%(x*i))

    i=i+1
else:
    print('it is from else block')
