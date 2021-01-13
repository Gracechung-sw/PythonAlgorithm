n = int(input())
nums = list(map(int, input().split()))

leftInx=0
rightInx=n-1

temp=[]
result = ''
curr=-1

while leftInx<=rightInx:
  if nums[leftInx]>curr:
    temp.append(nums[leftInx], 'L')
  if nums[rightInx]>curr:
    temp.append(nums[rightInx], 'R')
    
  temp.sort() #이걸로 대소비교, 이런 값이 있는지 없는지까지 한번에 검사 가능
  if len(temp)==0:
    break
  else:
    result += temp[0][1] #sort()했으니 맨 앞에 있는 것이 curr보다는 크고 둘 중엔 더 큰것을 한 것이므로 temp[0][1]은 이런 값
    curr = temp[0][0]
    if tmp[0][1]=='L':
      leftInx=leftInx+1
    else:
      rightInx = rightInx-1

  temp.clear() #초기화

print(len(result)) #개수를 처음부터 하나씩 세는게 아니라 이렇게 배열의 길이가 개수를 나타낼 수 있다. 
print(result)
    

