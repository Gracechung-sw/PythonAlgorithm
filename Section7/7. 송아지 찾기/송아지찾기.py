from collections import deque

s, e = map(int, input().split())

MAX = 10000
dq = deque()
check = [0] * (MAX+10)

dq.append([s, 0]) #[위치, 점프 횟수]
check[s] = True

while dq:
  curr = dq.popleft()
  dist = curr[0] 
  level = curr[1]
  if(dist == e):
    print(level)
    break
  else:
    for next in (dist-1, dist+1, dist+5):
      if 0 < next <= MAX:
        if check[next]==False:
          dq.append([next, level+1])
          check[next] = True


