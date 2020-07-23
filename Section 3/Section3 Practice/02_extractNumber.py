String = input()
result = 0

for s in String:
    if s.isdecimal():
        result = result * 10 + int(s)

print(result)

num = 0
for i in range(1, result+1):
    if result % i == 0:
        num += 1

print(num)
