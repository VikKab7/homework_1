arr = list(map(int, input().split()))
k= int(input())
n = len(arr)
if n > 0:
  k = k % n
  arr2 = arr[-k:] + arr[:-k]
print(arr2)