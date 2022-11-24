'''Минимальный делитель'''
x = int(input())
res = x
for i in range(int(x**0.5), 1, -1):
    if x%i == 0:
        res = i
print(res)