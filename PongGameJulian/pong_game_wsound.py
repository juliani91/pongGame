import pygame,sys
import random
import pygame.mixer
from pygame.locals import*

pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()
font = pygame.font.SysFont("arial",50)
screen = pygame.display.set_mode((600,400),0,32)
pygame.display.set_caption("PONG GAME")

#creating bars as rectangle for later collides.
back = pygame.Surface((600,400))
background = back.convert()

bar = pygame.Surface((10,60))
bar1 = bar.convert()
bar1.fill((0,0,255))
bar2 = bar.convert()
bar2.fill((0,0,255))
bar1Rect = pygame.Rect((5,200),(5,60))
bar2Rect = pygame.Rect((585,200),(5,60))


#circle rect obj and speed for bars and circle

circ_sur = pygame.Surface((10,10))
circle = pygame.draw.circle(circ_sur,(255,0,0),(15/2,15/2),15/2)
circle = circ_sur.convert()
circle.fill((255,0,0))
circleRect = pygame.Rect((300,120),(20,20))

#Frame rects for later circle collapse
frame_sur = pygame.Surface((598,398))
frame_goal = pygame.draw.rect(screen,(0,0,255),Rect((595,0),(595,395)),2)
frame_goal2 = pygame.draw.rect(screen,(0,0,255),Rect((600,0),(600,400)),1)
frame_goal = frame_sur.convert()
frame_goal2 = frame_sur.convert()



frameRect = pygame.Rect((613,0),(200,400))
frameRect2 = pygame.Rect((-595,0),(595,395))

circle_speed = [3,3]
bar_speed = [2,2]

#bar positions
bar1_movex = 0
bar1_movey = 0
bar2_movex = 0
bar2_movey = 0

bar1_score , bar2_score = 0,0

#Sounds
hit = pygame.mixer.Sound("hit.wav")
point = pygame.mixer.Sound("point.wav")
#main loop game

while True:
    for e in pygame.event.get():
        if e.type == QUIT:
            sys.exit()
        if e.type == KEYDOWN:    
            if e.key == K_ESCAPE:
                sys.exit()
            if e.key == K_q:
                bar1_movey = -5
            if e.key == K_a:
                bar1_movey = +5
            if e.key == K_o:
                bar2_movey = -5
            if e.key == K_l:
                bar2_movey = +5
        if e.type == KEYUP:
            if e.key == K_q:
                bar1_movey = 0
            if e.key == K_a:
                bar1_movey = 0
            if e.key == K_o:
                bar2_movey = 0
            if e.key == K_l:
                bar2_movey = 0

    score1 = font.render(str(bar1_score), False,(0,255,0))
    score2 = font.render(str(bar2_score), False,(0,255,0))
        
    #Displaying the rect objects
    screen.blit(background,(0,0))
    screen.blit(bar1,bar1Rect)
    screen.blit(bar2,bar2Rect)
    screen.blit(circle,circleRect)
    screen.blit(frame_goal,frameRect)
    screen.blit(frame_goal2,frameRect2)
    screen.blit(score1,(250.,348.))
    screen.blit(score2,(315.,348.))

    #Drawing lines to the borders and the middle
    frame = pygame.draw.rect(screen,(255,255,255),Rect((1,1),(600,1)),2)
    frame2 = pygame.draw.rect(screen,(255,255,255),Rect((1,397),(600,1)),2)
    middleFrame = pygame.draw.rect(screen,(255,255,255),Rect((300,1),(1,397)),2)
    
    
    #Moving the bars
    time_passed = clock.tick(1000)
    time_seconds = time_passed/1000.0
    bar1_movey += time_seconds*bar1_movey
    bar2_movey += time_seconds*bar2_movey

    bar1Rect = bar1Rect.move(bar1_movex,bar1_movey)
    bar2Rect = bar2Rect.move(bar2_movex,bar2_movey)

    #bars out of bounds
    
    if bar1Rect.top <= 0:
        bar1Rect.move_ip(0,5)
    elif bar1Rect.bottom >= 400:
        bar1Rect.move_ip(0,-5)
    if bar2Rect.top <= 0:
        bar2Rect.move_ip(0,5)
    elif bar2Rect.bottom >= 400:
        bar2Rect.move_ip(0,-5)
    
    #circle moving in screen
    
    
    circleRect = circleRect.move(circle_speed)
    if circleRect.top < 0 or circleRect.bottom > 400:
        circle_speed[1] = -circle_speed[1]
        hit.play()
    if circleRect.colliderect(bar1Rect) or circleRect.colliderect(bar2Rect):
        circle_speed[0] = -circle_speed[0]
        hit.play()
        

    #Circle collapse with goal frames, restart position
    if circleRect.colliderect(frameRect):
        pygame.time.delay(1500)
        point.play()
        bar1_score += 1
        circleRect.center = (300,120)
    elif circleRect.colliderect(frameRect2):
        pygame.time.delay(1500)
        point.play()
        bar2_score += 1
        circleRect.center = (300,300)        
    
    pygame.display.update()
            
    
    

