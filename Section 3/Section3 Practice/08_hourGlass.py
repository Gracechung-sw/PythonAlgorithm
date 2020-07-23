#1. 입력받기
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
M =  int(input())


#2. Queue 생각해보며 회전하기
for _ in range(M):
    rowNum, direction, length = map(int, input().split())
    
    if direction == 0 :
        for _ in range(length):
            arr[rowNum-1].append(arr[rowNum-1].pop(0))#.pop(이 자리에 있는 것을 pop해라(빼라))
    else:
        for _ in range(length):
            arr[rowNum-1].insert(0, (arr[rowNum-1].pop())) #insert(어느 자리에, 이걸 넣어라)
 #공부하고 외워야 할 것
 #알고리즘 생각 방향
 #python에서의 .append(-)
 #python에서의 .pop(_)
 #python에서의 .insert(_)

#3. 모래시계모양 합 구해주기
#사과나무와 같게
result = 0
start = 0
end = N
for i in range(N):
    for j in range(start, end):
        result += arr[i][j]
    if i<N//2:
        start+=1
        end-=1 #모래시계 위에서는 점점 좁혀지기
    else:
        start-=1 
        end+=1 #모래시계 아래에서는 점점 넓혀지기
         
print(result)
        


 

