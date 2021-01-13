# 창고에 상자가 가로방향으로 일렬로 쌓여 있습니다.
# 만약 가로의 길이가 7이라면
# 1열은 높이가 6으로 6개의 상자가 쌓여 있고, 2열은 3개의 상자, 3열은 9개의 상자가 쌓여 있
# 으며 높이는 9라고 읽는다.
# 창고 높이 조정은 가장 높은 곳에 상자를 가장 낮은 곳으로 이동하는 것을 말한다.
# 가장 높은 곳이나 가장 낮은 곳이 여러곳이면 그 중 아무거나 선택하면 된다.
# 위에 그림을 1회 높이 조정을 하면 다음과 같아진다.
# 창고의 가로 길이와 각 열의 상자 높이가 주어집니다. m회의 높이 조정을 한 후 가장 높은 곳
# 과 가장 낮은 곳의 차이를 출력하는 프로그램을 작성하세요.
# ▣ 입력설명
# 첫 번째 줄에 창고 가로의 길이인 자연수 L(1<=L<=100)이 주어집니다.
# 두 번째 줄에 L개의 자연수가 공백을 사이에 두고 입력됩니다. 각 자연수는 100을 넘지
# 않습니다
# 세 번째 줄에 높이 조정 횟수인 M(1<=M<=1,000)이 주어집니다.
# ▣ 출력설명
# M회의 높이 조정을 마친 후 가장 높은곳과 가장 낮은 곳의 차이를 출력하세요.

# 1. L입력받기
# 2. height 입력받기 height = list(map(int, input().split()))
# 3. m입력 받기
# 4. 내림차숝 정렬
# 5. for m번 반복
# 5-1. max height인 height[0] -= 1
# 5-2. min height인 height[L-1] += 1
# 5-3. height[0]가 여전히 max height인지 검사 아니면 자리 바꾸기
# 5-4. height[L-1]가 여전히  min height인지 검사 아니면 자리 바꾸기

L = int(input())
height = list(map(int, input().split()))
m = int(input())

height.sort(reverse=True)

# for _ in range(m):
#     height[0] -= 1
#     height[L-1] += 1
#     if(height[0] < height[1]):
#         temp = height[0]
#         height[0] = height[1]
#         height[1] = temp
#     if(height[L-1] > height[L-2]):
#         temp = height[L-1]
#         height[L-1] = height[L-2]
#         height[L-2] = temp

# print(height[0]-height[L-1])
# 이렇게 하면 반례가 생긴다.height[0] -= 1 된 것이 height[2]보다, height[3]보다.. 작을 수있기 때문이다. (height[1]~height[어디까지] 같은 값일 수도 있으니까)
# 그래서 아래와 같은 방법이어야 한다.


# 1. L입력받기
# 2. height 입력받기 height = list(map(int, input().split()))
# 3. m입력 받기
# 4. 내림차숝 정렬
# 5. for m번 반복
# 5-1. max height인 height[0] -= 1
# 5-2. min height인 height[L-1] += 1
# 5-3. 다시 sorting

for _ in range(m):
    height[0] -= 1
    height[L-1] += 1
    height.sort(reverse=True)

print(height[0]-height[L-1])
