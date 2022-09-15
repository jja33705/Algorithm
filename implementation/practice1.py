# 왕실의 나이트

# 8 X 8 크기의 좌표 평면 위의 특정한 칸에 나이트가 있다.
# 나이트가 이동할 수 있는 경우의 수를 구하라

input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

# 나이트가 이동할 수 있는 8개의 경우의 수 정의
steps = [(-2, 1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

# 각 경우의 수로 이동했을 때 좌표 위에 있는지 확인
result = 0

for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)