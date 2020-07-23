arr = list(range(1, 21)) 

for _ in range(10):
    a, b = map(int,input().split(' ')) 
    # arr[a:b+1] = arr[a:b+1:-1] #이렇게 하면 안된다. 하나씩 바꿔줘야 하는가보다. 
    for i in range((b-a+1)//2): #그 구간의 길이만큼 도는데, 
        arr[a+i-1], arr[b-i-1] = arr[b-i-1], arr[a+i-1] #이렇게 앞뒤를 바꿔준다. 
        #-1이 있는 이유는 값은 1, 2, 3, ..., 21이지만 그것의 index는 0, 1, 2, ..., 20이기 때문이다. 


print(arr)

#############-1처럼 index 랑 그것의 값이 달라서 신경써줘야 하는 것을 없애려면
############ index가 1, 2, 3, ...20 인 것에 값도 1, 2, 3, ...., 20 이도록 넣어주면 ㄴ된다.
############ 단, 이때는 arr[0] = 0도 있으니 맨 처음 값을 pop()해서 없애줘야 한다. 
'''
arr = list(range(21))

for _ in range(10):
    a, b = map(int, input.split(' '))
    for i in range((b-a+1)//2):
        arr[a+i], arr[b-i] = arr[b-i], arr[a+i]
    arr.pop()

print(arr)
'''