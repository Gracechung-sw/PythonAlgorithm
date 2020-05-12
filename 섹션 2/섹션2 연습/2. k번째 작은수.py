T = int(input())

for t in range(T):  
    N, s, e, k = map(int, input().split())

    arr = list(map(int, input().split()))
    arr = arr[s-1:e].sort()

    print('#' + t+1 + ' ' + arr[k-1])

