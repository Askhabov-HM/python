# python хранит в переменной
# ссылку в памяти. В памяти хранится объект.
# У объекта есть св-ва и методы
someText = 'some text'
# покажет ссылку на переменную
print(id(someText))
# выведет тип данных в переменной
print(type(someText))
someNumber = 1
print(type(someNumber))

# Каскадное присваивание присвоит ссылку каждой переменной
x=y=z=0
print( id(x), id(y), id(z) )
# обратное действие
x2, y2, z2 = 1, 2, 3
print( id(x2), id(y2), id(z2) )

# True/False
trueFalse = True
