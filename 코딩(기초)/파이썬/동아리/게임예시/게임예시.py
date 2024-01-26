import os
import pygame
import random 

pygame.init()

화면크기_가로 = 880
화면크기_세로 = 480
화면 = pygame.display.set_mode((화면크기_가로, 화면크기_세로))
pygame.display.set_caption("게임제목")

이미지_폴더_위치 = os.path.dirname(__file__)
이미지_위치 = os.path.join(이미지_폴더_위치, "게임 이미지")

캐릭터 = pygame.image.load(os.path.join(이미지_위치, "캐릭터.png"))
캐릭터_크기 = 캐릭터.get_rect().size
캐릭터_가로 = 캐릭터_크기[0]
캐릭터_세로 = 캐릭터_크기[1]

적 = pygame.image.load(os.path.join(이미지_위치, "적.png"))
적_크기 = 적.get_rect().size
적_가로 = 적_크기[0]
적_세로 = 적_크기[1]

게임폰트 = pygame.font.Font(None, 30)

캐릭터_y좌표 = (화면크기_세로 / 2) - (캐릭터_세로 / 2)
캐릭터_x좌표 = (화면크기_가로 / 2) - (캐릭터_가로 / 2)

프레임속도 = 50
프레임 = pygame.time.Clock()

캐릭터_x이동 = 0
캐릭터_y이동 = 0
캐릭터_이동_속도 = 1

적_x좌표 = 0
적_y좌표 = 0
적_x이동 = 3
적_y이동 = 3

정립 = False

def 적_분열(적_x좌표_임시, 적_y좌표_임시, 적_y이동_임시):
    global 진행여부
    정립 = False
    if 정립 != True:
        적 = pygame.image.load(os.path.join(이미지_위치, "적.png"))
        적_크기 = 적.get_rect().size
        적_가로 = 적_크기[0]
        적_세로 = 적_크기[1]
        적_x좌표 = 적_x좌표_임시
        적_y좌표 = 적_y좌표_임시
        적_x이동 = 3
        적_y이동 = 적_y이동_임시
        정립 = True
        
    while 진행여부:
        if 적_x좌표 < 0:
            적_x좌표 = 0 
            적_x이동 *= -1
        elif 적_x좌표 > 화면크기_가로 - 적_가로:
            적_x좌표 = 화면크기_가로 - 적_가로
            적_x이동 *= -1
        
        if 적_y좌표 < 0:
            적_y좌표 = 0 
            적_y이동 *= -1
        elif 적_y좌표 > 화면크기_세로 - 적_세로:
            적_y좌표 = 화면크기_세로 - 적_세로
            적_y이동 *= -1

        적_x좌표 += 적_x이동
        적_y좌표 += 적_y이동

        if 적_x좌표 < 0:
            적_x좌표 = 0 
            적_x이동 *= -1
        elif 적_x좌표 > 화면크기_가로 - 적_가로:
            적_x좌표 = 화면크기_가로 - 적_가로 - 1
            적_x이동 *= -1
            적_x좌표_임시 = 적_x좌표
            적_y좌표_임시 = 적_y좌표
            적_y이동_임시 = -1 * 적_y이동
            적_분열(적_x좌표_임시, 적_y좌표_임시, 적_y이동_임시)
        
        if 적_y좌표 < 0:
            적_y좌표 = 0 
            적_y이동 *= -1
        elif 적_y좌표 > 화면크기_세로 - 적_세로:
            적_y좌표 = 화면크기_세로 - 적_세로
            적_y이동 *= -1

        적_위치 = 적.get_rect()
        적_위치.right = 적_x좌표 + 적_가로
        적_위치.top = 적_y좌표

        if 캐릭터_위치.colliderect(적_위치):
            게임오버 = 게임폰트.render("game over", True, (0, 255, 0)) # 폰트변수.render(출력할 글자), True, (색깔)
            화면.blit(게임오버, (화면크기_가로 / 2 - 캐릭터_가로 / 2, 화면크기_세로 / 2 - 캐릭터_세로 / 2))
            pygame.display.update()
            pygame.time.delay(1500)
            진행여부 = False
        화면.blit(적, (적_x좌표, 적_y좌표))

진행여부 = True
while 진행여부:
    프레임_설정 = 프레임.tick(프레임속도)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            진행여부 = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                캐릭터_y이동 -= 10 * 캐릭터_이동_속도
            if event.key == pygame.K_s:
                캐릭터_y이동 += 10 * 캐릭터_이동_속도
            if event.key == pygame.K_a:
                캐릭터_x이동 -= 10 * 캐릭터_이동_속도
            if event.key == pygame.K_d:
                캐릭터_x이동 += 10 * 캐릭터_이동_속도

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                캐릭터_y이동 += 10 * 캐릭터_이동_속도
            if event.key == pygame.K_s:
                캐릭터_y이동 -= 10 * 캐릭터_이동_속도
            if event.key == pygame.K_a:
                캐릭터_x이동 += 10 * 캐릭터_이동_속도
            if event.key == pygame.K_d:
                캐릭터_x이동 -= 10 * 캐릭터_이동_속도
    
    캐릭터_y좌표 += 캐릭터_y이동
    캐릭터_x좌표 += 캐릭터_x이동

    if 캐릭터_x좌표 < 0:
        캐릭터_x좌표 = 0 
    elif 캐릭터_x좌표 > 화면크기_가로 - 캐릭터_가로:
        캐릭터_x좌표 = 화면크기_가로 - 캐릭터_가로
    
    if 캐릭터_y좌표 < 0:
        캐릭터_y좌표 = 0 
    elif 캐릭터_y좌표 > 화면크기_세로 - 캐릭터_세로:
        캐릭터_y좌표 = 화면크기_세로 - 캐릭터_세로

    캐릭터_위치 = 캐릭터.get_rect()
    캐릭터_위치.right = 캐릭터_x좌표 + 캐릭터_가로
    캐릭터_위치.top = 캐릭터_y좌표

    if 정립 == False:
        적_분열(0, 0, 3)
        정립 = True

    화면.fill((25, 25, 25))
    화면.blit(캐릭터, (캐릭터_x좌표, 캐릭터_y좌표))

    pygame.display.update()

pygame.quit()