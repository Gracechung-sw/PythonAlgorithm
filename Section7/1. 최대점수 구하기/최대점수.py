def DFS(inx, score, time):
  global result
  #기저 조건
  # 문제를 다 풀었을 때 또는 시간이 다 되었을 때
  if time > m: #시간이 넘었을 때 score는 최종 점수로 볼 수 없으니까 그냥 return
    return
  if inx >= n: #시간이 아직 남았는데 문제를 풀던지 안 풀던지 해서 다 훑어보았을 때는 그 때 가진 점수가 최대 점수인지 확인
    result = max(result, score)
    return

  else:
    DFS(inx+1, score+list[inx][0], time+list[inx][1]) #현재 문제를 풀고, 다음으로 넘어감
    DFS(inx+1, score, time)#현재 문제를 풀지 않고, 다음으로 넘어감 

if __name__ == "__main__":
  n, m = map(int, input().split())
  list = [list(map(int, input().split())) for _ in range(n)]
  result = -1
  DFS(0, 0, 0) #inx, score, time
  print(result)
