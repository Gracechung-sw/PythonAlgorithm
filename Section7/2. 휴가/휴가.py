# # 문제 해석이 중요한 문제!!
# # P가 1이면 1일이 걸린다는게 아니라 당일에 상담이 끝날 수 있다는 의미이다. 
# def DFS(inx, money):
#   global result
#   #기저조건 
#   if inx >= n: #시간이 다 되었을 때, 상담 스케줄 다 훑어봤을 때
#     result = max(result, money)
#     return
#   else:
#     DFS(inx+list[inx][0], money+list[inx][1])
#     DFS(inx+1, money)


# if __name__ == "__main__":
#   n = int(input())
#   list = [list(map(int, input().split())) for _ in range(n)]
#   result = -1
#   DFS(0, 0) #상담 inx(=걸린시간) 번 돈
#   print(result)


#위의 방법으로 하면 inx가 날짜-1이 되므로 헷갈린다 ㅠ 그래서 아에 inx을 'inx일'과 같이 쉽게 보기 위해선
def DFS(day, money):
  global result
  #기저조건 
  if day == n+1: #시간이 다 되었을 때, 상담 스케줄 다 훑어봤을 때
    result = max(result, money)
    return 
  else:
    if day+list[day][0] <= n+1: #이럴 때만 상담 가능
      DFS(day+list[day][0], money+list[day][1])
    #상담을 안하기로 했다면 그냥 
    DFS(day+1, money)


if __name__ == "__main__":
  n = int(input())
  list = [list(map(int, input().split())) for _ in range(n)] #[[3, 10], [2, 15], [1, 10], [1, 30], [2, 10]]
  list.insert(0, [0, 0]) #[[0, 0], [3, 10], [2, 15], [1, 10], [1, 30], [2, 10]]
  result = -1
  DFS(1, 0) #상담 inx(=걸린시간) 번 돈
  print(result)