k, n = map(int, input().split())
arr = []
start = 0
end = 1000000

#띄어쓰기가 아니라 줄바꿈으로 배열 값이 입력되는 경우 split으로 못 읽고
#for문으로 하나하나 읽어야 함
for i in range(k):
    arr.append(int(input()))

while start <= end:
    cnt = 0
    mid = (start + end)//2

    for j in range(k):
        cnt += arr[j]//mid

    if cnt >= n:
       start = mid+1
       result = mid #n 개수 이상일 때 가장 긴 길이를 출력하는 것이므로 cnt == n 이라고해서 mid가 바로 답이 아니고, 갈때까지 갔을 때의 mid값을 구하는 것이다. 
    else :
        end = mid-1

print(result)

 
