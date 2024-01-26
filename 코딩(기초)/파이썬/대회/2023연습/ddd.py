입력값 = input(("입력하시오"))

값1 = 0
값2 = 1
글자수 = (len(입력값))
정리 = []

while 글자수 != 0:
    정리.append(입력값[값1 : 값2])
    값1 += 1
    값2 += 1
    글자수 -= 1
print(정리)

"""A위치 = 입력값.index("A")
B위치 = 입력값.index("B")
C위치 = 입력값.index("C")

# A위치 = 입력값.index("A", A위치 + 1)
A시도 = 0
B시도 = 0

시도 = 정리
A위치 = 시도.index("A", A위치 + A시도)
B위치 = 시도.index("B", B위치 + B시도)
print(시도)
if A위치 < B위치:
    시도.pop(A위치)
    print(시도)
    B위치 = 시도.index("B", B위치 + B시도)
    시도.pop(B위치)
    print(시도)
B위치 = 시도.index("B", B위치 + B시도)
C위치 = 시도.index('C')
시도.pop(B위치)
print(시도)
if B위치 < C위치:
    시도.pop(B위치 - 1)
    C위치 = 시도.index('C')
    시도.pop(C위치 - 1)
    print(시도)"""