def DFS(money_sum, num):
  global mini
  if money_sum > m or num > mini:
    return
  elif money_sum == m:
    if num < mini:
      mini = num
  else:
    for i in range(n):
      DFS(money_sum+ch[i], num+1)

if __name__ == "__main__":
  n = int(input())
  ch = list(map(int, input().split()))
  m = int(input())
  ch.sort(reverse=True)
  mini = m+10 #1원짜리로 다 바꿔봤자 m개가 최대이고, 안전하게 10개 더 해줌
  DFS(0, 0) #사용하기로 한 동전 값의 합, 사용한 동전 갯수
  print(mini)
