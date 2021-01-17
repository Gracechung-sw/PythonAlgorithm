import sys

def DFS(inx, sum):
  if inx >= n:
    if sum == (total-sum):
      print("YES")
      sys.exit(0) #프로그램 종료
  else:
    DFS(inx+1, sum+ch[inx]) #부분집합으로 사용하는 것
    DFS(inx+1, sum) #부분집합으로 사용하지 않는 것


if __name__ == "__main__":
  n = int(input())
  ch = list(map(int, input().split()))
  total = sum(ch)
  DFS(0,0)
  print("NO")
  