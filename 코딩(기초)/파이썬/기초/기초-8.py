print("총", "균", "쇠", sep = " 그리고 ", end = " 저자:")
# sep로 ,를 사용했을때 콤마가 들어간 (공백)안에 무엇을 넣을 지 결정할수있다. 추가로 end로
# 문장끝에 더 무언가를 나오게 할수있다. (문장의 끝 부분을 ~~로 바꿔달라)
print("재러드 다이아몬드")
import sys
print("오스트랄로피테쿠스", "호모사피엔스", file = sys.stdout) # 표준출력으로 코드가 찍힘
print("오스트랄로피테쿠스", "호모사피엔스", file = sys.stderr) # 표준에러로 코드가 찍힘
년도 = {"가온":15, "현빈":8, "현준":4}
for 이름, 년 in 년도.items():
    print(이름.ljust(4), str(년).rjust(2), sep = ":")
    # ljust는 왼쪽에 숫자만큼 공간확보 + (왼쪽 정열)
    # rjust는 오른쪽에 숫자만큼 공간확보 + (오른쪽 정열)
for 수 in range(1,21):
    print("대기번호 : " + str(수).zfill(3)) # zfill(~)은 3개의 숫자에서 빈공간은 0으로 채우라는것
답 = input("아무거나 입력ㄱㄱ") # input를 하고 나온 값은 str같은걸로 감쌀 필요가 없다.
print("당신이 아무거나 입력한값은" + 답 + "인데요!") # 단, 문자열 형태로 저장된다.
print("{0: >10}".format(17)) # {0: >10} >은 오른쪽으로 정열 10은 10칸 뛰어서 라는뜻
print("{0: >+10}".format(-17)) # 숫자앞에 +를 입력하면 양수일때 +를 음수일때 -를 붙여 출력
print("{0:_<+10}".format(-17)) # 공백을 다른걸로 채워 그게 나오게 할수있고 ><방향을 바꿔 정열 발향을 바꿀수있다.
print("{0:,}".format(100000000000)) # {0:,}이렇게 입력해 세자리마다 ,를 찍게할수있다.
print("{0:^<+28,}".format(100000000000)) # 물론 다른 부호도 붙일수있음
print("{0:f}".format(5/3)) # 소수점또한 표현가능
print("{0:.3f}".format(5/3)) # 이렇게한다면 소수점 3자리까지 반올림하라는뜻이다.
파일 = open("기초-8파일.txt", "w", encoding="utf8")
# open("파일이름", "w", encoding="utf8")으로 파일을 열고 이름을 정하고 "w"는 쓰는(쓰기 사용X) 목적
# 으로 연다가 되는데 encoding="utf8"은 한글이 이상하게 출력되는걸 막기위해 입력한다. (쓰면 좋음)
print("파일 입출력", file = 파일) # 으로 원하는 파일에 글을 입력할수있다.
print("테스트 중입니다!", file = 파일) # 
파일.close() # 반드시 꼭 닫아 줘야한다. 닫지않으면 절대 안된다!
파일 = open("기초-8파일.txt", "a", encoding="utf8") # "a"는 이어 쓰는 목적이다.
파일.write("11강까지 있음") # 이런식으로 입력하면 줄바꿈이 없다.
파일.write("\n곧 끝나니까 참으세요.")
파일.close()
파일 = open("기초-8파일.txt", "r", encoding="utf8") # "r"는 읽어오는 목적이다.
print(파일.read()) # 이렇게 입력하면 읽어와서 출력한다.
print(파일.readline()) # 한줄만 읽고, 커서는 줄바꿈 실행
print(파일.readline())
파일.close()
파일 = open("기초-8파일.txt", "r", encoding="utf8")
while True:
    팦 = 파일.readline()
    if not 팦:
        break
    print(팦, end = "")
파일.close()
파일 = open("기초-8파일.txt", "r", encoding="utf8")
팍 = 파일.readlines # 파일을 가져와서 리스트 형태로 저장
for 파 in 팍():
    print(파, end = "")
파일.close()
import pickle
파일 = open("8-파일.pickle", "wb")
파 = {"이름:아우더", "나이:28", "취미", "운전" "드라이브" "레이싱"}
print(파)
pickle.dump(파, 파일) # (파)에 있는 정보를 [파일]에 저장
파일.close()
파일 = open("8-파일.pickle", "rb")
파 = pickle.load(파일) # [파일]에 있는 정보를 (파)에 불러오기
print(파)
파일.close()

# 8-5강 건너뜀 크게 중요 하지 않다 판단.
