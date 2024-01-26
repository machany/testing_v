class 오메가박스:
    def __init__(self, 인원):
        self.인원 = 인원

    def 일반_티켓(self):
        print("일반 티켓 {0}장을 구입하셔서 총 {1}원을 내셔야합니다.".format(self.인원, self.인원 * 12000))

    def 아침_일반_티켓(self):
        print("아침 일반 티켓 {0}장을 구입하셔서 총 {1}원을 내셔야합니다.".format(self.인원, (self.인원 * 12000) - (2500 * self.인원)))

    def 어린이_티켓(self):
        print("어린이 티켓 {0}장을 구입하셔서 총 {1}원을 내셔야합니다.".format(self.인원, self.인원 * 8500))

    def 아침_어린이_티켓(self):
        print("아침 어린이 티켓 {0}장을 구입하셔서 총 {1}원을 내셔야합니다.".format(self.인원, (self.인원 * 8500) - (self.인원 * 2500)))

    def 군인_티켓(self):
        print("군인 티켓 {0}장을 구입하셔서 총 {1}원을 내셔야합니다.".format(self.인원, self.인원 * 6000))

    def 아침_군인_티켓(self):
        print("아침 군인 티켓 {0}장을 구입하셔서 총 {1}원을 내셔야합니다.".format(self.인원, (self.인원 * 6000) - (self.인원 * 2500)))

    def 회원_티켓(self):
        print("회원 티켓 {0}장을 구입하셔서 총 {1}원을 내셔야합니다.".format(self.인원, self.인원 * 5000))

    def 아침_회원_티켓(self):
        print("아침 회원 티켓 {0}장을 구입하셔서 총 {1}원을 내셔야합니다.".format(self.인원, (self.인원 * 5000) - (self.인원 * 2500)))

    def 골든_회원_티켓(self):
        print("회원 티켓 {0}장을 구입하셔서 총 {1}원을 내셔야합니다.".format(self.인원, self.인원 * 3000))

    def 아침_골든_회원_티켓(self):
        print("아침 회원 티켓 {0}장을 구입하셔서 총 {1}원을 내셔야합니다.".format(self.인원, (self.인원 * 3000) - (self.인원 * 2500)))
