n = int(input())
word_dict = {}

# 노트에 적은 단어를 입력시마다 0으로 dict에 input
for i in range(n):
  key = input()
  word_dict[key] = 0

# 시에 쓰인 단어를 입력시ㅣ마다 1로 수정(사용했다는 의미)
for i in range(n-1):
  used_key = input()
  word_dict[used_key] = 1

# 이제 word_dict에서 value가 여전히 0인(사용되지 않은) key인 단어를 출력
for k, v in word_dict.items():
  if v == 0:
    print(k)
    break

# not_used = [k for k, v in word_dict.items() if v==0]
# print(not_used[0])
