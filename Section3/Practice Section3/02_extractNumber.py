String = input()
result = 0

#숫자형태의 문자 이어붙여서 숫자만들기
for s in String:
    if s.isdecimal():
        result = result * 10 + int(s)
print(result)

#약수개수 구하기
num = 0
for i in range(1, result+1):
    if result%i == 0:
        num += 1
print(num)



