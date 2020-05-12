N, k = map(int, input().split())

arr = list(map(int, input().split()))

result = set()
result = [arr[i]+arr[j]+arr[r] for i in range(N) for j in range(i+1, N) for r in range(j+1, N)]

#print(result)

result = list(result)
result.sort(reverse=True)
 
#print(result)
print(result[k-1])
