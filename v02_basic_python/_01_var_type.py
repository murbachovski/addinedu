# 1. 기본적인 변수 살펴보기
    # - 변수들이 이렇게 생겼구나~

# 변수 목록
x = 10  # 정수형 변수
y = 3.14  # 실수형 변수
name = "Python"  # 문자열 변수
is_python_fun = True  # 불리언 변수
colors = ["red", "green", "blue"]  # 리스트
coords = (10, 20)  # 튜플
person = {"name": "Tom", "age": 30}  # 딕셔너리
unique_values = {1, 2, 3}  # 집합
nothing = None  # NoneType

# 출력
print(x)
print(y)
print(name)
print(is_python_fun)

# 타입 출력
print(type(x))  # <class 'int'>
print(type(y))  # <class 'float'>
print(type(name))  # <class 'str'>
print(type(is_python_fun))  # <class 'bool'>
print(type(colors))       # <class 'list'>
print(type(coords))       # <class 'tuple'>
print(type(person))       # <class 'dict'>
print(type(unique_values))# <class 'set'>
print(type(nothing))      # <class 'NoneType'>

# 변수가 특정 유형인지 확인
print(isinstance(nothing, type(dict)))      # <class 'NoneType'>
