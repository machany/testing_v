class 매물:
    def __init__(self, 위치, 종류, 타입, 돈, 시공날짜):
        self.위치 = 위치
        self.종류 = 종류
        self.타입 = 타입
        self.돈 = 돈
        self.시공날짜 = 시공날짜

    def 정보(self):
        print("\n{0}의 XX{1} {2} 가격은 {3}원 입니다. [{4}년에 완공됨]".format(self.위치,\
            self.종류, self.타입, self.돈, self.시공날짜))

매물1 = 매물("강남", "아파트", "급매", "24억", 2019)
매물2 = 매물("서울", "고급 아파트", "매매", "37억", 2020)
매물3 = 매물("마포구", "오피스텔", "전세", "4억", 2007)
매물4 = 매물("송남", "빌라", "월세", "보증700만원/75만", 1999)
매물5 = 매물("서울", "원룸", "월세", "보증480만원/57만", 2011)
건물정보 = []
건물정보.append(매물1)
건물정보.append(매물2)
건물정보.append(매물3)
건물정보.append(매물4)
건물정보.append(매물5)
print("\n{0}개의 매물이 존재합니다.".format(len(건물정보)))
for 매물 in 건물정보:
    매물.정보()