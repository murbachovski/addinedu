# 4. 값 변경과 리스트 조작

mixed = [1, "hello", 3.14, True]  # 다양한 자료형을 포함하는 리스트

# 리스트 반복문 사용
for i in mixed:
    print(i)  # 각 과일을 출력

for index, value in enumerate(mixed):
    print(index, value)