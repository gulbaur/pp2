import pygame
import random
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE=(0,0,255)
 
 
class Block(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
 
    def reset_pos(self):
        self.rect.y = random.randrange(-300, -20)
        self.rect.x = random.randrange(0, screen_width)
 
    def update(self):
        self.rect.y += 1
        if self.rect.y > 410:
            self.reset_pos()
 
 
 
class Player(Block):
    def update(self):
        pos = pygame.mouse.get_pos()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
 
class Block11(pygame.sprite.Sprite):
    
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
 
    def reset_pos(self):
        self.rect.y = random.randrange(0,600)
        self.rect.x = random.randrange(0, screen_width)
 
    def update(self):
        self.rect.y -= 1
        if self.rect.y > 410:
            self.reset_pos()
class Player2(Block11):
    def update(self):
        pos = pygame.mouse.get_pos()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
 
pygame.init()
 
screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])
block_list = pygame.sprite.Group()
block_list1 = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()
 
for i in range(50):
    block = Block(BLACK, 20, 15)
 
    block.rect.x = random.randrange(screen_width)
    block.rect.y = random.randrange(screen_height)
    block_list.add(block)
    all_sprites_list.add(block)
for i in range(50):
    block1 = Block11(GREEN, 25, 15)
    block1.rect.x = random.randrange(screen_width)
    block1.rect.y = random.randrange(screen_height)
 
    block_list1.add(block1)
    all_sprites_list.add(block1)
 
player = Player(RED, 20, 15)
all_sprites_list.add(player)
done = False

clock = pygame.time.Clock()
score = 0
 
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    screen.fill(WHITE)
 
    all_sprites_list.update()
    blocks_hit_list = pygame.sprite.spritecollide(player, block_list, False)
    blocks_hit_list1 = pygame.sprite.spritecollide(player, block_list1, False)

    for block in blocks_hit_list:
        score -= 1
        block.reset_pos()
    for block11 in blocks_hit_list1:
        score += 1
        block11.reset_pos()

    all_sprites_list.draw(screen)
    clock.tick(20)
    font = pygame.font.SysFont("Impact", 20)
    SCORE = font.render("Score " + str(score), True, (255, 180, 0))
    screen.blit(SCORE, (70,70))
    pygame.display.flip()
 
pygame.quit()
