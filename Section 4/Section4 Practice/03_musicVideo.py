songs, dvd = map(int, input().split())
minute = list(map(int, input().split()))

def Check(capacity):
    total = 0 #한 dvd에 들어가는 곡 시간 
    cnt = 1 #필요한 dvd 개수 -> 이거 0이 아니라 1부터 시작해야한다는 것 조심

    for i in minute:
        if total + i > capacity:
            cnt += 1
            total = i
        else:
            total += i

    return cnt


start = 1
end = 1000

while start <=end:
    mid = (start + end)//2

    if Check(mid) <= dvd: #이 mid 값으로도 해당 dvd 개수로 저장가능하다면
        result = mid #일단 가능 한 것 이라고 저장해두고
        end = mid-1 # 용량 더 줄여본다. 
    else: #mid 값이 너무 작아서 안된다면
        start = mid+1 #용량 더 늘려본다. 

print(result) 

