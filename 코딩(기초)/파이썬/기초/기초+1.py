수 = [1, 2, 3, 4]
숫자 = [11, 2, 33, 44]
for 수_상, 수_하 in enumerate(수):
    print("수 =", 수_하)
    for 숫자_상, 숫자_하 in enumerate(숫자): # 여기에서 수행할 값이 없을시
        print("숫자 =", 숫자_하) #                 #
        if 숫자_하 == 수_하: #                     #
            print("같다")  #                       #
            break # <ㅡ이쪽 break문을 # 주석처리하면 # 이쪽 break문을 탈수없음  l
    else: # for문도 if처럼 else을 사용하수있음      #                          l
        continue # 이와 같이 continue 명령어로 ^해당for문 밖의 for문을 실행    l
    print("아래 break문 사용")
    break # <    <    <    <    <    <    <    <    <-이쪽 break문을 타려면이 ^break를 타야만 한다
print("바깥for문 탈출")