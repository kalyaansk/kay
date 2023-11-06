import pygame
import random
pygame.init()
from sys import exit


#game variables
WIDTH,HEIGHT=600,600
fps = 60
clock = pygame.time.Clock() 
running = False
screen1 = pygame.display.set_mode((WIDTH,HEIGHT))
title_font =pygame.font.Font('/System/Library/Fonts/Optima.ttc',56)
title_font1 =pygame.font.Font('/System/Library/Fonts/Supplemental/STIXTwoMath.otf',26)
rows = 6
cols = 8 
correct =[[0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0]]

attemps =0
matches =0
best_score = 0
game_over = False
            
new_board = True
options_list=[]
spaces=[]
used =[]
first_guess = False
second_guess = False
first_guess_num = 0
second_guess_num = 0

#intro screen
  
intro_surf = pygame.image.load('/Users/kk/Desktop/class11/computer science/PROJECTTT/pygame /memory game/intro_surf/Ma Belle Clit.jpg').convert()
intro_surf_rect = intro_surf.get_rect(topleft = (-50,-20))


title_font2 =pygame.font.Font('/System/Library/Fonts/Supplemental/AmericanTypewriter.ttc',50)
title_font3 =pygame.font.Font('/System/Library/Fonts/Supplemental/AmericanTypewriter.ttc',22)

title_surf1 = title_font2.render('Tap',True,('White')).convert_alpha()
title_surf1_rect = title_surf1.get_rect(topleft = (323, 64))

title_surf2 = title_font2.render('Tiles',True,('White')).convert_alpha()
title_surf2_rect = title_surf2.get_rect(topleft = (420,69))

playtext_surf = title_font3.render('Click to play ',True,('white')).convert_alpha()
playtext_surf_rect = playtext_surf.get_rect(bottomleft =(386, 140))




#functions


def generate_board():
    global options_list
    global spaces
    global used

    for item in range (rows*cols//2):
        options_list.append(item)

    for item in range(rows*cols):
        piece = options_list[random.randint(0,len(options_list)-1)]
        spaces.append(piece)
    
        if piece in used:
            used.remove(piece)
            options_list.remove(piece)
        else:
            used.append(piece)






def draw_backgrounds():
    top_menu = pygame.draw.rect(screen1,'Black',[0,0,WIDTH,HEIGHT-500],0,0)#the last befor 0 is for thickness of border nd the last one is for radius
 
    title_font_surf = title_font.render('tap tiles',True,('White')).convert_alpha()
    title_font_surf_rect = title_font_surf.get_rect(topleft = (10,20))
    screen1.blit(title_font_surf,title_font_surf_rect)
 
    broard_space = pygame.draw.rect(screen1,'gray50',[0,HEIGHT-500,WIDTH,HEIGHT-100],0,0)
    bottom_menu = pygame.draw.rect(screen1,'Black',[0,HEIGHT-100,WIDTH,HEIGHT-500],0,0)

    restart_button = pygame.draw.rect(screen1, 'grey50', [10, HEIGHT - 80, 200, 70], 0, 10)
    restart_text = title_font.render('Restart', True, 'White')
    screen1.blit (restart_text, (10, 520))
    score_text = title_font1. render (f'Current Turns: {(attemps)}', True, 'White')
    screen1.blit(score_text, (350, 520))
    best_text = title_font1. render (f'Previous Best: {(best_score)}', True, 'White')
    screen1.blit (best_text, (350, 560))

    return restart_button
 

def draw_board():
    global rows
    global cols
    global correct
    boord_list = []
    for i in range(cols):
        for j in range(rows):
            piece = pygame.draw.rect(screen1,'White',[i*75+12,j*65+112,50,50],0,4)#50,50 is the size of the rectangle, and we are padding
            boord_list.append(piece)
            '''piece_text = title_font1.render(f'{spaces[i*rows+j]}',True,'grey50')#formated string f{} cause we are useing variables for name 
            screen1.blit(piece_text,(i*75+18,j*65+120))'''


#here we r jst drawing a green box for correct value
    for r in range(rows):
        for c in range(cols):
            if correct[r][c]==1:
                pygame.draw.rect(screen1,'Green',[c*75+10,r*65+110,54,54],3,4)
                piece_text = title_font1.render(f'{spaces[c*rows+r]}',True,'Black')#formated string f{} cause we are useing variables for name 
                screen1.blit(piece_text,(c*75+18,r*65+120))    

    return boord_list

def check_guesses(first,second):
    global spaces
    global correct
    global attemps
    global matches
    if spaces [first] == spaces[second]:
        col1 = first // rows #first is the block you have clicked so in the first colomn there are 0to5 so 0 to 5 divided by 6 is 0 so when can find in which column the clicked box is in
        col2 = second // rows
        row1 = first - (col1 * rows)
        row2 = second - (col2 * rows)
        if correct[row1][col1] == 0 and correct[row2][col2]==0:
            correct[row1][col1] = 1
            correct[row2][col2] = 1
            attemps += 1
            matches += 1
            
    else:
        attemps += 1        
   

#intro loop

A1=True
while A1:
    for event in pygame.event.get(): #pygame.event.get will get us all the events 
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()#we are using this because when the pygame gets quit the loop still runs and exicutes the commands given below as off to exit the while loop we are using exit it is like a break statement but we are not using break cause exit is a proper way to exit a statement 
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)
        if event.type == pygame.MOUSEBUTTONDOWN:
            running = True 
            A1 = False
        screen1.blit(intro_surf,intro_surf_rect)
        screen1.blit(title_surf1,title_surf1_rect)
        screen1.blit(title_surf2,title_surf2_rect)
        screen1.blit(playtext_surf,playtext_surf_rect)

        pygame.display.update()

        clock.tick(60)
        



#mainloop

while running:
    clock.tick(fps)
    screen1.fill('White')
    if new_board:
        generate_board()
        new_board = False

    restart = draw_backgrounds()
    board = draw_board()

    if first_guess and second_guess:
        check_guesses(first_guess_num,second_guess_num)
        pygame.time.delay(1000)#this will freeze the opened box in milli secs
        first_guess = False
        second_guess = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range (len(board)):
                button = board[i]#i is the position of box like 1 2 3 4 in column wise
                if not game_over:
                    if button.collidepoint(event.pos) and not first_guess:
                        first_guess = True
                        first_guess_num = i
                
                    if button.collidepoint(event.pos) and not second_guess and first_guess and i != first_guess_num:
                        second_guess = True
                        second_guess_num = i
                        
            if restart.collidepoint(event.pos):
                options_list = []
                used = []
                spaces =[] 
                new_board = True
                attemps = 0
                matches = 0
                first_guess = False
                second_guess = False
                correct=[[0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0]]
                game_over = False

        #this is used to show the boxs
    if first_guess:
        piece_text = title_font1.render(f'{spaces[first_guess_num]}',True,'Blue')#formated string f{} cause we are useing variables for name 
        location = (first_guess_num // rows * 75 +18,(first_guess_num - (first_guess_num // rows * rows))*65+120)
        screen1.blit(piece_text,(location)) 
    if second_guess:
        piece_text = title_font1.render(f'{spaces[second_guess_num]}',True,'Blue')#formated string f{} cause we are useing variables for name 
        location = (second_guess_num // rows * 75 +18,(second_guess_num - (second_guess_num // rows * rows))*65+120)
        screen1.blit(piece_text,(location)) 

    pygame.display.update()

    
    if matches == rows*cols // 2:
            if best_score > attemps or best_score == 0:
                best_score = attemps
            game_over = True
            running = False

    

            
            clock.tick(60)    
            pygame.display.update()
            
            
            
            
while game_over:
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            exit()  

                game_over_draw = pygame.draw.rect(screen1,'azure3',[0,235,WIDTH,100],0,)
                game_over_text = title_font2.render('GAME OVER',True,'Black').convert_alpha()
                screen1.blit(game_over_text,(141, 256))
                score_text = title_font1. render (f'Total turns: {(attemps-1)}', True, 'White')
                screen1.blit(score_text, (224, 310))

            


                
                clock.tick(60)    
                pygame.display.update()

        


#winner = pygame.draw.rect(screen, 'gray50', [10, HEIGHT - 300, WIDTH - 20, 801], 0, 5)
#winner_text = title_font. render(f'You Won in {attemps} moves!', True,'White')
    

    

    


