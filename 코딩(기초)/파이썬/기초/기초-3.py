#연산자
'''# +는 더하기 -는 빼기 *는 곱하기 /은 나누기 *두개는 제곱
# %는 그수를 나누기한값의 나머지를 구한다 /두번은 몫을 구한다 
# <>크다작다 뒤에 =을 붙여 크거나 같다 작거나 같다로함
# =두번은 똑같다 =앞에 !가붙으면 ~~이 아니다가된다.'''
# ((~~) and (~~))을 하면 앞 뒤가 진실일때만 진실이 나온다. (&도 가능)
# ((~~) or (~~))을하면 하나라도 진실일떄 진실이 나온다. (|도 가능 -엔터위-)
# (~<~<~) 연속 비교도 가능
숫자 = 10
print(숫자)
숫자 = 숫자 + 5 #이렇게도 가능
print(숫자) # ^
숫자 = 10   # |
print(숫자) # |
숫자 += 5 # 위와 같은 결과 출력 (다른 기호와도 사용가능)
print(숫자)
# abs(~~) 숫자의 절대값구하기 pow(~, ~) 앞수의 (뒷수)제곱
# max(~, ~)괄호안에 숫자중 더큰값 min(~, ~)괄호안에 숫자중 더작은값
# round(소수) 반올림한 값 

# from math import * 를쓴후 쓸수있음
# floor(소수) 내림한값
# ceil(소수) 올림한값 sqrt(~~)괄호안의 수의 제곱근

# from random import * 를쓴후 쓸수있음  
# print(random()) 0.0 ~ 1.0미만의 렌덤수 print(rindom()*13) 0.0 ~ 13.0미만의 렌덤수 (소수포함)
# print(int(random)()*17)) 0 ~ 17미만의 정수 렌덤수 (미만) print(int(rindom)()*17) + 1) 1 ~ 18이하의 정수 렌덤수
# print(randringe)(0, 36)) 0 ~ 36미만의 정수 렌덤수 
# print(randint(2, 41)) 2 ~ 41이하의 정수 렌덤수