#import pygame
#import random

#pygame.init()

#width, height = 600, 600
#sreen = pygame.display.set_mode((width, height))
#pygame.display.set_caption("Угадай цвет")

#COLORS ={
   # "WHITE":(255, 255, 255),
   # "OLIVE":(128, 128, 0),
   # "PURPLE":(128, 0, 128),
    #"SILVER":(192,192,192),
#}

#color_keys = list(COLORS.keys())
#current_color = random.choice(color_keys)

#while True:
   # for event in pygame.event.get():
      #  if event.type == pygame.QUIT:
         # pygame.quit()
         # quit()

   # if event.type == pygame.KEYDOWN:

       # if event.key == pygame.K_w:
        #    current_color = "WHITE"
      #  elif event.key == pygame.K_o:
        #    current_color =="OLIVE"
       # elif event.key == pygame.K_p:
       #     current_color ="PURPLE"
      #  elif event.key == pygame.K_s:
           # current_color = "SILVER"

   # screen.fill(COLORS[current_color]) 
   # pygame.display.flip()


import sys
import random
import pygame

# Инициализация Pygame и микшера звуков
pygame.init()
pygame.mixer.init()

# Настройки окна
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Поймай квадрат!")

# Цвета (RGB)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 0, 0)
BLACK = (0, 0, 0)

# Загрузка звуковых эффектов
sound_hit = None
sound_miss = None

# Параметры игрового квадрата
TARGET_SIZE = 60
target_x = random.randint(0, WIDTH - TARGET_SIZE)
target_y = random.randint(0, HEIGHT - TARGET_SIZE)

# Игровые переменные
score = 0
GAME_DURATION = 30 # Время игры в секундах

start_ticks = pygame.time.get_ticks()

font = pygame.font.SysFont("Arial", 36)
final_font = pygame.font.SysFont("Arial", 50)

clock = pygame.time.Clock()
game_over = False

# Главный цикл игры
while not game_over:
    seconds_passed = (pygame.time.get_ticks() - start_ticks) / 1000
    time_left = max(0,GAME_DURATION - seconds_passed)
    
    if time_left <=0:
        game_over = True

for event in pygame.event.get():
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

    if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
        mouse_x, mouse_y = event.poss
        target_rect = pygame.Rect(target_x, target_y, TARGET_SIZE, TARGET_SIZE)

        if target_rect.collidepoint(mouse_x, mouse_y):
            score += 1
            target_x = random.randint(0, WIDTH - TARGET_SIZE)
            target_y = random.randint(0, HEIGHT - TARGET_SIZE)

    screen.fill(WHITE)
    if not game_over:
        pygame.draw.rect(screen, RED (target_x, target_y, TARGET_SIZE, TARGET_SIZE))
        score_text = font.render(f"Очки: {score}", True, BLACK)
        time_text = font.render(f"Время: {int(time_left)} c", True, BLACK)
        screen.blit(score_text,(20, 20))
        screen.blit(time_text,(WIDTH - 200, 20))

    pygame.display.flip()
    clock.tick(60)

    # Экран финала
    while True:
        screen.fill(WHITE)
        over_text = final_font.render("ИГРА ОКОНЧЕНА",True, RED)
        result_text = font.render(f"Ваш результат: {score} очков",True,BLACK)

        screen.blit(over_text,(WIDTH // 2 - 170, HEIGHT // 2 -80))
        screen.blit(result_text,(WIDTH // 2 - 150, HEIGHT // 2))

        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()