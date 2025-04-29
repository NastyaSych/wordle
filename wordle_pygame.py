import random

import pygame

from funcbase import get_mes, get_mes_n_rect, get_rect
from localization import localization as lc

pygame.init()

screen = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("Wordle")
clock = pygame.time.Clock()

# шрифты
comic_font = pygame.font.Font("Pixar.ttf", 50)
trash_font = pygame.font.Font("Trash.ttf", 50)
game_active = True

duck_surf = pygame.image.load("duck.jpg").convert()

# input_box = pygame.Rect(175, 375, 100, 50) # (x, y, width, high)

# word_enter = ""
# word_enter_box = trash_font.render(word_enter, False, (240, 128, 128))
# input_box = word_enter_box.get_rect(center=(500, 400))
# screen.blit(word_enter_box, input_box)

letter = []
for i in range(0, 5):
    letter.append([])
    for j in range(0, 5):
        letter[i].append(pygame.Rect(210 + 120 * i, 110 + 120 * j, 100, 100))
mode = ""
screen_num = 0
slovo = []
for i in range(0, 5):
    slovo.append([])
attempt = 1
bukwa = 0


def check_word():
    pass


def show_letters(bukwa: int, slovo: str, attempt: int):
    for i in range(0, bukwa):
        screen.blit(get_mes(slovo[attempt - 1][i], size=95), letter[i][attempt - 1])


def show_word(slovo, attempt):
    for j in range(0, attempt):
        for i in range(0, 5):
            screen.blit(get_mes(slovo[j][i], size=95), letter[i][j])


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # if event.type == pygame.TEXTINPUT:
        #     word_enter += event.text
        if event.type == pygame.MOUSEBUTTONDOWN:
            match screen_num:
                case 0:
                    if get_rect("eng", 333, 500).collidepoint(event.pos):
                        lan = "eng"
                        screen_num += 1
                    elif get_rect("ru", 666, 500).collidepoint(event.pos):
                        lan = "ru"
                        screen_num += 1
                case 1:
                    screen_num += 1
        if event.type == pygame.KEYDOWN:
            match screen_num:
                case 2:
                    if lc[lan]["keys"].get(event.key) is not None:
                        if bukwa == 5:
                            # check_word(slovo)
                            bukwa = 0
                            attempt += 1
                        if attempt != 6:
                            slovo[attempt - 1].append(lc[lan]["keys"][event.key])
                        else:
                            game_active = False
                        if bukwa <= 4:
                            bukwa += 1

    if game_active:
        screen.blit(duck_surf, (0, 0))
        match screen_num:
            case 0:
                screen.blit(*get_mes_n_rect(lc["eng"]["message"]["choose lang"]))
                screen.blit(*get_mes_n_rect("eng", 333, 500))
                pygame.draw.rect(
                    screen, (111, 196, 169), get_rect("eng", 333, 500), 2, 6
                )
                screen.blit(*get_mes_n_rect("ru", 666, 500))
                pygame.draw.rect(
                    screen, (111, 196, 169), get_rect("ru", 666, 500), 2, 6
                )
            case 1:
                word_ans = random.choice(lc[lan]["vocab"])
                screen.blit(
                    *get_mes_n_rect(lc[lan]["message"]["welcome"]),
                )
                screen.blit(
                    *get_mes_n_rect(lc[lan]["message"]["welcome2"], pos_y=400),
                )
            case 2:
                screen.blit(
                    *get_mes_n_rect(lc[lan]["message"]["word request"], pos_y=50),
                )
                for i in range(5):
                    for j in range(5):
                        pygame.draw.rect(screen, (111, 196, 169), letter[j][i], 3)
                if attempt != 1:
                    show_word(slovo, attempt - 1)
                show_letters(bukwa, slovo, attempt)

    else:
        screen.fill((94, 129, 162))
    pygame.display.update()
    clock.tick(60)
