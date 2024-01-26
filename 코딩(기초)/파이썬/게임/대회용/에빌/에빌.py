# 비고
'''현재 틀을 가져오되 class와 def를 적극 사용해 보기 쉽게 만들것
'''

# 주 내용
import os
from this import d # 파일위치 확인하기
import pygame # 파이게임 불러오기
pygame.init() # 초기화 (필수)
화면크기_가로 = 1540 # 1540 (전체화면 가로)
화면크기_세로 = 805 # 805 (전체화면 세로)
화면 = pygame.display.set_mode((화면크기_가로, 화면크기_세로)) # 화면설정
pygame.display.set_caption("에빌") # 타이틀(제목)설정

이미지_폴더_위치 = os.path.dirname(__file__) # 현재 폴더 위치 반환
이미지_위치 = os.path.join(이미지_폴더_위치, "에빌 이미지") # 캐릭터 이미지가 있는 폴더 위치 반환

캐릭터 = pygame.image.load(os.path.join(이미지_위치, "(임시)캐릭터.png"))
캐릭터_크기 = 캐릭터.get_rect().size # 이미지 크기를 구해옴
캐릭터_가로 = 캐릭터_크기[0] # 캐릭터의 가로크기
캐릭터_세로 = 캐릭터_크기[1] # 캐릭터의 세로크기  ### 캐릭터가 바닥위에 있게하기위해

적1 = pygame.image.load(os.path.join(이미지_위치, "(임시)적.png"))
적1_크기 = 적1.get_rect().size
적1_가로 = 적1_크기[0]
적1_세로 = 적1_크기[1]

바닥 = pygame.image.load(os.path.join(이미지_위치, "(임시)바닥.png"))
바닥_크기 = 바닥.get_rect().size
바닥_세로 = 바닥_크기[1] # 캐릭터가 바닥위에 있게하기위해

좌벽 = pygame.image.load(os.path.join(이미지_위치, "(임시)좌벽.png"))
좌벽_크기 = 좌벽.get_rect().size
좌벽_가로 = 좌벽_크기[0]

우벽 = pygame.image.load(os.path.join(이미지_위치, "(임시)우벽.png"))
우벽_크기 = 우벽.get_rect().size
우벽_가로 = 우벽_크기[0]

캐릭터_y좌표 = 화면크기_세로 - 캐릭터_세로 - 바닥_세로 + 1 # 바닥위 # 위치설정은 알아서
캐릭터_x좌표 = (화면크기_가로 / 2) - (캐릭터_가로 / 2) # 정중앙

#          검          #
검 = pygame.image.load(os.path.join(이미지_위치, "(임시)우검.png"))
검_크기 = 검.get_rect().size
검_가로 = 검_크기[0]

검_y좌표 = 캐릭터_y좌표 + 20
검_x좌표 = 캐릭터_x좌표 

검_공격_상태 = False
검_공격_방향_위 = False
검_공격_방향_아래 = True
검_공격_방향_찌르기 = False
검_변경 = False
검_공격_중 = False

검_공격_후 = False

우검 = True
좌검 = False

찌르기_초 = False
찌르기_중 = False
찌르기_후 = False

베기_초 = False
베기_중 = False
베기_후 = False

검_1회_이동 = False
#          검          #

적1_y좌표 = 화면크기_세로 - 적1_세로 - 바닥_세로
적1_x좌표 =  2000 #(화면크기_가로 / 2 + 화면크기_가로 / 5) - (적1_가로 / 2)
적1_이동속도 = 3
적1_어그로 = False
적1_체력 = 100
공격_감소_카운팅 = False

바닥_y좌표 = 화면크기_세로 - 바닥_세로
바닥_x좌표 = 0

좌벽_y좌표 = 0
좌벽_x좌표 = 10 - 좌벽_가로

우벽_y좌표 = 0
우벽_x좌표 = 화면크기_가로 * 3 - 10

게임폰트 = pygame.font.Font(None, 30) # 변수 설정 = 폰트 생성(사용 폰트, 크기)
캐릭터_x이동 = 0
캐릭터_y이동 = 0
캐릭터_이동_속도 = 10

프레임속도 = 60
프레임 = pygame.time.Clock() # 으로 프레임을 설정하게 바꿀수있으며

y점프 = False
벽_붙밀 = False

달리기 = False
대쉬_쿨 = False
대쉬사용시간 = 0
대쉬_쿨타임 = 5
대쉬_숙련도 = 150

우 = False
좌 = False

시작시간 = pygame.time.get_ticks()

최대스테미나 = 100 * 10
스테미나 = 최대스테미나 / 2
스테미나_회복량 = 0.1
스테미나_회복량_감소 = False
스테미나_중간전 = True
스테미나_감소 = False

공격력 = 10

녹다운 = False
스테미나_감소_달리기 = False
스테미나_감소_걷기 = False

탭 = True
탭시간 = 0

진행여부 = True
while 진행여부:
    프레임_설정 = 프레임.tick(프레임속도) # 으로 프레임을 설정한다. (프레임수)
    for event in pygame.event.get(): # 게임개발중 필수 키보드 입력, 마우스조작등을 확인 
        if event.type == pygame.QUIT: # (창닫기 버튼을 눌렀을때) (FULLSCREEN = 전체화면)
            진행여부 = False # 게임종료

        if event.type == pygame.KEYDOWN: # KEYDOWN는 반드시 대문자로 (키보드 버튼을 눌렀을때)
            if event.key == pygame.K_a: # K_원하는 키
                if 녹다운 == False:
                    if 달리기 == True:
                        캐릭터_x이동 = 캐릭터_이동_속도 * 1
                        스테미나_감소_달리기 = True
                    else:
                        캐릭터_x이동 = 캐릭터_이동_속도 * 0.5
                        스테미나_감소_걷기 = True
                    스테미나_감소 = True
                    좌 = True
                    검_변경 = True

            if event.key == pygame.K_d: # K_원하는 키
                if 녹다운 == False:
                    if 달리기 == True:
                        캐릭터_x이동 = 캐릭터_이동_속도 * -1
                        스테미나_감소_달리기 = True
                    else:
                        캐릭터_x이동 = 캐릭터_이동_속도 * -0.5
                        스테미나_감소_걷기 = True
                    스테미나_감소 = True
                    우 = True
                    검_변경 = True

            if event.key == pygame.K_w or event.key == pygame.K_SPACE: # K_원하는 키
                if 녹다운 == False:
                    if y점프 == True:
                        pass
                    else :
                        캐릭터_y이동 = 캐릭터_이동_속도 * -1.5
                        y점프 = True
                    스테미나 -= 1

            if event.key == pygame.K_r:
                if 달리기 == False:
                    달리기 = True
                else :
                    달리기 = False

            if event.key == pygame.K_TAB:
                탭 = True
                탭시간 = 경과시간

            if event.key == pygame.K_t:
                if 검_공격_방향_찌르기 == True:
                    검_공격_방향_찌르기 = False
                elif 검_공격_방향_찌르기 == False:
                    검_공격_방향_찌르기 = True

            # 개발자용 삭제할것
            if event.key == pygame.K_1:
                스테미나 += 100

            if event.key == pygame.K_2:
                최대스테미나 += 100

            if event.key == pygame.K_3:
                스테미나_회복량 += 0.05
            # 개발자용 삭제할것

        if event.type == pygame.KEYUP: # 키를 땠을때 (이동X)
            if event.key == pygame.K_w or event.key == pygame.K_SPACE: # or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                pass

            if event.key == pygame.K_a or event.key == pygame.K_d: # or event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                캐릭터_x이동 = 0
                스테미나_감소 = False
                스테미나_감소_달리기 = False
                스테미나_감소_걷기 = False
                우 = False
                좌 = False

        if event.type == pygame.MOUSEBUTTONDOWN: # MOUSEBUTTONDOWNd은 대문자로(마우스 클릭(좌, 우, 휠모두))
            # print(pygame.mouse.get_pos()) # 마우스의 위치(좌표 (x, y) ) 출력
            # print(event.button) # 1 = 좌클릭, 2 = 휠 클릭, 3 = 우 클릭, 4 = 휠 올리기, 5 = 휠 내리기
            if event.button == 1:
                if 검_공격_상태 == False:
                    검_공격_상태 = True
                    if 검_공격_방향_찌르기 == True:
                        스테미나 -= 15
                    else:
                        스테미나 -= 10

            if event.button == 3:
                if 스테미나 >= 최대스테미나 / 20 + 대쉬_숙련도 + 최대스테미나 / 10:
                    if 대쉬_쿨 == False:
                        대쉬사용시간 = 경과시간
                        if 좌 == True:
                            캐릭터_x이동 = 캐릭터_이동_속도 * (대쉬_숙련도 / 10)
                            좌벽_x좌표 += 캐릭터_x이동
                            우벽_x좌표 += 캐릭터_x이동
                            적1_x좌표 += 캐릭터_x이동
                            캐릭터_x이동 = 캐릭터_이동_속도 * 0.5
                            스테미나 -= 최대스테미나 / 20 + 대쉬_숙련도
                            #대쉬_쿨 = True
                            대쉬_숙련도 += 5
                        elif 우 == True:
                            캐릭터_x이동 = 캐릭터_이동_속도 * -(대쉬_숙련도 / 10)
                            좌벽_x좌표 += 캐릭터_x이동
                            우벽_x좌표 += 캐릭터_x이동
                            적1_x좌표 += 캐릭터_x이동
                            캐릭터_x이동 = 캐릭터_이동_속도 * -0.5
                            스테미나 -= 최대스테미나 / 20 + 대쉬_숙련도
                            #대쉬_쿨 = True
                            대쉬_숙련도 += 5
                        if 대쉬_숙련도 >= 1000:
                            대쉬_숙련도 = 1000

        if event.type == pygame.MOUSEBUTTONUP: # 마우스를 땠을때
            pass # aprint("땠다!")

        if event.type == pygame.MOUSEMOTION: # 마우스를 움직일때
            pass # print("움직이고 있다!")

    # 무기쪽, 공쪼개기는 https://www.youtube.com/watch?v=Dkx8Pl6QKW0&t을 보면 된다.
    # 속도를 줄일때 X이동 = -10 이라 가정 X이동 += 0.1 으로하면 점점느려짐. 부호가 다르면 반대로

    if 검_공격_상태 != True:
        검_x좌표 = 검_x좌표
        검_y좌표 = 캐릭터_y좌표

    if 찌르기_후 == True:
        if 우검 == True:
            검_x좌표 = 캐릭터_x좌표
        elif 좌검 == True:
            검_x좌표 = 캐릭터_x좌표 - 캐릭터_가로 * 2 + 7
        검_공격_상태 = False
        찌르기_후 = False
        최대스테미나 += 1.5
        스테미나_회복량 += 0.00003
        검_공격_중 = False

    if 베기_후 == True:
        if 검_공격_방향_위 == True:
            if 검_y좌표 >= 캐릭터_y좌표 - (캐릭터_세로 + 캐릭터_세로 / 2):
                검_y좌표 -= 5
            elif 검_y좌표 <= 캐릭터_y좌표 - (캐릭터_세로 + 캐릭터_세로 / 2):
                검_공격_후 = True
        else:
            if 검_y좌표 >= 캐릭터_y좌표 + (캐릭터_세로 + 캐릭터_세로 / 2):
                    검_y좌표 += 5
            elif 검_y좌표 <= 캐릭터_y좌표 + (캐릭터_세로 + 캐릭터_세로 / 2):
                검_공격_후 = True

        if 검_공격_후 == True:
            검_y좌표 = 캐릭터_y좌표
            if 우검 == True:
                검_x좌표 = 캐릭터_x좌표
            elif 좌검 == True:
                검_x좌표 = 캐릭터_x좌표 - 캐릭터_가로 * 2 + 7

            if 검_공격_방향_아래 == True:
                검_공격_방향_위 = True
                검_공격_방향_아래 = False
            elif 검_공격_방향_위 == True:
                검_공격_방향_아래 = True
                검_공격_방향_위 = False
            검_공격_상태 = False
            베기_후 = False
            최대스테미나 += 1.5
            스테미나_회복량 += 0.00003
            검_공격_중 = False
            검_1회_이동 = False
            검_공격_후 = False

    if 찌르기_중 == True:
        검_y좌표 = 캐릭터_y좌표
        if 우검 == True:
            if 검_x좌표 <= 캐릭터_x좌표 + 캐릭터_가로 * 3:
                검_x좌표 += 15
            elif 검_x좌표 >= 캐릭터_x좌표 + 캐릭터_가로 * 3:
                찌르기_중 = False
                찌르기_후 = True
        elif 좌검 == True:
            if 검_x좌표 >= 캐릭터_x좌표 - 캐릭터_가로 * 3:
                검_x좌표 -= 15
            elif 검_x좌표 <= 캐릭터_x좌표 - 캐릭터_가로 * 3:
                찌르기_중 = False
                찌르기_후 = True

    if 베기_중 == True:
        if 검_공격_방향_위 == True:
            if 검_y좌표 <= 캐릭터_y좌표 - 캐릭터_세로:
                    검_y좌표 -= 2
            elif 검_y좌표 >= 캐릭터_y좌표 - 캐릭터_세로:
                if 우검 == True:
                    검 = pygame.image.load(os.path.join(이미지_위치, "(임시)우검_상.png"))
                elif 좌검 == True:
                    검 = pygame.image.load(os.path.join(이미지_위치, "(임시)좌검_상.png"))
                베기_중 = False
                베기_후 = True
        else:
            if 검_y좌표 <= 캐릭터_y좌표 + 캐릭터_세로 / 2:
                    검_y좌표 += 3
            elif 검_y좌표 >= 캐릭터_y좌표 + 캐릭터_세로 / 2:
                if 우검 == True:
                    검 = pygame.image.load(os.path.join(이미지_위치, "(임시)우검.png"))
                elif 좌검 == True:
                    검 = pygame.image.load(os.path.join(이미지_위치, "(임시)좌검.png"))
                베기_중 = False
                베기_후 = True

    if 찌르기_초 == True:
        if 우검 == True:
            if 검_x좌표 >= 캐릭터_x좌표 - 캐릭터_가로:
                검_x좌표 -= 4
            elif 검_x좌표 <= 캐릭터_x좌표 - 캐릭터_가로:
                찌르기_중 = True
                찌르기_초 = False
        elif 좌검 == True:
            if 검_x좌표 <= 캐릭터_x좌표 + 캐릭터_가로 / 2:
                검_x좌표 += 8
            elif 검_x좌표 >= 캐릭터_x좌표 + 캐릭터_가로 / 2:
                찌르기_중 = True
                찌르기_초 = False

    if 베기_초 == True:
        if 검_공격_방향_위 == True:
            if 검_y좌표 >= 캐릭터_y좌표 - 캐릭터_세로 / 2:
                검_y좌표 -= 3
            elif 검_y좌표 <= 캐릭터_y좌표 - 캐릭터_세로 / 2:
                베기_초 = False
                베기_중 = True
        else:
            if 검_y좌표 >= 캐릭터_y좌표 - 캐릭터_세로:
                검_y좌표 -= 5
            elif 검_y좌표 <= 캐릭터_y좌표 - 캐릭터_세로:
                if 우검 == True:
                    검 = pygame.image.load(os.path.join(이미지_위치, "(임시)우검_중.png"))
                elif 좌검 == True:
                    검 = pygame.image.load(os.path.join(이미지_위치, "(임시)좌검_중.png"))
                베기_초 = False
                베기_중 = True

    if 녹다운 == False:
        if 검_공격_상태 == True:
            if 검_공격_방향_찌르기 == True:
                if 검_1회_이동 == False:
                    if 우검 == True:
                        검 = pygame.image.load(os.path.join(이미지_위치, "(임시)우검_중.png"))
                    elif 좌검 == True:
                        검 = pygame.image.load(os.path.join(이미지_위치, "(임시)좌검_중.png"))
                    찌르기_초 = True
                    검_공격_중 = True

            elif 검_공격_방향_위 == True:
                if 검_1회_이동 == False:
                    if 우검 == True:
                        검 = pygame.image.load(os.path.join(이미지_위치, "(임시)우검_중.png"))
                        검_x좌표 += 10 + 캐릭터_가로
                    elif 좌검 == True:
                        검 = pygame.image.load(os.path.join(이미지_위치, "(임시)좌검_중.png"))
                        검_x좌표 -= 10
                    검_y좌표 += 10
                    검_1회_이동 = True
                    베기_초 = True
                    검_공격_중 = True

            elif 검_공격_방향_아래 == True:
                if 검_1회_이동 == False:
                    if 우검 == True:
                        검 = pygame.image.load(os.path.join(이미지_위치, "(임시)우검_상.png"))
                        검_x좌표 += 10 + 캐릭터_가로
                    elif 좌검 == True:
                        검 = pygame.image.load(os.path.join(이미지_위치, "(임시)좌검_상.png"))
                        검_x좌표 -= 10
                    검_y좌표 -= 15
                    검_1회_이동 = True
                    베기_초 = True
                    검_공격_중 = True

    #         스테미나         #
    if 스테미나_감소_달리기 == True:
        스테미나 -= 0.3
        최대스테미나 += 0.05 * 1000
        스테미나_회복량 += 0.00005 * 1000
    elif 스테미나_감소_걷기 == True:
        스테미나 -= 0.05
        최대스테미나 += 0.01
        스테미나_회복량 += 0.00001

    if 스테미나_감소 == False:
        스테미나 += 스테미나_회복량
    
    if 녹다운 == True:
        스테미나_감소 = True
        if 스테미나 <= 최대스테미나 / 3:
            스테미나 += 스테미나_회복량
        else:
            최대스테미나 += 50
            스테미나_회복량 += 0.0005
            녹다운 = False
            스테미나_감소 = False

    if 스테미나 <= 0:
        스테미나 = 0
        녹다운 = True

    # 기술
    if 스테미나 <= 최대스테미나 / 10:
        달리기 = False
        스테미나_감소 = False
        녹다운 = True

    if 스테미나_중간전 == True:
        if 스테미나 >= 최대스테미나 / 2:
            if 스테미나_회복량_감소 == False:
                스테미나_회복량 = 스테미나_회복량 / 10
                스테미나_회복량_감소 = True
                스테미나_중간전 = False

        elif 스테미나 <= 최대스테미나 / 2:
            if 스테미나_회복량_감소 == True:
                스테미나_회복량 = 스테미나_회복량 * 10
                스테미나_회복량_감소 = False
                스테미나_중간전 = True

    elif 스테미나_중간전 == False:
        if 스테미나 >= 최대스테미나:
            스테미나 = 최대스테미나

        elif 스테미나 <= 최대스테미나 / 2:
            스테미나_중간전 = True
    #         스테미나         #

    if 캐릭터_x좌표 <= 0:
        캐릭터_x좌표 = 0 - 캐릭터_x이동
    elif 캐릭터_x좌표 >= 화면크기_가로 - 캐릭터_가로:
        캐릭터_x좌표 = 화면크기_가로 - 캐릭터_가로 - 캐릭터_x이동
    
    if 캐릭터_y좌표 >= 화면크기_세로 - 바닥_세로:
        캐릭터_y좌표 = 화면크기_세로 - 캐릭터_세로 - 바닥_세로

    # 위치 정보 업데이트 
    바닥_위치 = 바닥.get_rect()
    바닥_위치.top = 바닥_y좌표 + 바닥_세로

    좌벽_위치 = 좌벽.get_rect()
    좌벽_위치.right = 좌벽_x좌표 + 좌벽_가로

    우벽_위치 = 우벽.get_rect()
    우벽_위치.right = 우벽_x좌표 + 우벽_가로

    캐릭터_위치 = 캐릭터.get_rect()
    캐릭터_위치.right = 캐릭터_x좌표 + 캐릭터_가로
    캐릭터_위치.top = 캐릭터_y좌표

    검_위치 = 검.get_rect()
    검_위치.right = 검_x좌표 + 검_가로
    검_위치.top = 검_y좌표

    적1_위치 = 적1.get_rect()
    적1_위치.right = 적1_x좌표 + 적1_가로
    적1_위치.top = 적1_y좌표

    #          충돌          #
    if 캐릭터_위치.colliderect(적1_위치):
        # 실제로는 체력 감소 처리 요함.
        게임오버 = 게임폰트.render("Game Over", True, (255, 0, 0))
        화면.blit(게임오버, (화면크기_가로 / 2 - 10, 화면크기_세로 / 2 - 3))
        pygame.display.update()

    if 캐릭터_위치.colliderect(좌벽_위치):
        캐릭터_x이동 = -10
        벽_붙밀 = True

    if 캐릭터_위치.colliderect(우벽_위치):
        캐릭터_x이동 = 10
        벽_붙밀 = True
    #          충돌          #

    #          기술 쿨          #
    if 대쉬_쿨 == True:
        if 경과시간 >= 대쉬사용시간 + 대쉬_쿨타임:
            대쉬_쿨 = False
    #          기술 쿨          #

    좌벽_x좌표 += 캐릭터_x이동
    우벽_x좌표 += 캐릭터_x이동

    # 적 #
    if 검_위치.colliderect(적1_위치):
        if 검_공격_중 == True:
            if 공격_감소_카운팅 != True:
                적1_체력 -= 공격력
                공격_감소_카운팅 = True

    if 적1_y좌표 >= 화면크기_세로 - 바닥_세로:
        적1_y좌표 = 화면크기_세로 - 적1_세로 - 바닥_세로
    
    if 적1_어그로 == True:
        if 적1_x좌표 >= 캐릭터_x좌표:
            적1_x좌표 += 캐릭터_x이동 - 적1_이동속도
        elif 적1_x좌표 <= 캐릭터_x좌표:
            적1_x좌표 += 캐릭터_x이동 + 적1_이동속도
    else:
        적1_x좌표 += 캐릭터_x이동

    if 적1_어그로 != True:
        if 적1_x좌표 <= 화면크기_가로 - 적1_가로 * 5 and 적1_x좌표 >= 적1_가로 * 5:
            적1_어그로 = True
    else:
        if 적1_x좌표 <= 화면크기_가로 + 적1_가로 * 5 and 적1_x좌표 >= -적1_가로 * 5:
            적1_어그로 = False

    if 검_변경 == True:
        if 우 == True:
            검_x좌표 = 캐릭터_x좌표
            우검 = True
            좌검 = False
        if 좌 == True:
            검_x좌표 = 캐릭터_x좌표 - 캐릭터_가로 * 2 + 7
            좌검 = True
            우검 = False
        검_변경 = False

    if 검_공격_상태 == False:
        if 우검 == True:
            검 = pygame.image.load(os.path.join(이미지_위치, "(임시)우검.png"))
        elif 좌검 == True:
            검 = pygame.image.load(os.path.join(이미지_위치, "(임시)좌검.png"))

    if 검_공격_중 != True:
        if y점프 == True:
            캐릭터_y좌표 += 캐릭터_y이동
            캐릭터_y이동 += 0.5
            if 캐릭터_y좌표 >= 화면크기_세로 - 바닥_세로:
                y점프 = False
                캐릭터_y이동 = 0

    if 벽_붙밀 == True:
        캐릭터_x이동 = 0
        벽_붙밀 = False

    경과시간 = int(((pygame.time.get_ticks()) - 시작시간) / 1000)
    타이머 = 게임폰트.render(str(경과시간), True, (0, 255, 0))

    화면.fill((200, 200, 200)) # R, G, B 값으로도 지정가능
    # 화면.blit(배경, (0, 0)) # 배경그리기 단, 파이썬은 계속 그려주어야함
    화면.blit(바닥, (바닥_x좌표, 바닥_y좌표))
    화면.blit(좌벽, (좌벽_x좌표, 좌벽_y좌표))
    화면.blit(우벽, (우벽_x좌표, 우벽_y좌표))
    #
    화면.blit(타이머, (화면크기_가로 / 2 - 30, 10))
    화면.blit(검, (검_x좌표, 검_y좌표))
    화면.blit(캐릭터, (캐릭터_x좌표, 캐릭터_y좌표))
    화면.blit(적1, (적1_x좌표, 적1_y좌표))

    플레이어_확인 = 게임폰트.render("you", True, (0, 0, 0))
    if 탭 == True:
        화면.blit(플레이어_확인, (캐릭터_x좌표 - 8, 캐릭터_y좌표 - 30))
        if 경과시간 >= 탭시간 + 3:
            탭 = False

    #          개발자요 확인 수치          #
    스테미나_최대량_수치__개발자용__ = 게임폰트.render(str(int(최대스테미나)), True, (255, 255, 255))
    스테미나_회복량_수치__개발자용__ = 게임폰트.render(str(int(스테미나_회복량)), True, (255, 255, 255))
    스테미나_잔여량_수치__개발자용__ = 게임폰트.render(str(int(스테미나)), True, (255, 255, 255)) # 글자 = 폰트변수.render(출력할 글자), True, (색깔))
    대쉬_숙련도_상태__개발자용__ = 게임폰트.render(str(int(대쉬_숙련도)), True, (255, 255, 255))
    #          개발자요 확인 수치          #

    화면.blit(스테미나_최대량_수치__개발자용__, (100, 110))
    화면.blit(스테미나_회복량_수치__개발자용__, (100, 60))
    화면.blit(스테미나_잔여량_수치__개발자용__, (170, 110))
    화면.blit(대쉬_숙련도_상태__개발자용__, (100, 160))

    pygame.display.update() # 이걸로 계속 업데이트


진행상황 = open("현 진행상황", "w", encoding="utf8")
print(최대스테미나, file=진행상황)
print(스테미나_회복량, file=진행상황)
print(스테미나, file=진행상황)
print(대쉬_숙련도, file=진행상황)
진행상황.close()

pygame.time.delay(1000) # 일시정지 역할을하며 단위는 밀리세컨드 (원하는시간 초단위로 환산후 곱하기 1000)

pygame.quit() # 게임종료

# 마지막 테스트 총평 / 수정사항
'''수정이 상대적으로 힘듬, 기초 토대 준완, 재미 없음

추가할 내용
체력, 적 공격기, 스킬, 인터페이스

세부
공격어색, 기술사용이 의도와 다름

1차 추가 내용
캐릭터, 움직임

2차 추가 내용
캐릭터 움직임, 스텟, 넉다운, 대시

3차 추가 내용
공격, 적, 개발자 테스트

마지막 추가 내용
오류수정, 벨런스 조정, 전체 수정'''