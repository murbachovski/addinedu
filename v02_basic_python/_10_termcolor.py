from termcolor import colored
# https://pypi.org/project/termcolor/

# 1. 기본 색상 출력
print(colored("Hello, Red!", "red"))
print(colored("Hello, Green!", "green"))
print(colored("Hello, Blue!", "blue"))

# 2. 배경색 지정 (on_color)
print(colored("Hello with Yellow Background", "grey", "on_yellow"))

# 3. 텍스트 스타일 지정(attrs)
print(colored("Bold Text", "white", attrs=["bold"]))
print(colored("Underlined Text", "cyan", attrs=["underline"]))
print(colored("Reverse Color Text", "magenta", attrs=["reverse"]))

# 4. 여러 스타일 동시에 적용 가능
print(colored("Bold, Underlined and Red", "red", attrs=["bold", "underline"]))