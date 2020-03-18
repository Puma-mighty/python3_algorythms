

######classes and objects

class Goat:
    legs_number = 4
    def __init__(self, height, weight):
       self.height = height
       self.weight = weight
    def __str__(self): #У этого метода никаких параметров кроме
        #self быть не должно
        s = "weight = {}, height = {}".format(self.weight, self.height)
        return s

# После добавления веса и высоты в конструктор при создании
# объекта эти параметры будут требоваться
marusya = Goat(60, 40)
marusya.horns = 1

notka = Goat(65, 42)
notka.bell = "big"

#### так нельзя!!!
# A = [notka, marusya]
# for x in A:
#     print(x.horns)    AttributeError: 'Goat' object has no attribute 'horns'

# __init__ это конструктор
# Главная цель конструктора - иницыализацыя
# атрибутов конкретного экземпляра

for x in notka, marusya:
    print(x)
# Выведет: weight = 42, height = 65
# weight = 40, height = 60

notka.weight += 5 # 47
print(notka.weight) # 47
y = notka
y.height += 2
print(notka.height) # 67

print()
print(notka.legs_number)
notka.legs_number += 4
print(notka.legs_number)
print(marusya.legs_number)
print()

####### Именованные кортежы

from collections import namedtuple
Point = namedtuple("Point", "x y z")
A = Point(1, 0, 3)
# A.z *= 2  Так нельзя - ошыбка
print(A.z)
print()


####### Связный список
A = [1]
A.append([2])
A[1].append([3,A])
print(A)
print()

class LinkedList:
    def __init__(self):
        self._begin = None
    def insert(self, x):
        self._begin = [x, self._begin]
    def pop1(self):
        assert self._begin is not None, 'List is empty'
        x = self._begin[0]
        self._begin = self._begin[1]
        return x

a = LinkedList()
a.insert(5)
a.insert(10)
print(a.pop1())
print(a.pop1())
print(a.pop1())