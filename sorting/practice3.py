# 두 배열의 원소 교체
# 두 배열 A와 B가 주어진다.
# 최대 K번 배열 A의 원소와 배열 B의 원소를 바꿀 수 있다.
# 배열 A의 모든 원소의 합이 최대가 되도록 하라

n, k = map(int, input().split())

array_a = list(map(int, input().split()))
array_a.sort()
array_b = list(map(int, input().split()))
array_b.sort(reverse=True)

for i in range(k):
    if array_a[i] >= array_b[i]:
        break

    array_a[i], array_b[i] = array_b[i], array_a[i]

print(sum(array_a))