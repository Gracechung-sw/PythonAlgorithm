def DFS(inx, money):
  global K, cnt
  if money > T: #다 탐색되었지 않더라도, 원하는 금액이 넘어버리면 더이상 진행하지 않아도 되니까
    return
  if inx >= K: #다 탐색했을 때, 
    if money == T: #원하는 금액이 만들어져있으면
      cnt += 1
  else:
    for i in range(list[inx][1]+1):
      DFS(inx+1, money+list[inx][0]*i)

if __name__ == "__main__":
  T = int(input())
  K = int(input())
  list = [list(map(int, input().split())) for _ in range(K)]
  cnt = 0
  DFS(0, 0) #동전 종류를 나타내는 inx, 동전으로 바꾼 돈의 양. 즉 시작은 0
  print(cnt)