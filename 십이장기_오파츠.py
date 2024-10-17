import pygame as pg
import sys
pg.init()
pg.font.init()
game_font = pg.font.SysFont('ComicSansMS', 32)

BLUE  = (  0,   0, 255)
BLACK = (  0,   0,   0)
GREEN = (  0, 255,   0)
RED   = (255,   0,   0)

screen = pg.display.set_mode((900, 800))
clock = pg.time.Clock()

왕 = pg.image.load('./왕.jpg')
왕2 = pg.transform.rotate(pg.image.load('./왕2.jpg'),180)

자 = pg.image.load('./자.jpg')
자2 = pg.transform.rotate(자,180)

자뒷면 = pg.image.load('./자뒷면.jpg')
자뒷면2 = pg.transform.rotate(자뒷면,180)

장 = pg.image.load('./장.jpg')
장2 = pg.transform.rotate(장,180)

상 = pg.image.load('./상.jpg')
상2 = pg.transform.rotate(상,180)

#왕 = 1, 왕2 = 2
#장 = 3, 장2 = 4
#상 = 5, 상2 = 6
#자 = 7, 자2 = 8
#자뒷면 = 9, 자뒷면2 = 10
MAP = [[장2,왕2,상2],[0,자2,0],[0,자,0],[상,왕,장]]
MAP2 = [[4,2,6],[0,8,0],[0,7,0],[5,1,3]]

GT = []
GT2 = []
RT = []
RT2 = []

pos_y=-99
pos_x=-99
pos_Y=-99
pos_X=-99
flag = [False,-99,-99]
FLAG = [False,-1]
Gwin = False
Rwin = False
win = False
Rcnt = 0
Gcnt = 0
attack = True #True면 빨강팀 공격

text_surface = game_font.render('Your turn', True, (255, 0, 0))
win_text = game_font.render('Your winner!!!', True, (255, 0, 0))

TIME_LIMIT = 10
time_remaining = TIME_LIMIT*30

time_remaining_text_surface = game_font.render(str((time_remaining*10//30)/10),True,(255,255,255))

time_bar_surface = pg.Surface(((time_remaining/(TIME_LIMIT*30)*300), 10))
time_point_surface = pg.Surface((20,20),flags=pg.SRCALPHA)

time_remaining_text_rect = time_remaining_text_surface.get_rect()

time_bar_rect = pg.draw.rect(time_bar_surface,(255,255,255),(0,0,(time_remaining/(TIME_LIMIT*30))*300, 10))
time_point_rect = pg.draw.circle(time_point_surface,(255,0,0),(10,10),10)

time_remaining_text_rect.center = (152,50)

time_bar_rect.midleft = (2,50)
time_point_rect.center = (152+(time_remaining/(TIME_LIMIT*30)-0.5)*300,50)

def scope(y1, x1, y2, x2):
    yy=y2-y1
    xx=x2-x1
    if(y1==-99): return False
    n=MAP2[y1][x1]
    if(n==1 or n==2):
        if(yy>=-1 and yy<=1 and xx>=-1 and xx<=1): return True
        else: return False
    elif(n==3 or n==4):
        if((yy==0 and xx==1) or (yy==1 and xx==0) or (yy==0 and xx==-1) or (yy==-1 and xx==0)): return True
        else: return False
    elif(n==5 or n==6):
        if((yy==1 and xx==1) or (yy==-1 and xx==-1) or (yy==-1 and xx==1) or (yy==1 and xx==-1)): return True
        else: return False
    elif(n==7):
        if(yy==-1 and xx==0): return True
        else: return False
    elif(n==8):
        if(yy==1 and xx==0): return True
        else: return False
    elif(n==9):
        if(not((yy==1 and xx==-1) or (yy==1 and xx==1)) and yy>=-1 and yy<=1 and xx>=-1 and xx<=1): return True
        else: return False
    elif(n==10):
        if(not((yy==-1 and xx==-1) or (yy==-1 and xx==1)) and yy>=-1 and yy<=1 and xx>=-1 and xx<=1): return True
        else: return False
    

while True:
    screen.fill((255,204,102))

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
            break
        if event.type == pg.MOUSEBUTTONUP:
            mouse_pos=pg.mouse.get_pos()
            if((mouse_pos[1]-75.0)/152>=0 and (mouse_pos[0]-225.0)/152>=0 and (mouse_pos[1]-75.0)/152<4 and (mouse_pos[0]-225.0)/152<3):
                pos_y = (int)((mouse_pos[1]-75.0)/152)
                pos_x = (int)((mouse_pos[0]-225.0)/152)

                if(FLAG[0] and MAP2[pos_y][pos_x]==0):
                    if(attack and pos_y!=0):
                        MAP2[pos_y][pos_x]=RT2[FLAG[1]]
                        MAP[pos_y][pos_x]=RT[FLAG[1]]
                        del RT2[FLAG[1]]
                        del RT[FLAG[1]]
                        attack=1-attack

                        for i in range(3):
                            if(MAP2[0][i]==1 and Rcnt==1):
                                Rwin = True
                                win = True
                                Rcnt=0
                            if(MAP2[0][i]==1):
                                Rcnt+=1
                                
                            if(MAP2[3][i]==2 and Gcnt==1):
                                Gwin = True
                                win = True
                                Gcnt=0
                            if(MAP2[3][i]==2):
                                Gcnt+=1
                                
                    elif(not attack and pos_y!=3):
                        MAP2[pos_y][pos_x]=GT2[FLAG[1]]
                        MAP[pos_y][pos_x]=GT[FLAG[1]]
                        del GT2[FLAG[1]]
                        del GT[FLAG[1]]
                        attack=1-attack

                        for i in range(3):
                            if(MAP2[0][i]==1 and Rcnt==1):
                                Rwin = True
                                win = True
                                Rcnt=0
                            if(MAP2[0][i]==1):
                                Rcnt+=1
                                
                            if(MAP2[3][i]==2 and Gcnt==1):
                                Gwin = True
                                win = True
                                Gcnt=0
                            if(MAP2[3][i]==2):
                                Gcnt+=1

                if(flag[0] and (MAP2[pos_y][pos_x]==0 or (MAP2[pos_y][pos_x]-MAP2[flag[1]][flag[2]])%2==1) and scope(flag[1], flag[2], pos_y, pos_x)):
                        if(MAP[pos_y][pos_x]!=0):
                            MAP[pos_y][pos_x] = pg.transform.rotate(MAP[pos_y][pos_x],180)
                            if(attack):
                                RT.append(MAP[pos_y][pos_x])
                                RT2.append(MAP2[pos_y][pos_x]-1)
                            else:
                                GT.append(MAP[pos_y][pos_x])
                                GT2.append(MAP2[pos_y][pos_x]+1)
                        MAP2[pos_y][pos_x]=MAP2[flag[1]][flag[2]]
                        MAP2[flag[1]][flag[2]]=0
                        MAP[pos_y][pos_x]=MAP[flag[1]][flag[2]]
                        MAP[flag[1]][flag[2]]=0
                        attack=1-attack

                        for i in range(3):
                            if(MAP2[0][i]==1 and Rcnt==1):
                                Rwin = True
                                win = True
                                Rcnt=0
                            if(MAP2[0][i]==1):
                                Rcnt+=1
                                
                            if(MAP2[3][i]==2 and Gcnt==1):
                                Gwin = True
                                win = True
                                Gcnt=0
                            if(MAP2[3][i]==2):
                                Gcnt+=1
                        
                        time_remaining = TIME_LIMIT*30
                
                if(MAP2[pos_y][pos_x]!=0 and MAP2[pos_y][pos_x]%2-attack==0):
                        
                    flag = [True, pos_y, pos_x]
                    FLAG[0] = False
                else:
                    pos_y=-99
                    pos_x=-99
                    flag = [False, pos_y, pos_x]
                    FLAG[0] = False
            else:
                pos_y=-99
                pos_x=-99
                flag = [False, pos_y, pos_x]
                FLAG[0] = False
            
            if(attack):
                for i in range(len(RT)):
                    if(mouse_pos[0]>=720 and mouse_pos[0]<=870 and mouse_pos[1]>=75+152*i and mouse_pos[1]<=225+152*i):
                        pos_X=720
                        pos_Y=75+152*i
                        FLAG = [True,i]
            else:
                for i in range(len(GT)):
                    if(mouse_pos[0]>=30 and mouse_pos[0]<=180 and mouse_pos[1]>=75+152*i and mouse_pos[1]<=225+152*i):
                        pos_X=30
                        pos_Y=75+152*i
                        FLAG = [True,i]
                    
    if(FLAG[0]): pg.draw.rect(screen, BLUE, [pos_X,pos_Y,150,150],5)
    elif(pos_x>=0 and pos_y>=0):
        pg.draw.rect(screen, BLUE, [225+152*pos_x,75+152*pos_y,150,150],5)
        FLAG[0] = False

    if(not win):
        if(attack): screen.blit(text_surface,(380,700))
        else: screen.blit(text_surface,(380,15))
    else:
        if(Gwin): screen.blit(win_text,(380,15))
        else: screen.blit(win_text,(380,700))

    if(not win): time_remaining-=1

    if(time_remaining<=0):
        if(attack):
            Gwin = True
            win = True
        else:
            Rwin = True
            win = True


    time_remaining_text_rect = time_remaining_text_surface.get_rect()
    time_remaining_text_surface = game_font.render(str((time_remaining*10//30)/10),True,(255,255,255))

    time_bar_rect.width = int(time_remaining / (TIME_LIMIT*30)*300)
    time_point_rect.center = (152 + (time_remaining / (TIME_LIMIT*30) - 0.5) * 300, 50)

    surfaces = [time_remaining_text_surface,time_bar_surface,time_point_surface]
    rects = [time_remaining_text_rect, time_bar_rect, time_point_rect]
    for i in range(len(rects)):
        screen.blit(surfaces[i],rects[i])

    for i in range(3):
        if(MAP2[0][i]==7):
            MAP2[0][i]=9
            MAP[0][i]=자뒷면
        if(MAP2[3][i]==8):
            MAP2[3][i]=10
            MAP[3][i]=자뒷면2
    
    for i in range(4):
        for j in range(3):
            if(i==0):
                pg.draw.rect(screen, GREEN, [225+152*j,75+152*i,150,150],0)
            elif(i==3):
                pg.draw.rect(screen, RED, [225+152*j,75+152*i,150,150],0)
            pg.draw.rect(screen, BLACK, [225+152*j,75+152*i,150,150],2)

            if(MAP[i][j]!=0): screen.blit(MAP[i][j],(231+152*j,81+152*i))

    for i in range(len(GT)):
        if(GT2[i]==2):
            Gwin = True
            win = True
        if(GT2[i]==10):
            GT2[i]=8
            GT[i]=자2
        pg.draw.rect(screen,BLACK, [30,75+152*i,150,150],2)
        screen.blit(GT[i],(36,81+152*i))

    for i in range(len(RT)):
        if(RT2[i]==1):
            Rwin = True
            win = True
        if(RT2[i]==9):
            RT2[i]=7
            RT[i]=자
        pg.draw.rect(screen,BLACK, [720,75+152*i,150,150],2)
        screen.blit(RT[i],(726,81+152*i))

    pg.display.flip()
    clock.tick(30)
