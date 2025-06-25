def meters_to_feet(meters):
    feet = meters * 3.28084 # 1미터는 약 3.28피트
    return feet

# 사용자 입력 받기
user_input = input("미터 값을 입력하세요 :")

# 3. type 변경
# meters = float(user_input)

# 1. 타입 에러 확인 
meters = user_input

# 2. type 확인
# print(type(meters))

feet = meters_to_feet(meters)
print(f"{meters}m는 {feet:.2f}ft입니다.")
