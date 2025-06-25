# termcolor를 활용한 함수를 만들어 보세요.

from termcolor import colored

def print_styled_text(text, color="blue"):
    """
    주어진 텍스트를 figlet 폰트로 꾸미고 색상을 입혀 출력합니다.

    Parameters:
        text (str): 출력할 텍스트
        color (str): 색상 (기본값: "blue")
    """
    colored_text = colored(text, color)
    print(colored_text)

# 사용 예시
print_styled_text("Hello, World!", color="green")
