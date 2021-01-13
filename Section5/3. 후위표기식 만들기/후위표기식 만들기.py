str = input()
stack = []
res = '' #python에서 문자열은 +로 연결 할 수 있음

#숫자는 그냥 바로
#연산자의 경우 그 연산자보다 우선순위가 높거나 같으면 pop
#                             아니면 stop 하고 append

for i in str:
  if i == '(':
    stack.append(i)
  elif i == ')':
    while stack and stack[-1]!='(' :
      res += stack.pop()
    stack.pop()
  elif i=='*' or i=='/':
    while stack and (stack[-1]=='*'or stack[-1]=='/'):
      res += stack.pop()
    stack.append(i)
  elif i=='+' or i=='-':
    while stack and (stack[-1]=='+' or stack[-1]=='-' or stack[-1]=='*' or stack[-1]=='/'): #아니면 '(' 빼고 다니까, while stack and stack[-1]!='(': 로 해줘도 된다.
      res += stack.pop()
    stack.append(i)
  else: # 숫자인 경우
    res += i

# 그 다음에 str이 끝났을 때 stack에 남아있는 연산도 다 출력
while stack:
  res += stack.pop()

print(res)

