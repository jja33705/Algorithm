# 계수정렬
# 정렬하고자 하는 데이터가 모두 양의 정수고, 최소값과 최대값의 차이가 적을 때 굉장히 빠르게 동작한다.

array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

# 가장 큰 수의 계수까지 담을 수 있는 크기의 리스트를 만들어 준다
table = [0] * (max(array) + 1)

# 각 수가 몇번 등장했는지를 기록한다.
for n in array:
    table[n] += 1

# 각 수가 등장한 수만큼 출력해 준다.
for i in range(len(table)):
    for _ in range(table[i]):
        print(i, end=' ')