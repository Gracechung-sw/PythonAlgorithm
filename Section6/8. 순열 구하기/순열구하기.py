def DFS(inx):
  if inx >= m:
    global cnt
    cnt += 1
    for i in result:
      print(i, end = ' ')
    print()

  else:
    for i in range(1, n+1):
      if check[i] == 0:
        result[inx] = i
        check[i] = 1
        DFS(inx+1)
        result[inx] = 0
        check[i] = 0

if __name__ == "__main__":
  n, m = map(int, input().split())
  cnt = 0
  check = [0]*(n+1)
  result = [0]*m
  DFS(0)
  print(cnt)