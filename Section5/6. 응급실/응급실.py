from collections import deque

n, m = map(int, input().split())

# 여기서 의문이 들 것이다. 
# Q. 위험도가 같은 것이 있고, queue자료구조에서 계속 위치가 바뀐다면 그 게 처음 m번째ㅐ 였다는 걸 어떻게 알 수 있지??
# A. 그렇기 때문에 처음 '번째'에 해당하는  index 값을 자신의 위험도와 같이 묶어서 저장해주어야 한다. 
# 나는 dict형식으로 하려고 했었다. 
# dic 형식으로 묶어보자. 
dangers = [{'inx':inx, 'danger': danger} for inx, danger in enumerate(list(map(int, input().split())))]
# print(dangers) #[{'inx': 0, 'danger': 60}, {'inx': 1, 'danger': 50}, {'inx': 2, 'danger': 70}, {'inx': 3, 'danger': 80}, {'inx': 4, 'danger': 90}]


# 튶플 형식으로 묶을 수도 있다. 
# dangers = [(inx, danger) for inx, danger in enumerate(list(map(int, input().split())))]
# print(dangers) #[(0, 60), (1, 50), (2, 70), (3, 80), (4, 90)]

# 큐 자료구조를 사용하자. 
queue = deque(dangers)
cnt = 0
while True:
  curr = queue.popleft()
  # 자신의 뒤에 자신보다 위험도가 큰게 있는지 검사해주어야 한다. 
  # 여기서 한 번 더 의문이 들 것이다. 
  # Q. 어떻게 값을 비교하지?
  # A. any를 사용!
  if any(curr['danger'] < x['danger'] for x in queue): # 이 구문을 살펴보자. for문이 돌면서 queue자료형에 있는 자료들을 하나하나 x로 접근한다. 
    # 뒤로 간다.
    queue.append(curr)
  else:
    #진료받자.
    cnt += 1
    #근데 그게 m번재 환자라면 
    if curr['inx']==m:
      print(cnt)
      break
  


