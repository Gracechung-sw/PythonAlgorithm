from collections import deque

n = int(input())
maps = [list(map(int, input().split())) for _ in range(n)]
check = [[0]*n for _ in range(n)]

cnt = 0 #사과개수
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
dq = deque()

level = 0 #BFS 단계
inx = 1 #단계마다의 node 개수
dq.append([n//2, n//2])
check[n//2][n//2] = 1

while dq:
  if level > n//2:
    print(cnt)
    break
  
  for _ in range(len(dq)):
    curr = dq.popleft()
    y = curr[0]
    x = curr[1]
    cnt += maps[y][x]
    for i in range(4):
      nexty = y+dy[i]
      nextx = x+dx[i]
      if 0<=nexty<n and 0<=nextx<n:
        if check[nexty][nextx] == 0:
          dq.append([nexty, nextx])
          check[nexty][nextx] = 1
  level += 1


    



