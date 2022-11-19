'''Конец уроков'''
n = int(input())
init_time = (9,0)
# print(f'{n:02}')
mins = n*45 + (n-1)//2*15 + ((n-1)//2+(n-1)%2)*5
final_hours = init_time[0] + mins//60
final_mins = init_time[1] + mins%60
final_time = f'{final_hours:02} {final_mins:02}'
print(final_time)