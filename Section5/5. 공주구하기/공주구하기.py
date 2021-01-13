from collections import deque

n, k = map(int, input().split())
prince = list(range(1, n+1)) #1부터 ~ n+1 까지 list 값으로 초기화되어서 배열이 생성됨. 
queue = deque(prince) #list를 deque자료형으로 변환

while(len(queue)!=1):
  for i in range(k-1):
    queue.append(queue.popleft())
  queue.popleft()

print(queue[0])

