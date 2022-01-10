def sq(x):
    print(x**2)
    return x**2

mas = [1,2,3,4,5]
print(list(map(sq, mas)))


def mapStr(char):
    print(char)
    return char

stringForMap = 'Text'
print(list(map(mapStr, stringForMap)))


# def odd(x):
#     return not x%2

numbersForFilter = [1,2,3,4,5,6,7]

print(list(filter(lambda x: not x%2, numbersForFilter)))

# some zip func
# but i'm lazy