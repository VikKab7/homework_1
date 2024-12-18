arr= list(map(int, input().split()))
a = int(input())
k = 0
for x in arr:
    if  x== a:
       k += 1


print(k)