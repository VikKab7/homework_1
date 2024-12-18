def rev():
    n = int(input())
    stroka = input()
    arr = list(map(int, stroka.split()))
    if len(arr) != n:
        print('')
        return
    rev = arr[::-1]
    print( *rev)

rev()