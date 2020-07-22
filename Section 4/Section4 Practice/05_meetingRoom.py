# 그리디 알고리즘:
# 문제를 풀어나가는 단계에 있어서 그 단계에서 가장 좋은게 뭔지를 보는 알고리즘이다.
# "가장 좋은 것"은 보통 정렬을 통해 알 수 있다.
# 따라서 대부분의 그리디 문제는 정렬을 동반한다고 보면 된다.

# 내가 생각한 알고리즘은
# 우선, 끝나는 시간이 빨라야 그 남은 뒷시간에 더 많은 회의를 진행 할 수 있기 때문에
# 1. 끝나는 시간이 제일 빠른 것이 일단 start회의(curr회의)이다. cnt=1
# 2. 그리고 curr회의의 끝나는 시간보다 같거나 큰 것 중에서 끝나는 시간이 제일 빠른 회의가 그 다음 회의가 된다. cnt++
# 3. 그런 회의가 없으면 이제 더이상 진행될 수 있는 회의가 없다는 것이므로 print(cnt)하고 끝낸다.
# 이다.

# 이때 '끝나는 시간이 제일 빠른 것'을 계속해서 검사해야하므로
# 위의 그리디 알고리즘에서 말했던 것처럼 '정렬'을 사용한다.

n = int(input())
meeting = []
for i in range(n):
    # meeting[i].start, metting[i].end = map(int, input().split())
    start, end = map(int, input().split())
    # JS를 하다보니 객체형식으로 저장하는데 익숙해졌는데, Python은 tuple형식으로 저렇게 저장 할 수 있다.
    meeting.append((start, end))
    meeting.sort(key=lambda meeting_time: (meeting_time[1], meeting_time[0]))
    # meeting.sor() 는 tuple에서 앞의 자료값(여기선 start)을 기준으로 오름차순 정렬하고,
    #    이게 같을 경우에 뒤의 자료값(여기선 end)를 기준으로 하는데,
    # 나는 end(뒤의 자료값)을 1st 기준으로 삼고, 이게 동일할 경우 start를 2nd 기준값으로 고려하고 싶으므로
    # meeting.sort(key = lambda meeting_time: (meeting_time[1], meeting_time[0]))
    # 해준 것이다.

meeting_cnt = 0
end_time = 0
for s, e in meeting:
    if(s >= end_time):
        end_time = e
        meeting_cnt += 1

print(meeting_cnt)
