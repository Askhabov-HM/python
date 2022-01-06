#Строка неизменяемый объект

longStr = '''это
многострочный
текст
'''
print(longStr, end='\n-----\n')

strWithNumber = 'string and number: ' + str(999)
print(strWithNumber, end='\n-----\n')

lengthOfStr = 'one two three'
print('length of str: %d'%len(lengthOfStr), end='\n-----\n')

subs = 'abc' in 'abcde' #return boolean
print('substring: ' + str(subs), end='\n-----\n')

ordOfChar = ord('t') #return number of char
print('order of charset in Unicode: ' + str(ordOfChar), end='\n-----\n')

repeatStr = 'it\n'
print(repeatStr*5, end='\n-+-+-')