from collections import deque

n = 7
maps = [list(map(int, input().split())) for _ in range(n)]
check = [[-1]*n for _ in range(n)]

dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]

#시작
dq = deque()
dq.append((0, 0)) #y, x
check[0][0] = 0

while dq:
  curr = dq.popleft()

  for i in range(4):
    nexty = curr[0]+dy[i]
    nextx = curr[1]+dx[i]
    if 0<=nexty<n and 0<=nextx<n and maps[nexty][nextx] == 0 and check[nexty][nextx] == -1:
      dq.append((nexty, nextx))
      check[nexty][nextx] = check[curr[0]][curr[1]]+1

#목적지 도착했는지 확인
if check[6][6] == -1: #못 간 것이므로
  print(-1)
else:
  print(check[6][6])



