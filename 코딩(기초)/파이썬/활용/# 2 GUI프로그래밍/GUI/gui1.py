# 비고
'''
변수 = input("질문")이면 사용자가 입력한 값이된다.
프로그램 기초 사용 권장 툴입니다.
중요한 단위는 소수말고 정수로(나중에 보이는것만 소수로 하든지.)
'''

# 주 내용
from tkinter import * # 티킨터 프로그램 불러오기.
import os
창 = Tk() # T는 대문자, k는 소문자
창.title("이미지 합성기(제작ing)") # 제목
창.geometry("480x760+100+10") # (여기서는 엑스x로 사용) 가로 * 세로 + x좌표 + y좌표
창.resizable(False, True) # x(넓이), y(높이) / False = 조정 불가 처리

버튼_테스트용1 = Button(창, text= "테스트용1 나중에 바꾸세요!") # 버튼 생성 (Tk지정한 변수이름), text= 입력할 텍스트
버튼_테스트용1.pack()
버튼_테스트용2 = Button(창, padx= 30, pady= 10, text= "테스트용2 바꾸세요!") # padx= 가로크기 "여백", pady= 세로크기 "여백"
버튼_테스트용2.pack()
버튼_테스트용3 = Button(창, padx= 20, pady= 30, text= "테스트용3 나중에 바꾸세요!") # 단, 텍스트가 길면 가로크기를 넘을수있다.
버튼_테스트용3.pack()
버튼_테스트용4 = Button(창, width= 10, height= 4, text= "테스트용4 (넘을 수 있다)") # width= 가로크기 '지정', heirht= 세로크기 '지정'
버튼_테스트용4.pack()
버튼_테스트용5 = Button(창, fg= "green", bg= "black", text= "테스트용5") # fg= 글자색 지정, bg= 바탕색 지정
버튼_테스트용5.pack()

이미지_폴더_위치 = os.path.dirname(__file__)
이미지_위치 = os.path.join(이미지_폴더_위치, "# 2 GUI프로그래밍")
머찐버튼 = PhotoImage(os.path.join(이미지_위치, "머찐버튼.png")) # PhotoImage(file = "파일위치/이미지이름.png")
버튼_테스트용6 = Button(창, image= 머찐버튼) # image= 이미지를 저장한 변수이름
버튼_테스트용6.pack()

놀라운변화 = 1
def 놀라운_동작7():
    print("놀랍다!")

    global 놀라운변화
    놀라운변화 += 1
    if 놀라운변화 == 2:
        레이블1.config(text= "평범한 변화", fg= "black") # 레이블변수이름.config(레이블에 변화줄 내용)
    elif 놀라운변화 == 6:
        레이블1.config(text= "놀라운 변화", fg= "green")
    elif 놀라운변화 == 7:
        레이블1.config(text= "더 놀라운 변화")
    elif 놀라운변화 == 8:
        레이블1.config(text= "엄청나게 놀라운 변화", fg= "blue")
    elif 놀라운변화 == 9:
        레이블1.config(text= "뛰어난 놀라운 변화")
    elif 10 <= 놀라운변화 <= 15:
        레이블1.config(text= "전설적인 놀라운 변화", fg= "yellow")
    elif 16 <= 놀라운변화 <= 20:
        레이블1.config(text= "신화적인 변화", fg= "red")
    elif 놀라운변화 > 20:
        레이블1.config(text= "평범해지는 변화", fg= "dark red")
        놀라운변화 = 1

버튼_테스트용7 = Button(창, fg = "black", bg = "green", text= "놀라운 버튼", command= 놀라운_동작7) # command= 함수(딴것도 괜찮지만)
버튼_테스트용7.pack()

레이블1 = Label(창, text= "위는 테스트용 버튼들") # 레이블변수이름 = Ladel(버튼과 동일)
레이블1.pack()

텍스트1 = Text(창)
텍스트1.pack()
텍스트1.insert(END, "글을 입력하세요") # 처음에 나오는 텍스트지정

엔트리1 = Entry(창, width= 38)
엔트리1.pack()
엔트리1.insert(0, "한 문장을 입력하세요") # 엔트리는 1줄만(엔터X) 텍스트는 여러줄(엔터O)

def 불러오기():
    print(텍스트1.get("1.0", END)) # "1.0"에서 1은 첫번째줄, 0은 0번째 글자다. // 그리고 get은 "1.0"불러온다.
    print(엔트리1.get())

버튼_테스트용8 = Button(창, text= "텍스트 불러오기", command= 불러오기)
버튼_테스트용8.pack()

def 삭제():
    텍스트1.delete("1.0", END)
    엔트리1.delete(0, END) # delete는 삭제 명령어이고 (0, END)는 0부터 끝까지 라는 뜻

버튼_테스트용9 = Button(창, fg = "white", bg = "black", text= "텍스트 삭제", command= 삭제)
버튼_테스트용9.pack()

창.mainloop() # 창이 사라지지않는 역활


# 총평 / 세부 / 추가 내용
'''
-----총평-----
아직 아무것도 못한상태

-----추가할 내용-----
계속 배우도록

-----세부-----
없음

-----1차 추가 내용-----
버튼 7가지

-----n차 추가 내용-----
레이블추가
버튼누른 횟수마다 레이블변화

-----n차 추가 내용-----


-----마지막 추가 내용-----
내용 없음
'''