'''Какое из чисел больше'''
a = int(input())
b = int(input())
if a!=b:
    res = 1 if a>b else 2
else: res=0
print(res)