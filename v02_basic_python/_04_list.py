# 4. 값 변경과 리스트 조작

colors = ["red", "green", "blue"]  # 리스트
numbers = [1, 2, 3, 4, 5]  # 정수 리스트
mixed = [1, "hello", 3.14, True]  # 다양한 자료형을 포함하는 리스트

print(colors[0])     # 인덱싱
print(colors[1:3])   # 슬라이싱

# 리스트의 인덱싱과 슬라이싱
print(numbers[0])  # 첫 번째 요소 출력 (1)
print(colors[-1])  # 마지막 요소 출력 ("cherry")
print(numbers[1:4])  # 두 번째 요소부터 네 번째 요소까지 출력 ([2, 3, 4])

# 리스트의 요소 변경
numbers[0] = 10  # 첫 번째 요소를 10으로 변경
print(numbers)  # [10, 2, 3, 4, 5]

# 리스트에 요소 추가
numbers.append(6)  # 리스트 끝에 6 추가
print(numbers)  # [10, 2, 3, 4, 5, 6]

numbers.insert(2, 99)  # 인덱스 2 위치에 99 삽입
print(numbers)  # [10, 2, 99, 3, 4, 5, 6]

# 리스트에서 요소 제거
numbers.remove(99)  # 값이 99인 요소 제거
print(numbers)  # [10, 2, 3, 4, 5, 6]

popped_value = numbers.pop()  # 마지막 요소 제거 및 반환
print(popped_value)  # 6
print(numbers)  # [10, 2, 3, 4, 5]

# 리스트의 길이 확인
print(len(numbers))  # 5

# 리스트 정렬
numbers.sort()  # 오름차순 정렬
print(numbers)  # [2, 3, 4, 5, 10]

numbers.reverse()  # 내림차순 정렬 (순서 뒤집기)
print(numbers)  # [10, 5, 4, 3, 2]

# 리스트 요소 포함 여부 확인
print(3 in numbers)  # True (3이 리스트에 포함됨)
print(100 in numbers)  # False (100은 리스트에 없음)

# 리스트 반복문 사용
for fruit in colors:
    print(fruit)  # 각 과일을 출력