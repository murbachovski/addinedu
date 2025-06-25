# 클래스 정의
class Animal:
    # 생성자
    def __init__(self, name):
        # 속성
        self.name = name
    # 메서드
    def hello(self):
        print(f"안녕하세요. 저는 {self.name} 입니다.")
        
# 객체 생성
dog = Animal("뽀삐")

# 메서드 호출
dog.hello()