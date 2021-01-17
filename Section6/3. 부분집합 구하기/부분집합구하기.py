def DFS(inx):
  if inx >= n+1:
    for i in range(1, n+1):
      if ch[i] == 1:
        print(i, end=' ')
    print() #줄바꿈

  else:
    ch[inx] = 1 #사용함
    DFS(inx+1)
    ch[inx] = 0 #초기화
    DFS(inx+1)


if __name__ == "__main__":
  n = int(input())
  ch = [0] *  (n+1)
  DFS(1)
