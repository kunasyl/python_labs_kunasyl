'''Существует ли треугольник'''
a = int(input())
b = int(input())
c = int(input())
res = 'YES' if a+b>c and a+c>b and b+c>a else 'NO'
print(res)