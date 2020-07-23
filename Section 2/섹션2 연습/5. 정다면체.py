N, M = map(int, input().split())

cnt = [0]*(N+M+10)

for i in range(1, N+1): #0부터 시작하기때문에 range(N)해주면 안됨.
    for j in range(1, M+1):
        cnt[i+j]+=1

#이제 cnt list에서 최대값을 찾는다.
max = -1 
for i in range(n+m+1):
    if max < cnt[i]:
        max = cnt[i]

#이제 답 출력
for i in range(n+m+1):
    if cnt[i] == max:
        print(i, '')# 그냥 print(cnt[i]) 이렇게 하면 \n으로 출력되기 때문에 



