import 기초11자료 # 으로 불러올수있다.
기초11자료.아침_일반_티켓(3)
기초11자료.아침_어린이_티켓(1)
기초11자료.아침_군인_티켓(4)
기초11자료.아침_회원_티켓(14)
기초11자료.일반_티켓(2)
기초11자료.어린이_티켓(3)
기초11자료.군인_티켓(3)
기초11자료.이벤트_티켓(4)
기초11자료.회원_티켓(5)
print("")

import 기초11자료 as 티켓 # 형식으로 줄일수있다.
티켓.아침_일반_티켓(3)
티켓.아침_어린이_티켓(1)
티켓.아침_군인_티켓(4)
티켓.아침_회원_티켓(14)
티켓.일반_티켓(2)
티켓.어린이_티켓(3)
티켓.군인_티켓(3)
티켓.이벤트_티켓(4)
티켓.회원_티켓(5)
print("")

from 기초11자료 import * # 으로 앞에 안붙이고 함수를 사용 할수있다.
아침_일반_티켓(3)
아침_어린이_티켓(1)
아침_군인_티켓(4)
아침_회원_티켓(14)
일반_티켓(2)
어린이_티켓(3)
군인_티켓(3)
이벤트_티켓(4)
회원_티켓(5)
print("")

from 기초11자료 import 일반_티켓, 어린이_티켓, \
    군인_티켓, 이벤트_티켓, 회원_티켓 # 으로 원하는 함수만 불러와 사용 할수있다.
일반_티켓(2)
어린이_티켓(3)
군인_티켓(3)
이벤트_티켓(4)
회원_티켓(5)

from 기초11자료 import 회원_티켓 as vip # 으로 원하는 함수를 줄여서 사용 할수있다.
vip(5)

import 기초11.기초11자료2 # 단, 바로 클래스를 불러올수없다.
import 기초11.기초11자료3
영화관1 = 기초11.기초11자료2.CGM(4)
영화관2 = 기초11.기초11자료3.오메가박스(32)
영화관1.이벤트_티켓()
영화관2.아침_골든_회원_티켓()

from 기초11.기초11자료3 import * # 이런식으로도 불러오기가능
영화관2 = 기초11.기초11자료3.오메가박스(32)
영화관2.아침_골든_회원_티켓()
# __init__ 파일에서 이름을 허용해야 사용가능
import inspect
import 기초11자료
print(inspect.getfile(기초11자료)) # 이렇게 해서 모듈또는 패키지 자료위치를 알수있다.
#                     패키지설치방법
# pypi를 검색해서 들어가면 다양한 패키지들이 나온다.
# 복사칸에서 복사한뒤 "터미널"에 붙여넣고 그 코드를 복사 붙여넣기를 한다.
# 업그레이드가 필요할때 pip install --upgrade 그패키지이름
# 삭제하고 싶을때 pip uninstall 그패키지이름 삭제할건지 묻는데 y/n 으로 의사표현가능
import random
print(dir()) # dir은 이 프로젝트에서 사용중인 함수가 나오며
print(dir(random)) # dir(함수)로 그 함수의 코드들을 볼수있다. (lst, name)등등
# list of python builtins을 검색해 들어가 내장함수들을 볼수있다.
# list of python modules에 들어가 외장함수들을 볼수있다
import os # 기본기능 (폴더삭제, 폴더생성)
print(os.getcwd())
폴더 = "기초11파일"
if os.path.exists(폴더):
    print("이미 폴더가 존재합니다.")
    질문 = input("폴더를 삭제 하시겠습니까? (y/n)")
    if 질문 == "y":
        os.rmdir(폴더) # 폴더 삭제
        print(폴더, "폴더를 삭제했습니다.")
else:
    os.makedirs(폴더) # 폴더 생성
    print(폴더, "폴더를 생성합니다.")
import time # 시간관련 함수
print(time.localtime()) # 현재 시간 출력
print(time.strftime("%Y년 %m월 %d일 %H시 %M분 %S초")) # 깔끔하게 시간출력(대소문자 확실하게 구분)
import datetime # 시간함수보다 간단하게 시간 표현가능
print("오늘 날짜는", datetime.date.today())
오늘날짜 = datetime.date.today() # 오늘날짜 저장
오날 = datetime.timedelta(days=365) # 365일저장
print("이 코드 작성일 365일후 :", 오늘날짜 + 오날) # 오늘로부터 365일후