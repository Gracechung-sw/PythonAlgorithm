
#가장 가까운 두 말의 최대 거리를 구하는 문제
#마구간이 일렬로 있기 때문에 마구간입력이 들어오면 정렬부터 한다. 
#말들은 1~마구간의 맨 끝 위치 사이에 있을 것이다. 
#그래서 가장 가까운 두 말의 최대 거리(이하 Shortest)는 1~마무간의 맨 끝 위치 사이에 있을 것이다. 
#여기서 BS 시작, mid가 shortest라고 하면, 모든 말 사이의 거리는 mid'이상'이어야 한다. 

#이때 (나에게는) 생각해내기 어려웠던 부분이 '반드시 첫 번째 말의 위치는 맨 앞 마구간'이라는 것이다. 
#왜 첫 번째 말의 위치는 맨 앞 마구간일까? 두 번째 말~C번째 말의 마구간은 어쨌든 첫번째 말 보다 뒤에 있을 텐데
#가장 멀리 떨어져있으려면 첫 번째 말이 최대한 앞에 있어야 할 것이다. 따라서 '최대한 앞'이 바로 '맨 앞 마구간' 이다. 

#모든 말 사이의 거리는 mid'이상' 인지를 검사해서 mid이상이면 okay++
#okay가 말의 수인 C보다 적으면 C마리 다 못들어간단는 거니까 mid가 좀 작아져야 한다. 
#okay가 C보다 크거나 같으면 C마리 다 들어갈 수 있다는 거니까 mid 좀 더 늘려봐서 Shortest의 최대값을 찾는다. 
#okay 개수 세는게 좀 복잡하므로 함수로 따로 뺀다. 

def Count(len):#모든 말 사이의 거리는 mid'이상' 인지를 검사해서 mid이상이면 okay++하는 함수
    okay = 1 #무조건 첫번째 마구간에 첫 번째 말은 들어가있으므로
    nextHome = location[0]

    for i in range(1, home):
        if(location[i]-nextHome >= len):
            okay+=1
            nextHome = location[i]

    return okay


home, horse = map(int, input().split())
location = []
# 한 줄로 주어지는게 아니라 줄바꿈으로 주어졌으니 for문 돌아야함
for _ in range(home):
    tmp = int(input())
    location.append(tmp)#https://hashcode.co.kr/questions/1160/%EB%BB%98%EC%A7%88%EB%AC%B8-%EC%99%9C-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%A6%AC%EC%8A%A4%ED%8A%B8%EB%8A%94-push%EA%B0%80-%EC%95%84%EB%8B%88%EB%9D%BC-append%EB%A5%BC-%EC%93%B0%EB%8A%94-%EA%B1%B8%EA%B9%8C%EC%9A%94

location.sort()

start = 1
end = location[home-1]

while(start<=end):
    mid = (start+end)//2

    if(Count(mid) < horse):
        #print("no mid", mid)
        end = mid-1
    
    else:
        result = mid
        start = mid+1
        #print("yes mid", mid)

print(result) 
# print(mid) #result에 mid를 저장하는 과정 없이 바로 mid를 출력해버린다면 해당 mid 일때 Count를 만족하지 않는(여기선 no mid 찍어봤을 때의 값) 값일지라도 while문이 끝났기때문에 출력되는 것일수도 있다. 
#그래서 안전하게 항상 답이 될 수있는 mid값을 result에 저장해두고 마지막엔 result를 출력하는 것이 좋다. 