N, k = map(int, input().split())

arr = [i for i in range(1, N+1) if N%i==0]

if(len(arr) < k):
    print(-1)
else:
    print(arr[k-1])

##그런데 위의 방법처럼 하면, k 번째 약수가 넘었는데도 계속 for문을 돌게 되고, N이 크면 그만큼 시간 복잡도 상 좋지 않다. 
##그래서 중간에 멈춰주는 것이 좋다. 

N, k = map(int, input().split())
cnt = 0

for i in range(1, N+1):
    if N%i==0:
        cnt+=1
    if cnt==k:
        print(i)
        break
else: #for문 뒤에 오는 else는 'for문이 다 돌았다면'이란 의미이다 
    print(-1)