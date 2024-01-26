from random import *
# from _typeshed import self
class 유닛:
    def __init__(self, 이름, 체력, 공격력, 방어력, 속도):
        self.이름 = 이름
        self.체력 = 체력
        self.공격력 = 공격력
        self.방어력 = 방어력
        self.속도 = 속도
        
    def 공격받음(self, 데미지):
        데미지 = 데미지 - (self.방어력 * 2)
        self.체력 -= 데미지
        if self.체력 <= 0:
            print("{0}:파괴 되었습니다.\n".format(self.이름))
        else:
            print("{0}:{1}데미지를 받았습니다.".format(self.이름, 데미지))
            print("남은체력:{0}\n".format(self.체력))

    def 이동(self, 방향):
        print("{0}:{1}방향으로 {2}속도만큼 이동합니다.\n".format(self.이름, 방향, self.속도))

class 공격유닛(유닛): # 표준 유닛(일반) 체력:100 공격력:10 방어력:2 속도:2
    def __init__(self, 이름, 체력, 공격력, 방어력, 속도):
        유닛.__init__(self, 이름, 체력, 공격력, 방어력, 속도)
    
    def 공격(self, 방향):
     print("{0}:{1}의 공격력으로 {2}방향 공격합니다.\n".format(self.이름, self.공격력, 방향))

class 비행유닛(유닛):
    def __init__(self, 이름, 체력, 공격력, 방어력, 속도):
        유닛.__init__(self, 이름, 체력, 공격력, 방어력, 속도)

    def 이동(self, 방향):
        if 방향 == "북서" and 방향 == "북" and 방향 == "북동" and 방향 == "동" and 방향 == "남동" and\
            방향 == "남" and 방향 == "남서" and 방향 == "서":
            print("{0}:{1}방향으로 {2}비행 속도만큼 날아갑니다.".format(self.이름, 방향, self.속도))
        else:
            print("방향에 오류가 있습니다. (북서, 북, 북동, 동, 남동, 남, 남서, 서)으로 입력해주세요.")

class 비행공격유닛(비행유닛, 공격유닛):
    def __init__(self, 이름, 체력, 공격력, 방어력, 속도):
        비행유닛.__init__(self, 이름, 체력, 공격력, 방어력, 속도)
        공격유닛.__init__(self, 이름, 체력, 공격력, 방어력, 속도)

class 강제징집병(공격유닛):
    def __init__(self):
        print("강제징집병이 생성되었습니다.")
        공격유닛.__init__(self, "강제징집병", 60, 5, 1, 1)

class 경비병(공격유닛):
    def __init__(self):
        print("경비병이 생성되었습니다.")
        공격유닛.__init__(self, "경비병", 80, 8, 2, 2)

class 훈련병(공격유닛):
    def __init__(self):
        print("훈련병이 생성되었습니다.")
        공격유닛.__init__(self, "훈련병", 75, 11, 2, 2)

class 궁병(공격유닛):
    def __init__(self):
        print("궁병이 생성되었습니다.")
        공격유닛.__init__(self, "궁병", 50, 15, 1, 4)

class 수습기사(공격유닛): # 표준 유닛(고급) 체력:400 공격력:40 방어력:6 속도:3
    def __init__(self):
        print("수습기사가 생성되었습니다.")
        공격유닛.__init__(self, "수습기사", 310, 30, 5, 3)

class 견습기사(공격유닛):
    def __init__(self):
        print("견습기사가 생성되었습니다.")
        공격유닛.__init__(self, "견습기사", 370, 40, 6, 3)

class 최하급기사(공격유닛): # 표준 유닛(희귀) 체력:600 공격력:80 방어력:17 속도:6
    def __init__(self):
        print("최하급기사가 생성되었습니다.")
        공격유닛.__init__(self, "최하급기사", 480, 50, 9, 5)
        self.장비착용 = False

    def 장비(self):
        if self.장비착용 == False:
            print("{0}:장비를 착용합니다.\n".format(self.이름))
            self.장비착용 = True
            self.공격력 += 20
            self.방어력 += 3
            self.속도 -= 2
        else:
            print("{0}:장비를 해제합니다\n".format(self.이름))
            self.장비착용 = False
            self.공격력 -= 20
            self.방어력 -= 3
            self.속도 += 2

class 하급기사(공격유닛):
    def __init__(self):
        print("하급기사가 생성되었습니다.")
        공격유닛.__init__(self, "하급기사", 540, 60, 10, 6)
        self.장비착용 = False
        self.살기 = False

    def 장비(self):
        if self.장비착용 == False:
            print("{0}:장비를 착용합니다\n".format(self.이름))
            self.장비착용 = True
            self.공격력 += 30
            self.방어력 += 5
            self.속도 -= 3
        else:
            print("{0}:장비를 해제합니다\n".format(self.이름))
            self.장비착용 = False
            self.공격력 -= 30
            self.방어력 -= 5
            self.속도 += 3
    
    def 살기방출(self):
        if self.장비착용 == False:
            print("{0}:장비를 착용해야합니다\n".format(self.이름))
        else:
            if self.살기 == False:
                print("{0}:살기를 내보내기 시작했습니다\n".format(self.이름))
                self.살기 = True
                self.공격력 += 10
                self.방어력 += 1
                self.속도 -= 2
            else:
                print("{0}:살기를 그만 내보내기 시작했습니다\n".format(self.이름))
                self.살기 = False
                self.공격력 -= 10
                self.방어력 -= 1
                self.속도 += 2

def 시작():
    print("게임을 시작합니다.\n")
def 끝():
    print("게임이 종료되었습니다.\n")

시작()
강제징집병1 = 강제징집병()
강제징집병2 = 강제징집병()
경비병1 = 경비병()
경비병2 = 경비병()
훈련병1 = 훈련병()
훈련병2 = 훈련병()
궁병1 = 궁병()
궁병2 = 궁병()
수습기사1 = 수습기사()
수습기사2 = 수습기사()
견습기사1 = 견습기사()
견습기사2 = 견습기사()
견습기사3 = 견습기사()
견습기사4 = 견습기사()
최하급기사1 = 최하급기사()
최하급기사2 = 최하급기사()
하급기사1 = 하급기사()
하급기사2 = 하급기사()
하급기사3 = 하급기사()
하급기사4 = 하급기사()
하급기사5 = 하급기사()
하급기사6 = 하급기사()

공격유닛정리 = []
공격유닛정리.append(강제징집병1)
공격유닛정리.append(강제징집병2)
공격유닛정리.append(경비병1)
공격유닛정리.append(경비병2)
공격유닛정리.append(훈련병1)
공격유닛정리.append(훈련병2)
공격유닛정리.append(궁병1)
공격유닛정리.append(궁병2)
공격유닛정리.append(수습기사1)
공격유닛정리.append(수습기사2)
공격유닛정리.append(견습기사1)
공격유닛정리.append(견습기사2)
공격유닛정리.append(견습기사3)
공격유닛정리.append(견습기사4)
공격유닛정리.append(최하급기사1)
공격유닛정리.append(최하급기사2)
공격유닛정리.append(하급기사1)
공격유닛정리.append(하급기사2)
공격유닛정리.append(하급기사3)
공격유닛정리.append(하급기사4)
공격유닛정리.append(하급기사5)
공격유닛정리.append(하급기사6)

for 유닛 in 공격유닛정리:
    유닛.이동("남동")

for 유닛 in 공격유닛정리:
    유닛.공격("북동")

for 유닛 in 공격유닛정리:
    유닛.공격받음(randint(50, 100))

for 유닛 in 공격유닛정리:
    if isinstance(유닛, 최하급기사): # isinstance 로 무엇인지 확인 할수있다.
        유닛.장비()
    elif isinstance(유닛, 하급기사):
        유닛.장비()
        유닛.살기방출()

for 유닛 in 공격유닛정리:
    유닛.공격("북서")

for 유닛 in 공격유닛정리:
    유닛.공격받음(randint(450, 470))

끝()