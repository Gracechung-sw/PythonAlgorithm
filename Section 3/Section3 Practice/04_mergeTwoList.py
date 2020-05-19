

#sort()함수를 호출하면, nlogn 시간복잡도를 가진다. (퀵정렬)
#result = (arr1+arr2).sort()
#return result;
#그런데 이 문제의 경우는 정렬이 이미 되어있기때문에 n 번만에 끝낼 수 있다.
#  
N = int(input())
arr1 = list(map(int, input().split()))
M = int(input())
arr2 = list(map(int, input().split()))

n=m=0 #원래는 i=0 해서 result[i++] = arr1[n] 이런식으로 해주려고 했는데 필요없다. python엔 append 메소드가 있으니끼
result = []
while n < N and m < M :
    if arr1[n] < arr2[m] :
        result.append(arr1[n])
        n+=1
    
    else :
        result.append(arr2[m])
        m+=1
    

if n < N : #arr1이 남았다는 거니까 arr1 남은 것들은 그대로 result에 붙임
    #slice기능 사용해서 그냥 붙여버리기
    result += arr1[n:]
if m < M :
    result +=- arr2[m:]

print(result)