# 1이 될 때까지
# 어떤 수 n을 1을 빼거나, k로 나누는 두개의 연산만을 이용해 1로 만드려고 한다.
# 최소 횟수를 구하라

n, k = map(int, input().split())

result = 0

# 1을 빼다가 k로 나누어질 때는 k로 나누는 작업을 반복하면 된다.
while True:
    # k로 나누어지는 숫자로 만든다.
    target = (n // k) * k
    result += n - target
    n = target

    # k보다 작아졌을때는 반복문을 빠져나온다.
    if n < k:
        break

    # k로 나눠줌
    n //= k
    result += 1

# 나머지 k로 나눌 수 없는 숫자들을 빼준다.
result += n - 1

print(result)