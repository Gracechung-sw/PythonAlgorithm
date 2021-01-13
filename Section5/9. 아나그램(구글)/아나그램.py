# str1_dict = {'A':2, 'a': 1, 'b':1, 'e':2}
# str2_dict = {'A':2, 'b':1, 'e':2}

# print(str1_dict==str2_dict)

str1 = input()
str2 = input()

str1_dict = dict()

for i in str1:
  str1_dict[i] = str1_dict.get(i, 0)+1 

for i in str2:
  str1_dict[i] = str1_dict.get(i, 0)-1 


for cnt in str1_dict:
  if str1_dict.get(cnt) >=1:
    print("NO")
    break
else:
  print("YES")
    
    