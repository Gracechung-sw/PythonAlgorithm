num, m = map(int, input().split())
num = list(map(int, str(num))) #각 자리수에 있는 숫자 하나하나에 접근 할 수 있기 때문
# print(num)

stack = []
for currNum in num: #각 숫자를 돌면서
  #pop한다 언제까지? 
  #stack에 pop할 게 남아있고, 삭제해야만 하는 개수 m이 아직 남아있고, stack의 top이 나보자 작으면
  while stack and m>0 and stack[-1]<currNum:
    stack.pop()
    m -= 1 #하나 pop했으니까 삭제해야만 하는 개수도 하나 줄여준다. 
  #이후 빠져나오면 나를 push한다. 
  stack.append(currNum) #python에서는 push가 아닌 append사용

#그런데 이 경우 내 앞의 숫자들이 다 나보다 커서 더이상 pop이 일어ㅏ지 않고 push 만 되어서
# 삭제해야만 하는 개수 m이 아직 남아있는 경우가 있다. 
# 이 경우 어짜피 stack에 들어있는 수는 내림차순으로 들어있기 때문에 m개만큼 뒤를 잘라주면 된다. 
if m!=0:
  stack = stack[:-m]
#이제 list형식의 stack에 들어있는 각 숫자를 하나의 문자열로 붙여주면 답 완료
result = ''.join(map(str, stack))
print(result)#정답

  
