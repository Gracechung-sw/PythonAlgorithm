#1. N 입력받기
#2. NxN 행렬이 입력되지만, 나는 가장자리에 0을 넣은 행렬을 완성해야 함
#3. 모두 0으로 초기화된 (N+2)*2 행렬을 만들고
#4. arr[1:N, 1:N]은 주어진 값들로 채우기
#=> 3, 4는 이렇게 하는게 아니라, N*N 값 먼저 입력받고 insert, append이용해서 가장자리에 0을 덧붙여줌
#5. 1:N까지 돌면서 동서남북 보다 크면 cnt+=1
#6. cnt 출력

N = int(input())

arr = [list(map(int, input().split())) for col in range(N)]

arr.insert(0, [0 for row in range(N)])
arr.append([0 for row in range(N)])
for i in range(N+2):
    arr[i].insert(0, 0)
    arr[i].append(0)

cnt = 0
# for i in range(1, N+1):
#     for j in range(1, N+1):
#         currValue = arr[i][j]
#         if(currValue>arr[i-1][j] and currValue>arr[i+1][j]
#             and currValue>arr[i][j-1] and currValue>arr[i][j+1]):
#             cnt+=1


# if(currValue>arr[i-1][j] and currValue>arr[i+1][j]
#             and currValue>arr[i][j-1] and currValue>arr[i][j+1]):
# 이 부분을 한 줄로 바꿔적을 수 있다. 
# python all 함수: https://codepractice.tistory.com/87

#동, 서, 남, 북
dx = [1, -1, 0, 0]
dy = [0, 0, +1, -1]

for i in range(1, N+1):
    for j in range(1, N+1):
        if all(arr[i][j] > arr[i+dy[direction]][j+dx[direction]] for direction in range(4)):
            cnt += 1

print(cnt)



