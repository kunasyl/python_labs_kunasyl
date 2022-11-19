'''Максимум из трех'''
a = int(input())
b = int(input())
c = int(input())
if a>b:
    res = a if a>c else c
else:
    res = b if b>c else c
print(res)