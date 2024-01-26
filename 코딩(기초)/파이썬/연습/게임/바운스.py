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
이미지_위치 = os.path.join(이미지_폴더_위치, "이미지") # 캐릭터 이미지가 있는 폴더 위치 반환

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

적1_y좌표 = 화면크기_세로 - 적1_세로 - 바닥_세로
적1_x좌표 =  2000 #(화면크기_가로 / 2 + 화면크기_가로 / 5) - (적1_가로 / 2)
적1_이동속도 = 3
적1_어그로 = False

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

단2점프 = False
점프 = False
벽_붙밀 = False

시작시간 = pygame.time.get_ticks()

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
                캐릭터_x이동 = 캐릭터_이동_속도 * 1

            if event.key == pygame.K_d: # K_원하는 키
               캐릭터_x이동 = 캐릭터_이동_속도 * -1

            if event.key == pygame.K_w or event.key == pygame.K_SPACE: # K_원하는 키
                if 단2점프 == True:
                    pass
                elif 점프 == True:
                    캐릭터_y이동 = 캐릭터_이동_속도 * -1.5
                    단2점프 = True
                elif 단2점프 == False:
                    캐릭터_y이동 = 캐릭터_이동_속도 * -1.5
                    점프 = True

        if event.type == pygame.KEYUP: # 키를 땠을때 (이동X)
            if event.key == pygame.K_w or event.key == pygame.K_SPACE: # or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                pass

            if event.key == pygame.K_a or event.key == pygame.K_d: # or event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                캐릭터_x이동 = 0

    # 무기쪽, 공쪼개기는 https://www.youtube.com/watch?v=Dkx8Pl6QKW0&t을 보면 된다.
    # 속도를 줄일때 X이동 = -10 이라 가정 X이동 += 0.1 으로하면 점점느려짐. 부호가 다르면 반대로

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

    좌벽_x좌표 += 캐릭터_x이동
    우벽_x좌표 += 캐릭터_x이동

    # 적
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

    if 벽_붙밀 == True:
        캐릭터_x이동 = 0
        벽_붙밀 = False

    if 점프 == True:
        캐릭터_y좌표 += 캐릭터_y이동
        캐릭터_y이동 += 0.5
        if 캐릭터_y좌표 >= 화면크기_세로 - 바닥_세로:
            점프 = False
            단2점프 = False
            캐릭터_y이동 = 0

    경과시간 = int(((pygame.time.get_ticks()) - 시작시간) / 1000)
    타이머 = 게임폰트.render(str(경과시간), True, (0, 255, 0))

    화면.fill((200, 200, 200)) # R, G, B 값으로도 지정가능
    # 화면.blit(배경, (0, 0)) # 배경그리기 단, 파이썬은 계속 그려주어야함
    화면.blit(바닥, (바닥_x좌표, 바닥_y좌표))
    화면.blit(좌벽, (좌벽_x좌표, 좌벽_y좌표))
    화면.blit(우벽, (우벽_x좌표, 우벽_y좌표))
    #
    화면.blit(타이머, (화면크기_가로 / 2 - 30, 10))
    화면.blit(캐릭터, (캐릭터_x좌표, 캐릭터_y좌표))
    화면.blit(적1, (적1_x좌표, 적1_y좌표))

    플레이어_확인 = 게임폰트.render("you", True, (0, 0, 0))
    if 탭 == True:
        화면.blit(플레이어_확인, (캐릭터_x좌표 - 8, 캐릭터_y좌표 - 30))
        if 경과시간 >= 탭시간 + 3:
            탭 = False

    pygame.display.update() # 이걸로 계속 업데이트


진행상황 = open("현 진행상황", "w", encoding="utf8")

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