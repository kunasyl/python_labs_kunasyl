'''Голосование'''
def election(*args) -> int:
    cnt_0, cnt_1 = 0, 0
    for i in args:
        if int(i) == 0:
            cnt_0 += 1
        else:
            cnt_1 += 1
    return 0 if cnt_0>cnt_1 else 1

x, y, z = input().split()
print(election(x,y,z))