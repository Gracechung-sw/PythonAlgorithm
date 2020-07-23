arr = [list(map(int, input().split())) for _ in range(9)]


def check(arr):
    for i in range(9):
        rowcnt = [0]*10 #중복된는게 있는지 확인하는 checklist
        colcnt = [0]*10
        for j in range(9):
            rowcnt[arr[i][j]] = 1
            colcnt[arr[j][i]] = 1
        if sum(rowcnt)!=9 or sum(colcnt)!=9:
            return False

    #python range(start, stop, step)
    # for k in range(0, 9, 3):
    #     matrixcnt = [0]*10
    #     for i in range(k, k+3):
    #         for j in range(k, k+3):
    #             matrixcnt[arr[i][j]] = 1
    #         if sum(matrixcnt)!=9:
    #             return False
    #이게 왜 안되는거지 => 이렇게 하면 대각선 3x3 matrix만 돌게 되니까

    for i in range(3):
        for j in range(3):
            matrixcnt=[0]*10
            for k in range(3):
                for s in range(3):
                    matrixcnt[arr[i*3+k][j*3+s]]=1
            if sum(matrixcnt)!=9:
                return False

    return True

if check(arr):
    print("YES")
else:
    print("NO")