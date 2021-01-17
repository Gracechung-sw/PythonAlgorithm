def getBinary(num):
  if num == 0:
    return
  else:
    getBinary(num//2)
    print(num%2, end='')

if __name__ == "__main__":
  num = int(input())
  print(getBinary(num))