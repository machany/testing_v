비교대상1 = "철수"
비교대상2 = "칠수"
비교방법 = "나이차이"
비교이유 = "어리다"
나이1 = 19
나이2 = 31
구별 = 나이2 < 나이1

#을 사용하면 숨김처리가 되어 실행중일때 보이지않는다.
'''작은 따음표3개를 사용하면
작은 따음표가 끝나는 데까지
숨김 처리가 된다'''
#여러 문장을 드레그한뒤 컨트롤 + 슬러쉬를 누르면
#일괄 숨김 처리된다

print(비교대상1 + "와 " + 비교대상2 + "는(은) " + 비교방법 + "가 있다")
print(비교대상2 +"는 " + 비교이유)
비교대상1 = "철수"
비교대상2 = "칠수"
print(비교대상1 + "는 " + str(나이2) + "살이다")
print(비교대상2 + "는 " ,나이1, "살이다")
print(비교대상1 + "는(은)" ,비교대상2, "보다 나이가 적다")
print(구별)
# ,을 사용하게되면 뛰어쓰기가 자동 포함된다
