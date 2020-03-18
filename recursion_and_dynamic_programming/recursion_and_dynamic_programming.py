##### Задача о рюкзаке
# Есть рюкзак, в который можно положыть максимальную массу М
# Есть предметы с разной массой и стоимостью.
# Общая масса предметов больше массы рюкзака
# Вопросы могут быть такими:
# Как положыть в рюкзак максимальный вес?
# Как положыть максимум по стоимости?
# Максимум по весу и по объёму?
# Если количество предметов равно N,
# то количество выборок предметов равно 2 ** N

##### Дискретная задача о рюкзаке
# F(i, k) - макс. стоимость предметов, которая помещается в рюкзак ёмкость к,
# при этом можно изпользовать только первые i предметов
# - стоимость, m - масса

# F(k, i) = v[i] + F(k-m[i], i-1) - если берём iй предмет
# F(k, i) = F(k, i-1)- если не берём
# Как решыть, брать или не брать?
# надо взять максимум
# F(k, i) = max(v[i]+F(k-m[i], i-1), F(k, i-1))

def beg(M, m:list, v: list):
    # m = [0] * N
    # v = [0] * N
    N = len(v)
    F = [[0] * (N + 1) for i in range(M + 1)]  # N - кол-во предметов, N - общая масса
    for i in range(1, N):
        for k in range(1, M+1):
            if m[i] <= k:
                F[k][i] = max(F[k][i-1], v[i]+F[k-m[i]][i-1])
            else:
                F[k][i] = F[k][i-1]
    return F[M][N]

m = [1, 4, 5, 8, 2, 9, 8]
v = [14, 3, 15, 6, 12, 3, 1]

print(beg(24, m, v))

