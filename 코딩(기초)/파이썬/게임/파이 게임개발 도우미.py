import os # 파일위치 확인하기
import pygame # 파이게임 불러오기
pygame.init() # 초기화 (필수)
화면크기_가로 = 880 # 1540 (전체화면 가로)
화면크기_세로 = 480 # 805 (전체화면 세로)
화면 = pygame.display.set_mode((화면크기_가로, 화면크기_세로)) # 화면설정
pygame.display.set_caption("게임제목") # 타이틀(제목)설정

# 한번만 해도 됨                                                                                               #
이미지_폴더_위치 = os.path.dirname(__file__) # 현재 폴더 위치 반환
이미지_위치 = os.path.join(이미지_폴더_위치, "캐릭터 이미지가 있는 폴더이름") # 캐릭터 이미지가 있는 폴더 위치 반환
#                                                                                                             #
캐릭터 = pygame.image.load(os.path.join(이미지_위치, "캐릭터 파일(이미지) 이름.파일 형식(대부분 png)"))
캐릭터_크기 = 캐릭터.get_rect().size # 이미지 크기를 구해옴
캐릭터_가로 = 캐릭터_크기[0] # 캐릭터의 가로크기
캐릭터_세로 = 캐릭터_크기[1] # 캐릭터의 세로크기  ### 캐릭터가 바닥위에 있게하기위해
충돌체 = 0

# 지워도                                                                                             #
바닥 = pygame.image.load(os.path.join(이미지_위치, "바닥 파일(이미지) 이름.파일 형식(대부분 png)"))
바닥_크기 = 바닥.get_rect().size
바닥_세로 = 바닥_크기[1] # 캐릭터가 바닥위에 있게하기위해
# 됨                                                                                                 #

캐릭터_y좌표 = 화면크기_세로 - 캐릭터_세로 - 바닥_세로 # 바닥위 # 위치설정은 알아서
캐릭터_x좌표 = (화면크기_가로 / 2) - (캐릭터_가로 / 2) # 정중앙
게임폰트 = pygame.font.Font(None, 30) # 변수 설정 = 폰트 생성(사용 폰트, 크기)
캐릭터_x이동 = 0
캐릭터_y이동 = 0
캐릭터_이동_속도 = 1

프레임속도 = 50
프레임 = pygame.time.Clock() # 으로 프레임을 설정하게 바꿀수있으며

진행여부 = True
while 진행여부:
    프레임_설정 = 프레임.tick(프레임속도) # 으로 프레임을 설정한다. (프레임수)
    for event in pygame.event.get(): # 게임개발중 필수 키보드 입력, 마우스조작등을 확인 
        if event.type == pygame.QUIT: # (창닫기 버튼을 눌렀을때) (FULLSCREEN = 전체화면)
            진행여부 = False # 게임종료

        if event.type == pygame.KEYDOWN: # KEYDOWN는 반드시 대문자로 (키보드 버튼을 눌렀을때)
            if event.key == pygame.K_SPACE: # K_원하는 키
                pass  # 캐릭터_x좌표 += 캐릭터_x이동

        if event.type == pygame.KEYUP: # 키를 땠을때 (이동X)
            if event.key == pygame.K_w or event.key == pygame.K_s or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                캐릭터_y이동 = 0

            if event.key == pygame.K_a or event.key == pygame.K_d or event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                캐릭터_x이동 = 0

        if event.type == pygame.MOUSEBUTTONDOWN: # MOUSEBUTTONDOWNd은 대문자로(마우스 클릭(좌, 우, 휠모두))
            print(pygame.mouse.get_pos()) # 마우스의 위치(좌표 (x, y) ) 출력
            print(event.button) # 1 = 좌클릭, 2 = 휠 클릭, 3 = 우 클릭, 4 = 휠 올리기, 5 = 휠 내리기

        if event.type == pygame.MOUSEBUTTONUP: # 마우스를 땠을때
            print("땠다!")

        if event.type == pygame.MOUSEMOTION: # 마우스를 움직일때
            print("움직이고 있다!")

    # 무기쪽, 공쪼개기는 https://www.youtube.com/watch?v=Dkx8Pl6QKW0&t=6210s을 보면 된다.
    # 속도를 줄일때 X이동 = -10 이라 가정 X이동 += 0.1 으로하면 점점느려짐. 부호가 다르면 반대로 (2차함수 참조)

    캐릭터_y좌표 += 캐릭터_y이동
    캐릭터_x좌표 += 캐릭터_x이동

    if 캐릭터_x좌표 < 0:
        캐릭터_x좌표 = 0
    elif 캐릭터_x좌표 > 화면크기_가로 - 캐릭터_가로:
        캐릭터_x좌표 = 화면크기_가로 - 캐릭터_가로
    
    if 캐릭터_y좌표 >= 화면크기_세로 - 바닥_세로:
        캐릭터_y좌표 = 화면크기_세로 - 캐릭터_세로 - 바닥_세로

    # 위치 정보 업데이트 
    캐릭터_위치 = 캐릭터.get_rect()
    캐릭터_위치.right = 캐릭터_x좌표 + 캐릭터_가로
    캐릭터_위치.top = 캐릭터_y좌표
    충돌체_위치 = 0

    if 캐릭터_위치.colliderect(충돌체_위치):
        print("충돌")

    화면.fill((25, 25, 25)) # R, G, B 값으로도 지정가능
    # 화면.blit(배경, (0, 0)) # 배경그리기 단, 파이썬은 계속 그려주어야함
    화면.blit(캐릭터, (캐릭터_x좌표, 캐릭터_y좌표))

    대충_알간 = 게임폰트.render("ㅇㅋ?", True, (255, 255, 255)) # 글자 = 폰트변수.render(출력할 글자), True, (색깔))

    화면.blit(대충_알간, (100, 110))

    pygame.display.update() # 이걸로 계속 업데이트

pygame.time.delay(1000) # 일시정지 역할을하며 단위는 밀리세컨드 (원하는시간 초단위로 환산후 곱하기 1000)

pygame.quit() # 게임종료