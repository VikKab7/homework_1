a = int(input())
b = int(input())
m = int(input())
n = int(input())
if ((abs(a - m) - abs(b - n)) * (a - m) * (b - n)
or (b == m and b == n)) :
    print('NO')
else :
    print('YES')