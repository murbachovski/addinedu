import pyfiglet

# 함수화
def good_sentence(sen):
    '''
    함수 설명:
        입력된 문자열을 pyfiglet을 이용해 아스키 아트 형태로 변환합니다.

    매개변수(Parameter):
        sen (str): 출력할 문자열
    '''
    good_sen = pyfiglet.figlet_format(sen)
    print(good_sen)
    
good_sentence("Hello!!!")

# 함수 설명 보기
# help(good_sentence)