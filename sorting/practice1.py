# 위에서 아래로

# n 개의 수가 입력된다. 내림차순으로 정렬하여 출력하라

n = int(input())
arr = [int(input()) for _ in range(n)]

result = sorted(arr, reverse=True)

for num in result:
    print(num, end=' ')