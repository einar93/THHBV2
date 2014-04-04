from main import*
from globals import *

def drawScore(screen, score):
    font=pygame.font.Font(None,30)
    scoretext=font.render("Score: "+str(score), 1,(255,255,255))
    screen.blit(scoretext, (SCREENRECT.width*0.80, SCREENRECT.height*0.05))

def drawText(screen):
    
    500,440
    
    myfont = pygame.font.SysFont("Arial", 20)
    restart = myfont.render("R to Restart!", 1, (255,0,0))
    screen.blit(restart, (SCREENRECT.width*0.05, SCREENRECT.height*0.88))
    esc = myfont.render("ESC to Exit!", 1, (255,0,0))
    screen.blit(esc, (SCREENRECT.width*0.05, SCREENRECT.height*0.93))
    theme1 = myfont.render("Press 1 for forest theme", 1, (255,0,0))
    screen.blit(theme1,(SCREENRECT.width*0.25, SCREENRECT.height*0.88))
    theme2 = myfont.render("Press 2 for StarWars theme",1,(255,0,0))
    screen.blit(theme2,(SCREENRECT.width*0.25, SCREENRECT.height*0.93))
    mute = myfont.render("M to mute!",1,(255,0,0))
    screen.blit(mute,(SCREENRECT.width*0.05, SCREENRECT.height*0.83)) 

def drawTime(screen, time):
    font=pygame.font.Font(None,30)
    timetext=font.render("Time: "+str(time), 1,(255,255,255))
    screen.blit(timetext, (SCREENRECT.width*0.80, SCREENRECT.height*0.9))
   

def drawHighScore(screen, score_lst):
    score_lst = score_lst[::-1] #reverse the list
    offset = 30
    font=pygame.font.Font(None,30)
    count = 0
    
    scoretext=font.render("High Scores:", 1,(255,255,255))
    screen.blit(scoretext, (SCREENRECT.width*0.80, SCREENRECT.height*0.29))
    
    for i in range(len(score_lst)):
        if i >= 3 : break
        scorevalue = font.render(str(score_lst[i][2]), 1,(255,255,255))
        screen.blit(scorevalue, (SCREENRECT.width*0.80, SCREENRECT.height*0.36+i*offset))

