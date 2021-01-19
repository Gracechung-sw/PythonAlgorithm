def DFS(inx, A, B, C):
  global result
  #기저조건
  if inx >= n:
    # A, B, C 중 같은게 있는지 확인
    abc = set()
    abc.add(A)
    abc.add(B)
    abc.add(C)
    if len(abc)==3: #즉, 같은게 없으면
      result = min((max(A, B, C)-min(A, B, C)), result)

  #아니면
  else:
    DFS(inx+1, A+list[inx], B, C)
    DFS(inx+1, A, B+list[inx], C)
    DFS(inx+1, A, B, C+list[inx])

if __name__ == "__main__":
  n = int(input())
  list = [int(input()) for _ in range(n)]
  result = 1000000000
  DFS(0, 0, 0, 0) #동전의 inx, A, B, C 의 금액
  print(result)
