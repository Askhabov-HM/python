def squareNumber(firstNum, secondNum=10):
    if(0 < firstNum < 10):
        return firstNum * firstNum
    elif(firstNum%2 == 0):
        return firstNum/secondNum
    else:
        return 'number is less than zero'

theNumber = int(input('Please enter the number: '))
print(squareNumber(theNumber))