########Куча
# Свойства:
# 1) Каждая родительская вершына меньше потомков по числовому значению
# 2) Глубина всех листьев отличается не больше чем на единицу
# Глубина вершыны это кратчайшый путь от этой вершыны до корня
# 3) Последний слой заполняется слева направо без пробелов
# Можно сделать кучу и в обратном порядке - по убыванию -
# тогда каждая родительская вершына больше потомков по числовому значению,
# а корень имеет максимальное значение

# Двоичную кучу удобно представлять в массиве, перечисляя элементы начиная с корня
# В двоичной куче у - iго элемента потомки имеют номера 2i + 1 и 2i + 2
# А предок iго элемента имеет номер (i-1)//2

class Heap:
    def __init__(self):
        self.values = []
        self.size = 0
    # добавление элементов в кучу
    def insert(self, x):
        self.values.append(x)
        self.size += 1
        self.lift_up(size-1)
    def lift_up(self, i):
        while i != 0 and self.values[i] < self.values[(i-1)//2]:
            self.values[i], self.values[(i-1)//2] = self.values[(i-1)//2], self.values[i]
    def extract_min(self):
        tmp = self.values[0]
        self.values[0] = self.values[-1] # -1 - индекс последнего элемента в списке в питоне
        self.values.pop() # Удаляет последний элемент из списка
        self.size -= 1
        self.lift_down(0)
    def lift_down(self, i):
        while 2*i+1 < self.size: # непонятный символ на месте i
            j = i
            if self.values[2*i+1] < self.values[i]:
                j = 2*i + 1
            if 2*i+2 < self.size and self.vakues[2*i+2] < self.values[j]:
                j = 2*i + 2
            if i == j:
