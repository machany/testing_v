class CGM:
    def __init__(self, 인원):
        self.인원 = 인원
    
    def 일반_티켓(self):
        print("일반 티켓 {0}장을 구입하셔서 총 {1}원을 내셔야합니다.".format(self.인원, self.인원 * 11000))

    def 아침_일반_티켓(self):
        print("아침 일반 티켓 {0}장을 구입하셔서 총 {1}원을 내셔야합니다.".format(self.인원, (self.인원 * 11000) - (1000 * self.인원)))

    def 어린이_티켓(self):
        print("어린이 티켓 {0}장을 구입하셔서 총 {1}원을 내셔야합니다.".format(self.인원, self.인원 * 8000))

    def 아침_어린이_티켓(self):
        print("아침 어린이 티켓 {0}장을 구입하셔서 총 {1}원을 내셔야합니다.".format(self.인원, (self.인원 * 8000) - (self.인원 * 1000)))

    def 군인_티켓(self):
        print("군인 티켓 {0}장을 구입하셔서 총 {1}원을 내셔야합니다.".format(self.인원, self.인원 * 8000))

    def 아침_군인_티켓(self):
        print("아침 군인 티켓 {0}장을 구입하셔서 총 {1}원을 내셔야합니다.".format(self.인원, (self.인원 * 8000) - (self.인원 * 1000)))

    def 이벤트_티켓(self):
        print("이벤트 티켓 {0}장을 구입하셔서 총 {1}원을 내셔야합니다.".format(self.인원, self.인원 * 2000))

if __name__ == "__main__":
    print("모듈안에서 직접실행할때")
    영화관1 = CGM(4)
    영화관1.이벤트_티켓()
else:
    print("모듈 밖에서 실행될때")
