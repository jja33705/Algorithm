# 부품 찾기
# 동빈이네 전자 매장에는 N개의 부품이 있다.
# 동빈이네 전자 매장에 M개의 부품이 모두 있는지 확인하는 프로그램을 작성하라.

import sys

def binary_search(arr, value, start, end):
    if start > end:
        return False
    
    mid = (start + end) // 2

    if arr[mid] == value:
        return True
    elif arr[mid] > value:
        return binary_search(arr, value, start, mid - 1)
    else:
        return binary_search(arr, value, mid + 1, end)

n = int(sys.stdin.readline().strip())
arr_n = list(map(int, sys.stdin.readline().strip().split()))
arr_n.sort()

m = int(sys.stdin.readline().strip())
arr_m = list(map(int, sys.stdin.readline().strip().split()))

for num in arr_m:
    result = binary_search(arr_n, num, 0, len(arr_n) - 1)
    
    if result:
        print('yes')
    else:
        print('no')