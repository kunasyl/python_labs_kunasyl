'''Перевод числа'''
n = str(input())
res = []
for i in range(len(n)):
    res.append(int(n[i]) * 2**(len(n)-i-1))
print(sum(res))