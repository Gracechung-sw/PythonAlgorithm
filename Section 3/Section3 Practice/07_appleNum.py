N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

x = y = N//2
appleNum = 0

for i in range(N):
    #appleNum += arr[x-i][y] + arr[x+i][y] + arr[x][y-i] + arr[x][y+i] #이렇게 하면 + 모양으로 밖에 더해지지 않으니까
    for j in range(N):
        if((abs(y-i)+abs(x-j)) <= N//2):
            appleNum += arr[i][j]


print(appleNum)

# 1. 하나하나 가면서
# 2. 중심으로부터의
# 3. 거리를 계산하고
# 4. 해방 범위에 속하는 것만
# 5. 더해준다. 