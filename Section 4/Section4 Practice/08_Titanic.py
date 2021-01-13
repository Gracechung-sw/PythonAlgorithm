
# 처음 생각해낸 방법은 내림차순 정렬 후 2명의 몸무게 더해서 제한 몸무게보다 작으면 Go cnt++ index+=2해주려고 했다. 
# 그런데 그러면 뒤로갈수록 2명을 태워도 제한무게보다 작고, 한명을 더 태울 수 있을 정도로 무게가 남게될 수ㅜ도 있다. 
# 이러면 최소 개수가 되지 않기 때문에
# 오름차순 정렬후
# 맨 앞사람과 맨 뒤사람을 함께 태우는ㄴ 방식으로 진행한다. 
# 그리고 list에서 pop(0)과 pop(-1)을 사용하면 이후 list의 element들의 재배치가 다시되어야한다는 비효율이 있기 때문에
# pointer만 바꿔주는ㄴ deque 자료구조를 이용하는 것이 좋다 
from collections import deque
n, limit=map(int, input().split())
weight=list(map(int, input().split()))
weight.sort()
weight=deque(weight)
cnt=0
while weight:
    if len(weight)==1:
        cnt+=1
        break
    if weight[0]+weight[-1]>limit:
        weight.pop()
        cnt+=1
    else:
        weight.popleft()
        weight.pop()
        cnt+=1
print(cnt)

