board = [list(map(int, input().split())) for _ in range(7)]

cnt = 0

for i in range(7):
    for j in range(3):
        fiveSlice1 = board[i][j:j+5]
        if fiveSlice1 == fiveSlice1[::-1]:
            cnt+=1

# for j in range(7):
#     for i in range(3):
#         fiveSlice2 = board[i:i+5][j]
#         if fiveSlice2 == fiveSlice2[::-1]
#             cnt+=1
#syntax error - 열(column)에서는 slice가 되지 않는다. 

for j in range(7):
    for i in range(3):
        for k in range(2):
            if board[i+k][j] != board[i+4-k][j]: 
                break
        else:
            cnt+=1

print(cnt)


