def DFS(inx):
  global cnt

  if inx >= m:
    cnt += 1
    for i in range(m):
      print(ch[i], end=' ')
    print()
  else:
    for i in range(1, n+1):
      ch[inx] = i
      DFS(inx+1)

if __name__ == "__main__":
  n, m = map(int, input().split())
  cnt = 0
  ch = [0]*n
  DFS(0)
  print(cnt)