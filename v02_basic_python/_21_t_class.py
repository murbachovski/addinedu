# 클래스: 동물(Animal)에 대한 설계도 정의
class Animal:  # 클래스 정의
    
    # 생성자: 객체가 생성될 때 자동으로 호출됨
    def __init__(self, name, age, weight, city):
        '''
        Animal Class
        '''
        # self: 인스턴스 자기 자신을 가리킴
        # name: 생성 시 전달받은 이름을 self.name이라는 속성에 저장
        self.name = name  # 속성(변수), 인스턴스가 가지고 있는 데이터
        self.age = age
        self.weight = weight
        self.city = city
        
    # 메서드: 객체가 사용할 수 있는 함수
    def hello(self):  
        # 메서드 안에서 self를 통해 속성에 접근
        print(f"나는 {self.name}, 내 나이는 {self.age}, 내 몸무게는 {self.weight}, 사는 곳은 {self.city}")  # f-string을 이용한 출력
        
dog = Animal("강아지", 7, 25, "Seoul")
dog.hello()

wolf = Animal("늑대", 30, 80, "Busan")
wolf.hello()

cat = Animal("고양이", 3, 12, "USA")
cat.hello()
