print("파이게임이 설치가 안됬다면")
print("\"pip install pygame\"")
print("입력해 주세요")
import os # 파일 확인
import pygame # 파이게임 불러오기
pygame.init() # 초기화 (필수)
화면크기_가로 = 880
화면크기_세로 = 480
화면 = pygame.display.set_mode((화면크기_가로, 화면크기_세로)) # 화면설정
pygame.display.set_caption("공 튕기기") # 타이틀(제목)설정

# 배경 & 캐릭터 이미지 불러오기 경로복사후 큰따음표 안에
이미지_폴더_위치 = os.path.dirname(__file__) # 현재 폴더 위치 반환
이미지_위치 = os.path.join(이미지_폴더_위치, "공 튕구기(이미지)") # 캐릭터 이미지가 있는 폴더 위치 반환
배경 = pygame.image.load(os.path.join(이미지_위치, "배경.png"))
# 배경 = pygame.image.load("C:/Users/한미숙/OneDrive/바탕 화면/양/코딩/활용/# 1 게임/공 튕구기(이미지)/배경.png")
판1 = pygame.image.load(os.path.join(이미지_위치, "판1.png"))
판2 = pygame.image.load(os.path.join(이미지_위치,"판2.png"))
판1_크기 = 판1.get_rect().size # 이미지 크기를 구해옴
판2_크기 = 판2.get_rect().size
판1_가로 = 판1_크기[0] # 캐릭터의 가로크기
판1_세로 = 판1_크기[1] # 캐릭터의 세로크기
판2_가로 = 판2_크기[0]
판2_세로 = 판2_크기[1]
판_1_x좌표 = 화면크기_가로 - ( 화면크기_가로 - 10 - 판1_가로 )
판_2_x좌표 = 화면크기_가로 - 판2_가로 * 2 - 10
판_1_y좌표 = 화면크기_세로 / 2 - 판1_세로 / 2
판_2_y좌표 = 화면크기_세로 / 2 - 판2_세로 / 2
판1이동 = 0
판2이동 = 0

상판 = pygame.image.load(os.path.join(이미지_위치, "상판.png"))
하판 = pygame.image.load(os.path.join(이미지_위치, "하판.png"))
상판_크기 = 상판.get_rect().size
하판_크기 = 하판.get_rect().size
상판_가로 = 상판_크기[0]
상판_세로 = 상판_크기[1]
하판_가로 = 하판_크기[0]
하판_세로 = 하판_크기[1]

공 = pygame.image.load(os.path.join(이미지_위치, "공.png"))
공_크기 = 공.get_rect().size
공_가로 = 공_크기[0]
공_세로 = 공_크기[1]
공_x좌표 = 화면크기_가로 / 2 - 공_가로 / 2
공_y좌표 = 화면크기_세로 / 2 - 공_세로 / 2

빨_현점수 = 0
파_현점수 = 0

게임폰트 = pygame.font.Font(None, 30) # 변수 설정 = 폰트 생성(사용 폰트, 크기)

시작시간 = pygame.time.get_ticks() # 현재 틱을 받아옴

프레임속도 = 240
캐속 = 300 / 프레임속도
공_x속도 = 캐속 / 2
공_y속도 = 공_x속도 / 2
프레임 = pygame.time.Clock() # 으로 프레임을 설정하게 바꿀수있으며

초속증가 = 0
플마판 = True
승패 = False

# [({!중요!})] 이벤트루프 게임 진행여부판단 및 게임조작
진행여부 = True
while 진행여부:
    프레임_설정 = 프레임.tick(프레임속도) # 으로 프레임을 설정한다. (프레임수)
    for event in pygame.event.get(): # 게임개발중 필수 키보드 입력, 마우스조작등을 확인 
        if event.type == pygame.QUIT: # QUIT는 반드시 대문자로 (창닫기 버튼을 눌렀을때)
            진행여부 = False # 게임종료

        if event.type == pygame.KEYDOWN: # KEYDOWN는 반드시 대문자로 (키보드 버튼을 눌렀을때)
            if event.key == pygame.K_w:
                판1이동 -= 캐속
            if event.key == pygame.K_s:
                판1이동 += 캐속
            if event.key == pygame.K_o:
                판2이동 -= 캐속
            if event.key == pygame.K_k:
                판2이동 += 캐속

        if event.type == pygame.KEYUP: # 키를 땠을때 이동X
            if event.key == pygame.K_w or event.key == pygame.K_s:
                판1이동 = 0

            if event.key == pygame.K_o or event.key == pygame.K_k:
                판2이동 = 0
      
        if 판_1_y좌표 <= 0:
            판_1_y좌표 = 1
        elif 판_1_y좌표 >= 화면크기_세로 - 판1_세로:
            판_1_y좌표 = 화면크기_세로 - 판1_세로 - 판1이동
        if 판_2_y좌표 <= 0:
            판2이동 = 0
            판_2_y좌표 = 1
        elif 판_2_y좌표 >= 화면크기_세로 - 판2_세로:
            판2이동 = 0
            판_2_y좌표 = 화면크기_세로 - 판2_세로 - 1

    # 충돌처리를 위한 위치 정보 업데이트

    판_1_y좌표 += 판1이동
    판_2_y좌표 += 판2이동
    공_x좌표 += 공_x속도
    공_y좌표 += 공_y속도

    판위치1 = 판1.get_rect()
    판위치1.right = 판_1_x좌표 + 판1_가로
    판위치1.top = 판_1_y좌표

    판위치2 = 판2.get_rect()
    판위치2.left = 판_2_x좌표
    판위치2.top = 판_2_y좌표

    공위치 = 공.get_rect()
    공위치.right = 공_x좌표 + 공_가로
    공위치.left = 공_x좌표
    공위치.top = 공_y좌표

    if 판위치1.colliderect(공위치):
        공_x속도 = 공_x속도 * -1
        if 플마판 == True:
            플마판 = False
        else:
            플마판 = True

    if 판위치2.colliderect(공위치):
        공_x속도 = 공_x속도 * -1
        if 플마판 == True:
            플마판 = False
        else:
            플마판 = True

    if 공_x좌표 <= 0 or 공_x좌표 >= 화면크기_가로 - 공_가로:
        공_x속도 = 공_x속도 * -1
        if 공_x좌표 <= 0:
            파_현점수 = 파_현점수 + 1
        else:
            빨_현점수 = 빨_현점수 + 1
        공_x좌표 = 화면크기_가로 / 2 - 공_가로 / 2
        공_y좌표 = 화면크기_세로 / 2 - 공_세로 / 2
        공_x속도 = 캐속 / 2
        플마판 = True
        pygame.time.delay(1000)

    if 공_y좌표 <= 0 or 공_y좌표 >= 화면크기_세로 - 공_세로:
        공_y속도 = 공_y속도 * -1

    if 빨_현점수 == 5 or 파_현점수 == 5:
        판_1_y좌표 = 화면크기_세로 / 2 - 판1_세로 / 2
        판_2_y좌표 = 화면크기_세로 / 2 - 판2_세로 / 2
        진행여부 = False
        승패 = True

    화면.fill((25, 25, 25)) # R, G, B 값으로도 지정가능
    # 화면.blit(배경, (0, 0)) # 배경그리기 단, 파이썬은 계속 그려주어야함
    화면.blit(판1, (판_1_x좌표, 판_1_y좌표))
    화면.blit(판2, (판_2_x좌표, 판_2_y좌표))
    화면.blit(공, (공_x좌표, 공_y좌표))

    경과시간 = int(((pygame.time.get_ticks()) - 시작시간) / 1000) # ms단위기에 1000을 나누어 초 단위로 표시
    타이머 = 게임폰트.render(str(경과시간), True, (0, 255, 0))
    # 글자 = 폰트변수.render((출력할 글자), True, (색깔))

    빨_점수 = 게임폰트.render(str(빨_현점수), True, (255, 0, 0))
    파_점수 = 게임폰트.render(str(int(파_현점수)), True, (0, 0, 255))

    화면.blit(상판, (0, (0)))
    화면.blit(하판, (0, 화면크기_세로 - 하판_세로))

    if 경과시간 <= 5:
        조작키설명_w = 게임폰트.render("w", True, (255, 255, 255))
        조작키설명_s = 게임폰트.render("s", True, (255, 255, 255))
        조작키설명_o = 게임폰트.render("o", True, (255, 255, 255))
        조작키설명_k = 게임폰트.render("k", True, (255, 255, 255))
        화면.blit(조작키설명_w, (100, 110))
        화면.blit(조작키설명_s, (100, 370))
        화면.blit(조작키설명_o, (800, 110))
        화면.blit(조작키설명_k, (800, 370))

    화면.blit(타이머, (화면크기_가로 / 2 - 30, 10)) # 425 화면크기_가로 / 2 - 30
    화면.blit(빨_점수, (화면크기_가로 / 4, 10))
    화면.blit(파_점수, (화면크기_가로 / 2 + 화면크기_가로 / 4 - 30, 10))

    if 플마판 == True:
        공_x속도 = 공_x속도 + 캐속 / 1000
    else:
        공_x속도 = 공_x속도 - 캐속 / 1000
    
    pygame.display.update() # 이걸로 계속그림

pygame.time.delay(1000) # 일시정지 역할을하며 단위는 밀리세컨드 (원하는시간 초단위로 환산후 곱하기 1000)

if 승패 == True:
    if 빨_현점수 == 5:
        승리자 = 게임폰트.render("RED WIN", True, (255, 0, 0))
        화면.blit(승리자, (화면크기_가로 / 4, 화면크기_세로 / 2 - 10))
    elif 파_현점수 == 5:
        승리자 = 게임폰트.render("BLUE WIN", True, (0, 0, 255))
        화면.blit(승리자, (화면크기_가로 / 2 + 화면크기_가로 / 4 - 30, 화면크기_세로 / 2 - 10))
    pygame.display.update()
    pygame.time.delay(4000)

pygame.quit() # 게임종료
### 완성 ### 수정완료(판 정중앙후 게임 결과) ###