'''Сумма чисел'''
n = int(input())
nums = []
for _ in range(n):
    i = int(input())
    nums.append(i)
print(sum(nums))
