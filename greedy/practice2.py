# 숫자 카드 게임
# 숫자가 쓰인 카드들이 n * m형태로 놓여 있다. (n = 행의 개수, m = 열의 개수)
# 먼저 뽑고자 하는 카드가 포함돼 있는 행을 선택한다.
# 그다음 선택되 행에서 가장 숫자가 낮은 카드를 뽑아야 한다.
# 처음에 행을 고른 후, 그 행에서 가장 숫자가 낮은 카드를 뽑아야 한다는 점을 고여하여 최종적으로 가장 높은 숫자의 카드를 뽑아라.
n, m = map(int, input().split())

result = 0

#결국은 각 행에서 최소값을 구하고, 그 최소값들 중에서 최대값이 답이다.
for _ in range(n):
    data = list(map(int, input().split()))
    
    min_value = min(data)

    result = max(result, min_value)

print(result)