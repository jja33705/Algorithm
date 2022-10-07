array = [5, 7, 9, 0, 3, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    # 배열의 길이가 1이 되면 종료
    if start >= end:
        return
    
    # 맨 앞의 원소를 피봇으로 삼는다.
    pivot = start
    left = start + 1
    right = end

    # 왼쪽에서 피봇보다 큰 값과 오른쪽에서 피봇보다 작은 값을 서로 교차되기 전까지 계속 바꿔준다.
    while left <= right:

        # 왼쪽부터 피봇보다 큰 값을 찾는다.
        while left <= end and array[left] <= array[pivot]:
            left += 1
        
        # 오른쪽에서 피봇보다 작은 값을 찾는다.
        while right > start and array[right] >= array[pivot]:
            right -= 1
        
        # 만약 위에서 찾은 두 값이 교차되었으면 피봇과 작은 값을 교환
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        else: # 교차되지 않았으면 두 값을 교환
            array[left], array[right] = array[right], array[left]

    # 피봇은 정렬된 것으로 보고, 피봇 왼쪽, 오른쪽으로 똑같이 수행
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)

quick_sort(array, 0, len(array) - 1)
print(array)