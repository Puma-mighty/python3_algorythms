# Стек (очередь lifo)
a = "pumacatpumacatpuma"
b = "puma"
print(a.count("puma"))
s = a.replace("puma", "tiger")
print(s)
L1 = [0, 1, 2, 3, 4]
L2 = L1[:]
print(L1 == L2) #True
print(L1 is L2) #False
L3 = L1[::-1]
print(L3) # [4, 3, 2, 1, 0]
L3[1:3]=[8, 16, 32, 64]
print(L3) # [4, 8, 16, 32, 64, 1, 0]
print(L3[10:20]) # []
# L3[::2] = [10, 20, 30]    Так нельзя! количество элементов в списке [10, 20, 30]
# print(L3) равно 3б а в изходном срезе через 2 шага 4 элемента. В этом случае количество
# элементов должно совпадать
L3[::2] = [10, 20, 30, 40] # а вот так можно
print(L3)   # [10, 8, 20, 32, 30, 1, 40]
s = sum(L3)
print(s) # 141

print()

######## Список строк
s = input("Введите ФИО ") # Введите ФИО Volkov Sergei Vasilievich
A = s.split()
print(A) # ['Volkov', 'Sergei', 'Vasilievich']
A[0] = A[0].upper()
print(A[0]) # VOLKOV
str1 = '-'.join(A)
print(str1) # VOLKOV-Sergei-Vasilievich
