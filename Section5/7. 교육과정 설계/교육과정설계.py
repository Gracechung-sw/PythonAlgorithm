from collections import deque

necessary = input()
n = int(input())

for i in range(n):
  schedule = input()
  #매번 YES, NO검사해주어야 하므로 필수과복 큐 자료구조 초기화
  queue = deque(necessary)
  for curr in schedule:
    if curr in queue: #필수과목이라면
      # 이제 순서 맞는지 검사
      if curr != queue.popleft(): #순서 x
        print("#{} NO".format(i+1))
        break
      else: #순서 o 
        pass #계속
      
  else: #필수 과목이 아니라면
    # 필수과목을 다 넣었는지 검사
    if len(queue) != 0: # 다 안 넣음
      print("#{} NO".format(i+1))
    else: #다 넣음
      print("#{} YES".format(i+1))


      
  