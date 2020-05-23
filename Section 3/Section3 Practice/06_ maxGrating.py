# #격자판 최대합
# # pythonic code point
# # 1. M*N 2차원 격자판을 입력받기 
#     #방법1. arr = [list(map(int, input().split(''))) for _ in range(M)]
#     #이건 입력받는다기보다, 0부터 해당 범위까지의 2차원 격자판 선언하는 경우임
#     #방법2. arr = [[0 for col in range(N)] for row in range(M)]
#     #방법3. arr = [[0]*N]*M]

# #2. 2차원 배열 출력하기
# # for x in arr:
# #     print(x)로 단순하게 출력하면 됨

# # 3. 이중 for문 한 줄로 코딩하기
# for i in v: 
#     for j in i: 
#         print(j)
# -> [j for i in v for j in i] : [j // for i in v //for j in i]

N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

maxi = -999999
for i in range(N):
    rowSum = 0
    colSum = 0
    #for문 하나에 열 한개, 행 한개의 합 구할 수 있음 단 N*N 격자판일 경우에 한함
    for j in range(N):
        rowSum += arr[i][j] 
        colSum += arr[j][i]
    maxi = max(maxi, rowSum, colSum)


for i in range(N):
    crossSum1 = crossSum2 = 0
    crossSum1 += arr[i][i]
    crossSum2 += arr[i][N-i-1]

    maxi = max(maxi, crossSum1, crossSum2)

print(maxi)





