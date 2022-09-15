# 게임 개발
# n * m 크기의 직사각형 의 각각의 칸은 육지 또는 바다다.
# 바다로 되어 있는 공간에는 갈 수 없다.
# 캐릭터의 움직임을 위한 메뉴얼은 다음과 같다.
# 1. 현재 위치에서 현재 방향을 기준으로 왼쪽부터 차례대로 탐색해, 가 보지 않았고 육지인 칸으로 이동한다.
# 2. 네 방향 모두 가본 칸이거나 바다로 된 칸이라면 바라보는 방향 그애로 한 칸 뒤로 가고 1단계로 돌아간다.
#    이 때 뒤쪽 방향이 바다인 칸이라 뒤로 갈 수 없는 경우에는 움직임을 멈춘다.
# 캐릭터가 방문한 칸의 수를 구하라

n, m = map(int, input().split())

# 방문한 위치를 저장하기 위한 맵을 생성해 0으로 초기화
d = [[0] * m for _ in range(n)]

# 시작 좌표, 방향 입력
x, y, direction = map(int, input().split())

# 현재 좌표 방문 처리
d[x][y] = 1

array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 방향 별 움직임 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

count = 1
turn_time = 0
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dx[direction]
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        if array[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0

print(count)