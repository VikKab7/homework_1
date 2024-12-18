arr = list(map(int, input().split()))
if len(arr) == 0:
    print('')
else:
    maximum = arr[0]
    for num in arr:
        if num > maximum:
           maximum = num
    print(maximum)