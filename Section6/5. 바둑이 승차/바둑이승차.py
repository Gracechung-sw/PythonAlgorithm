

# def DFS(inx, sum, tsum):
#   global maxi #이렇게 하면 전역변수로 인식한다. 
#   if sum > max_weight: #일찍 cut edge
#     return
#   if sum + (total-tsum) < maxi: #현재 태운 강아지 무게와 남은 강아지 무게를 더했는데 최대값이 아니면 더이상 진행 하나마나
#     return
    
#   if inx == n:
#     if maxi < sum and sum <= max_weight: #여기서 UnboundLocalError: local variable 'maxi' referenced before assignment 에러가 발생ㅎ한다. maxi가 전역변수라고 생각했는데 왜 이런 에러가 발생하는 것일까?
#       #아래 maxi=sum 코드에서 선언과 값을 넣어주기 때문에 지역변수가 된다. 그래서 계속 argument로 가지고 다녀야 한다. 
#       maxi = sum 
#   else:
#     DFS(inx+1, sum+ch[inx], tsum+ch[inx])
#     DFS(inx+1, sum, tsum+ch[inx])


# if __name__ == "__main__":
#   max_weight, n = map(int, input().split())
#   ch = [int(input()) for _ in range(n)]
#   print(ch)
#   maxi = -1 #전역변수라고 생각했는데..!
#   total = sum(ch)
#   DFS(0, 0, 0)
#   print(maxi)



# def DFS(inx, sum):
#   global maxi
#   if inx >= n:
#     if maxi < sum and sum <= max_weight:
#       maxi = sum
#   else:
#     DFS(inx+1, sum+ch[inx])
#     DFS(inx+1, sum)


# if __name__ == "__main__":
#   max_weight, n = map(int, input().split())
#   ch = [int(input()) for _ in range(n)]
#   maxi = -1 #전역변수라고 생각했는데..!
#   DFS(0, 0)
#   print(maxi) 


#이렇게 해도 되지만 백트랙킹을 적용하여서 시간을 줄 일 수 있다. 
#1. 지금까지 태운 바둑이만으로도 max_weight를 넘어버리는 경우(DFS를 더 진행할 필요가 없다.)
# def DFS(inx, sum):
#   global maxi

#   if sum > max_weight:
#     return
#   if inx >= n:
#     if maxi < sum and sum <= max_weight:
#       maxi = sum

#   else:
#     DFS(inx+1, sum+ch[inx])
#     DFS(inx+1, sum)

# if __name__ == "__main__":
#   max_weight, n = map(int, input().split())
#   ch = [int(input()) for _ in range(n)]
#   maxi = -1 #전역변수라고 생각했는데..!
#   DFS(0, 0)
#   print(maxi) 

#더 cutout이 가능하다. 백트랙킹을 적용하여서 시간을 줄 일 수 있다. 
#2. 태울까 말까 검사를 한 바둑이를 제외하고 남은 바둑이를 다 테우더라도 이전에 나온 maxi값을 넘을 수 없다면? 더이상 DFS를 진행 할 필요가 없다. 
def DFS(inx, total, checksum):
  global maxi

  if total > max_weight:
    return
  if total + (sum(ch)-checksum) < maxi:
    return
  if inx >= n:
    if maxi < total and total <= max_weight:
      maxi = total

  else:
    DFS(inx+1, total+ch[inx], checksum+ch[inx])
    DFS(inx+1, total, checksum)

if __name__ == "__main__":
  max_weight, n = map(int, input().split())
  ch = [int(input()) for _ in range(n)]
  maxi = -1 #전역변수라고 생각했는데..!
  DFS(0, 0, 0)
  print(maxi)

