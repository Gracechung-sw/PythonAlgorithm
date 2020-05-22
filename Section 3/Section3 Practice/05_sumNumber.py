#N개의 수로 된 수열 N<=10000
#이 수열의 i 번째 수 부터 j 번째 수까지의 합이 M 이 되는 경우의 수를 구하는 프로그램 M<=3억
#연속적인 부분집합의 원소의 수의 합
 

#arr[start]~arr[end]까지의 합을 start와 end를 바꿔가면서 구한다. 
#start: 0~<N 일때 end: start~<N 일때
#연속합: 연속합+arr[end] 이고, 
#연속합이 M인지 아닌지 검사해주어야 한다. 
#1. 연속합 < M => 더 더해본다.
#2. 연속합 == M => cnt++ 하고, start를 옆으로 이동시켜준다. 
    #왜냐하면 arr[]의 값은 항상 양수로, M이 나왔다면 arr[end]를 더 더해준다면 M보다 커질 일만 남았기때문에
#3. 연속합 > M => 이 arr[start]를 시작으로 하는 연속합에서는 M 이 나오지 않는다는 의미이므로 start를 옆으로 이동시켜준다. 

N, M = map(int, input().split())
arr = list(map(int, input().split()))

start = 0
end = 1
cnt = 0
sum = arr[start]

while start<N and end<N:
    if sum == M:
        #debugging
        #print(sum, start, end)
        #
        cnt += 1
        sum -= arr[start]
        start += 1

    elif sum < M :
        sum += arr[end]
        end += 1

    else:
        sum -= arr[start]
        start += 1

# while True:
#     if sum<M:
#         if end<N:
#             sum += arr[end]
#             end += 1
#         else:
#             break
#     elif sum == M:
#         cnt += 1
#         sum -= arr[start]
#         start += 1
#     else:
#         sum -= arr[start]
#         start += 1

print(cnt)









