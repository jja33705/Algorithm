# 1로 만들기
# 정수 X가 주어질 때 정수 X에 사용할 수 있는 연산은 다음과 같은 4가지이다.
# 1. X가 5로 나누어떨어지면 5로 나눈다.
# 2. X가 3으로 나누어떨어지면 3으로 나눈다.
# 3. X가 2로 나누어떨어지면 2로 나눈다.
# 4. X에서 1을 뺸다.
# 정수 X가 주어졌을 때 연산 4개를 최소 횟수로 사용해 1을 만들려고 한다.

x = int(input())

d = [0] * 30001

for i in range(2, x + 1):
    d[i] = d[i - 1] + 1

    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)
    
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)
    
    if i % 5 == 0:
        d[i] = min(d[i], d[i // 5] + 1)

print(d[x])