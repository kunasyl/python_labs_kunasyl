'''Степень'''
def power(a:float, n:int) -> float:
    return a**n

a, n = input().split()
print(power(float(a), int(n)))