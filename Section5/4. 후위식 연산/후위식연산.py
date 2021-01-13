str = input()

stack = []

for i in str:
  if i.isdigit(): #숫자
    stack.append(i)
  else:#연산자면 stack에서 계산할 숫자 2개 꺼내서 연산후 다시 push
    #이 때 주의할 것은 먼저 들어간 것이 앞에 있던 숫자라는 것! 
    # 5-2 와 2-5는 다르다!
    # 5/2 와 2/5는 다르다!
    num2 = int(stack.pop())
    num1 = int(stack.pop())
    if i == '+':
      stack.append(num1+num2)
    elif i == '-':
      stack.append(num1-num2)
    elif i == '*':
      stack.append(num1*num2)
    else:
      stack.append(num1/num2)

print(stack[-1])


    
