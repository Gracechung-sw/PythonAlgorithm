N = int(input())

arr = list(map(int, input().split()))


avg = round(sum(arr)/N) 
#sum: list안의 값을 함해주는 것. for문 돌려서 하나하나 더할 필요 없음
#round: 소수 첫째자리에서 반올림 하여 정수로 만드는 함수

#값과 학생번호(index)가 둘 다 필요하므로 enumerate를 사용한다. 는게 핵심이다. 
min = 2147000000 #정수 중 가장 큰것으로 최소값 초기화
for inx, score in arr:
    temp = abs(avg-score)
    if min>temp: # 등식 빼줌으로써 답이 되는 점수가 여러 개일 경우 번호가 빠른 학생의 번호를 답으로 한다.를 충족해준다.
        min = temp
        thatscore = score
        studentnum = inx+1 #+1하는 것 주의!! inx 0 인 학생 번호가 1번 이므로 
    else if min == temp: # 답이 2개일 경우 성적이 높은 학생의 번호를 출력하세요. 이 조건을 만족하기위해 같은 경우, 실제 점쑤 중 어느것이 더 큰지(양수인지)확인 해야 한다. 
        if(thatscore<score):
            thatscore = score
            studentnum = inx+1

print(avg, studentnum)

    


