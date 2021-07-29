import pygame
import random
import time
import json
pygame.init()
WIDTH, HEIGHT = 800,600
FPS = 30
BLACK=(0,0,0)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)
WHITE=(255,255,255)
font = pygame.font.SysFont("Impact", 20)
font1 = pygame.font.SysFont("Impact", 72)
font2 = pygame.font.SysFont("Impact", 36)

FramePerSec = pygame.time.Clock()
Screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("snake")

brick = pygame.image.load("brickwall.png")
Score = 0
running = True
class eda():
    def __init__(self):
        self.radius = 5
        self.x = random.randint(100,600)
        self.y = random.randint(100,500)
    def draw(self):
        pygame.draw.circle(Screen, (255,0,0), [self.x, self.y], self.radius)

class Snake():
    def __init__(self, colour, element):
        self.radius = 5
        self.dx = 1
        self.dy = 0
        self.colour = colour
        self.element = element

    def move(self):
        for i in range(len(self.element) - 1, 0, -1):
            self.element[i][0] = self.element[i - 1][0]
            self.element[i][1] = self.element[i - 1][1]
        self.element[0][0] += self.dx
        self.element[0][1] += self.dy
    def draw(self):
        for i in self.element:
            pygame.draw.circle(Screen,self.colour,i,self.radius)

def menu():
    running1 = True
    choose = 0
    while running1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running1 = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    running1 = False
                    choose = 1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_2:
                    running1 = False
                    choose = 2
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_3:
                    running1 = False
                    choose = 3
        font1 = pygame.font.SysFont("Impact", 72)
        P = font1.render("Press", True, RED)
        P1 = font1.render("1-easy", True, RED)
        P2 = font1.render("2-medium", True, RED)
        P3 = font1.render("3-hard", True, RED)
        Screen.blit(P, (280, 30))
        Screen.blit(P1, (230, 130))
        Screen.blit(P2, (230, 230))
        Screen.blit(P3, (230, 335))
        pygame.display.flip()
        Screen.fill(WHITE)
    return choose

def game_over():
    Screen.fill((60, 170, 60))
    GAME_OVER = font1.render('GAME OVER!', True, (212, 75, 75))
    Screen.blit(GAME_OVER, (240,200))
    if choose == 1 and 2 and 3:
        my_score = font2.render('Total score: ' + str(Score), True, (255, 255, 255))
        Screen.blit(my_score, (300, 280))
    pygame.display.flip()
    time.sleep(3)
    pygame.quit()
    
def save_game():
    f = open("save", "w")
    if choose ==1 and 2 and 3:
        snake_save_game = {
            "Elements": snake1.element,
            "dx": snake1.dx,
            "dy": snake1.dy,
            "level": choose,
            "Score": Score
        }
    
    y = json.dumps(snake_save_game)
    f.write(y)
    f.close()

choose = menu()

pygame.display.flip()

food = eda()
#EASY
if choose == 1:
    F = [[100,100],[95,100],[90,100]]
    snake1 = Snake((0,0,255),F)
    while running:
        for i in range(len(snake1.element)-1):
            if snake1.element[0] == snake1.element[i+1]:
                game_over()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    save_game()
                    running = False
                if event.key == pygame.K_RIGHT and snake1.dx != -5:
                    snake1.dx = 5
                    snake1.dy = 0
                if event.key == pygame.K_LEFT and snake1.dx != 5:
                    snake1.dx = -5
                    snake1.dy = 0
                if event.key == pygame.K_UP and snake1.dy != 5:
                    snake1.dx = 0
                    snake1.dy = -5
                if event.key == pygame.K_DOWN and snake1.dy != -5:
                    snake1.dx = 0
                    snake1.dy = 5
        Screen.fill((0,204,255))
        snake1.draw()
        snake1.move()
        food.draw()
        FramePerSec.tick(FPS)
        for i in range(0, WIDTH, 30):
            Screen.blit(brick,(i,0))
            Screen.blit(brick,(i,570))
            Screen.blit(brick,(0,i))
            Screen.blit(brick,(770,i))
        for i in range(0, WIDTH, 30):
            Screen.blit(brick,(200,i-400))
            Screen.blit(brick,(600,i-400))
        for i in range(150, WIDTH, 30):
            Screen.blit(brick,(400,i))
            
        
        if snake1.element[0][1] > food.y-5 and snake1.element[0][1] <food.y+5:
            if snake1.element[0][0] > food.x-5 and snake1.element[0][0] < food.x+5:
                Score += 1
                food.x = random.randint(40,190) and random.randint(240,390) and random.randint(440,590) and random.randint(640,760)
                food.y = random.randint(40,140) and random.randint(410,560) 
                snake1.element.append([0,0])
    
        if (snake1.element[0][0] > 200 and snake1.element[0][0] < 230 and snake1.element[0][1] < 400 and snake1.element[0][1] > 0)or (snake1.element[0][0] > 600 and snake1.element[0][0] < 630 and snake1.element[0][1] < 400 and snake1.element[0][1] > 0)or (snake1.element[0][0] > 400 and snake1.element[0][0] < 430 and snake1.element[0][1] < 600 and snake1.element[0][1] > 150) or snake1.element[0][0] < 30 or snake1.element[0][0] > 770 or snake1.element[0][1] < 30 or snake1.element[0][1] > 570:
            game_over()
    
        SCORE = font.render("Score " + str(Score), True, (255, 180, 0))
        Screen.blit(SCORE, (70,70))
        pygame.display.flip()
        pygame.image.save(Screen, "zmeika.png")

#MEDIUM
elif choose == 2:
    F = [[50, 50], [55,170], [60,170]]
    snake1 = Snake((0,0,255), F)
    while running:
        for i in range(len(snake1.element)-1):
            if snake1.element[0] == snake1.element[i+1]:
                game_over()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    save_game()
                    running = False
                if event.key == pygame.K_RIGHT and snake1.dx != -6:
                    snake1.dx = 6
                    snake1.dy = 0
                if event.key == pygame.K_LEFT and snake1.dx != 6:
                    snake1.dx = -6
                    snake1.dy = 0
                if event.key == pygame.K_UP and snake1.dy != 6:
                    snake1.dx = 0
                    snake1.dy = -6
                if event.key == pygame.K_DOWN and snake1.dy != -6:
                    snake1.dx = 0
                    snake1.dy = 7
        Screen.fill((0,204,255))
        snake1.draw()
        snake1.move()
        food.draw()
        FramePerSec.tick(FPS)
        for i in range(0, WIDTH, 30):
            Screen.blit(brick,(i,0))
            Screen.blit(brick,(i,570))
            Screen.blit(brick,(0,i))
            Screen.blit(brick,(770,i))
        for i in range(0, WIDTH, 30):
            Screen.blit(brick,(i-150,80))
            Screen.blit(brick,(i-150,240))
            Screen.blit(brick,(i-150,400))
        for i in range(100, WIDTH, 30):
            Screen.blit(brick,(i,160))
            Screen.blit(brick,(i,320))
            Screen.blit(brick,(i,480))
        if snake1.element[0][1] > food.y-5 and snake1.element[0][1] <food.y+5:
            if snake1.element[0][0] > food.x-5 and snake1.element[0][0] < food.x+5:
                Score += 1
                food.x = random.randint(200,500)
                food.y = random.randint(200,400)
                snake1.element.append([0,0])
    
        if (snake1.element[0][0] > 0 and snake1.element[0][0] < 650 and snake1.element[0][1] < 110 and snake1.element[0][1] > 80) or(snake1.element[0][0] > 0 and snake1.element[0][0] < 650 and snake1.element[0][1] < 270 and snake1.element[0][1] >240) or (snake1.element[0][0] > 0 and snake1.element[0][0] < 650 and snake1.element[0][1] < 430 and snake1.element[0][1] > 400)or (snake1.element[0][0] > 100 and snake1.element[0][0] < 800 and snake1.element[0][1] < 190 and snake1.element[0][1] > 160) or ( snake1.element[0][0] > 100 and snake1.element[0][0] < 800 and snake1.element[0][1] < 350 and snake1.element[0][1] >320) or (snake1.element[0][0] > 100 and snake1.element[0][0] < 800 and snake1.element[0][1] < 510 and snake1.element[0][1] >480) or snake1.element[0][0] < 30 or snake1.element[0][0] > 770 or snake1.element[0][1] < 30 or snake1.element[0][1] > 570:
            game_over()
    
        SCORE = font.render("Score " + str(Score), True, (255, 180, 0))
        Screen.blit(SCORE, (150,70))
        pygame.display.flip()
        pygame.image.save(Screen, "zmeika.png")


#HARD
elif choose == 3:
    F = [[90, 65], [95,65], [100,65]]
    snake1 = Snake((0,0,255), F)
    while running:
        for i in range(len(snake1.element)-1):
            if snake1.element[0] == snake1.element[i+1]:
                game_over()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    save_game()
                    running = False
                if event.key == pygame.K_RIGHT and snake1.dx != -7:
                    snake1.dx = 7
                    snake1.dy = 0
                if event.key == pygame.K_LEFT and snake1.dx != 7:
                    snake1.dx = -7
                    snake1.dy = 0
                if event.key == pygame.K_UP and snake1.dy != 7:
                    snake1.dx = 0
                    snake1.dy = -7
                if event.key == pygame.K_DOWN and snake1.dy != -7:
                    snake1.dx = 0
                    snake1.dy = 7
        Screen.fill((0,204,255))
        snake1.draw()
        snake1.move()
        food.draw()
        FramePerSec.tick(FPS)
        for i in range(0, WIDTH, 30):
            Screen.blit(brick,(i,0))
            Screen.blit(brick,(i,570))
            Screen.blit(brick,(0,i))
            Screen.blit(brick,(770,i))
        for i in range(180,600, 30):
            Screen.blit(brick,(100,i-100))
            Screen.blit(brick,(670,i-100))
        for i in range(230,800,30):
            Screen.blit(brick,(i-130,80))
        for i in range(330,800,30):
            Screen.blit(brick,(i-130,470))
        for i in range(280,600, 30):
            Screen.blit(brick,(200,i-110))
        for i in range(420,800,30):
            Screen.blit(brick,(i-220,170))
        for i in range(370,600, 30):
            Screen.blit(brick,(570,i-200))
        for i in range(520,800,30):
            Screen.blit(brick,(i-220,380))
        for i in range(620,800,30):
            Screen.blit(brick,(i-320,270))
        
        if snake1.element[0][1] > food.y-5 and snake1.element[0][1] <food.y+5:
            if snake1.element[0][0] > food.x-5 and snake1.element[0][0] < food.x+5:
                Score += 1
                food.x = random.randint(40,90) and random.randint(140,190) and random.randint(240,290) and random.randint(340,560) and random.randint(610,660) and random.randint(710,760)
                food.y = random.randint(40,70) and random.randint(120,160) and random.randint(210,260) and random.randint(310,370) and random.randint(420,480) and random.randint(530,560)
                snake1.element.append([0,0])
    
        if (snake1.element[0][0] > 300 and snake1.element[0][0] < 480 and snake1.element[0][1] < 300 and snake1.element[0][1] > 270) or (snake1.element[0][0] > 300 and snake1.element[0][0] < 580 and snake1.element[0][1] < 410 and snake1.element[0][1] >380) or (snake1.element[0][0] > 570 and snake1.element[0][0] < 600 and snake1.element[0][1] < 410 and snake1.element[0][1] > 170) or (snake1.element[0][0] > 200 and snake1.element[0][0] < 580 and snake1.element[0][1] < 200 and snake1.element[0][1] > 170) or (snake1.element[0][0] > 200 and snake1.element[0][0] < 230 and snake1.element[0][1] < 490 and snake1.element[0][1] > 170) or (snake1.element[0][0] > 200 and snake1.element[0][0] < 670 and snake1.element[0][1] < 500 and snake1.element[0][1] > 470) or (snake1.element[0][0] > 670 and snake1.element[0][0] < 700 and snake1.element[0][1] < 500 and snake1.element[0][1] > 80) or (snake1.element[0][0] > 100 and snake1.element[0][0] < 670 and snake1.element[0][1] < 110 and snake1.element[0][1] > 80) or (snake1.element[0][0] > 100 and snake1.element[0][0] < 130 and snake1.element[0][1] < 500 and snake1.element[0][1] > 80) or snake1.element[0][0] < 30 or snake1.element[0][0] > 770 or snake1.element[0][1] < 30 or snake1.element[0][1] > 570:
            game_over()
    
        SCORE = font.render("Score " + str(Score), True, (255, 180, 0))
        Screen.blit(SCORE, (150,70))
        pygame.display.flip()
        pygame.image.save(Screen, "zmeika.png")
