n, m = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()
start = 0
end = n-1

def BinarySearch(start, end, m):
    mid = (start+end)//2

    if arr[mid] > m:
        return BinarySearch(start, mid-1, m)

    elif arr[mid] == m:
        return mid
    
    else:
        return BinarySearch(mid+1, end, m)

print(BinarySearch(start, end, m)+1)


##비재귀방법
# while start <= end:
#     mid = (start+end)//2

#     if arr[mid] > m:
#         end = mid-1
        
#     elif arr[mid] == m:
#         print(mid+1)
#         break
    
#     else:
#         start = mid+1
