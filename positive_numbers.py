arr= list(map(int, input().split()))
k = 0
for num in arr:
    if num > 0:
        k += 1

print(k)