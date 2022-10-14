# 성적이 낮은 순서로 학생 출력하기
# 이름과 학생으로 구분된 성적이 입력된다. 성적이 낮은 순서대로 학생의 이름을 출력하라.

n = int(input())

array = []

for _ in range(n):
    input_data = input().split()

    array.append((input_data[0], int(input_data[1])))

array = sorted(array, key= lambda student: student[1])

for student in array:
    print(student[0], end=' ')