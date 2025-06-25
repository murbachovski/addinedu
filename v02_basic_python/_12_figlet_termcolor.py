# pyfiglet + termcolor

import pyfiglet
from termcolor import colored

# 1. 폰트 입히기
sentence = pyfiglet.figlet_format("***********")

# 2. 색상 입히기
colored_sentence = colored(sentence, "blue")

# 3. 출력
print(colored_sentence)
