# 떡볶이 떡 만들기
# 동빈이네 떡볶이 떡은 길이가 일정하지 않다.
# 절단기에 높이 H를 지정하면 줄지어진 떡을 한번에 절단한다. 
# 높이가 H보다 긴 떡은 H의 윗부분이 잘리고, 낮은 떡은 잘리지 않는다.
# 손님이 요청한 총 길이가 M일 때 적어도 M만큼의 떡을 얻기 위해 절단기에 설정할 수 있는 높이의 최대값을 구하라

import sys

n, m = map(int, sys.stdin.readline().strip().split())
arr = list(map(int, sys.stdin.readline().strip().split()))

start = 0
end = 1000000000

result = 0
while start <= end:
    mid = (start + end) // 2

    total = 0
    for x in arr:
        if x > mid:
            total += x - mid
    
    if total < m:
        end = mid - 1
    else:
        result = mid # 최대한 덜 잘랐을 때가 정답이므로, 여기에서 result에 기록
        start = mid + 1