import pyfiglet
from termcolor import colored

def decorate_text(text, color="blue"):
    '''
    설명:
        입력한 텍스트에 아스키 아트 폰트를 적용하고, 색상을 입혀 출력하는 함수입니다.

    매개변수:
        text (str): 꾸밀 텍스트
        color (str): 적용할 색상 (기본값은 'blue')
        font (str): 사용할 pyfiglet 폰트 (기본값은 'standard')

    반환값:
        str: 꾸며진 텍스트 (색상 + 아스키 아트)
    '''
    ascii_art = pyfiglet.figlet_format(text)
    colored_art = colored(ascii_art, color)
    print(colored_art)

# 사용 예시
decorate_text("Python!", color="green")
