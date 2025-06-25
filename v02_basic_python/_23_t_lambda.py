from pyfiglet import figlet_format
from termcolor import colored

# 함수 이름 : lambda 매개변수 1, 매개변수 2, ... : 매개변수를 이용한 함수의 내용

# def fancy_text(text, color='cyan'):
#     """
#     설명:
#         입력한 텍스트를 아스키 아트 형식으로 바꾸고 색상을 입혀 출력용 문자열을 반환합니다.

#     매개변수:
#         text (str): 출력할 텍스트
#         color (str): 적용할 색상 (기본값 'cyan')

#     반환값:
#         str: 꾸며진 아스키 아트 텍스트
#     """
#     ascii_art = figlet_format(text)
#     colored_art = colored(ascii_art, color)
#     return colored_art

# pyfiglet + termcolor를 한 줄로 처리하는 lambda 함수
fancy_text = lambda text, color='cyan': colored(figlet_format(text), color)

# 사용 예시
print(fancy_text("PYTHON", "green"))
