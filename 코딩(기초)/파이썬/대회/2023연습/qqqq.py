입력값 = input()

값1 = 0
값2 = 1
글자수 = (len(입력값))
정리 = []
제동 = False

while 글자수 != 0:
    정리.append(입력값[값1 : 값2])
    값1 += 1
    값2 += 1
    글자수 -= 1
# print(정리)

글자수 = (len(입력값))
실행 = 정리
i = -1
ii = 0
다른값 = False
실행횟수 = 0
완판 = True
타값 = 0

def 연산():
    global 실행
    global 위치1값
    global 위치2값
    global i
    global 실행횟수

    위치1값 = 실행[i]
    위치2값 = 실행[i + 1]
    실행[i] = 위치2값
    실행[i + 1] = 위치1값
    실행횟수 += 1

try:
    while i != 글자수:
        i += 1
        위치1 = 실행[i]
        위치2 = 실행[i + 1]
        if 위치1 == "0" or 위치1 == "2" or 위치1 == "4" or 위치1 == "6" or 위치1 == "8":
            위치1 = "짝수"
        else:
            위치1 = "홀수"

        if 위치2 == "0" or 위치2 == "2" or 위치2 == "4" or 위치2 == "6" or 위치2 == "8":
            위치2 = "짝수"
        else:
            위치2 = "홀수"
        
        if 제동 == False:
            if 위치1 == "홀수":
                판단 = "홀수"
            else:
                판단 = "짝수"
            제동 = True

        if 위치1 == 위치2:
            pass
        else:
            if 판단 == "홀수":
                if 위치1 == "홀수":
                    continue
                else:
                    연산()
            else:
                if 위치1 == "홀수":
                    연산()
                else:
                    continue
            i = -1
            print(실행)
except:
    print(실행횟수)