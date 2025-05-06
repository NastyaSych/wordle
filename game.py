import random

import pygame

from localization import localization as lc

WINDOW_WIDTH, WINDOW_HEIGHT = 800, 950
COLORS = {
    "white": (204, 204, 255),
    "back": (93, 63, 211),
    "text": (25, 25, 112),
    2: "green",
    1: "yellow",
    0: (204, 204, 255),
}


pygame.init()

font = pygame.font.Font("font/RuthlessSketch.ttf", 35)
font_let = pygame.font.Font("font/RuthlessSketch.ttf", 95)


def get_phrase(message, type="message", place="up", only_rect=False):
    match type:
        case "button":
            text = font_let.render(message, False, COLORS["text"])
            match place:
                case "right":
                    point = (150, 700)
                case "left":
                    point = (650, 700)
        case "message":
            text = font.render(message, False, COLORS["text"])
            match place:
                case "up":
                    point = (400, 100)
                case "center":
                    point = (400, 500)
                case "down":
                    point = (400, 900)
    if only_rect is True:
        return text.get_rect(center=point)
    else:
        return text, text.get_rect(center=point)


class Box(pygame.sprite.Sprite):
    def __init__(self, x, y, groups, color=COLORS["white"]):
        super().__init__(groups)
        self.image = pygame.Surface((100, 100), pygame.SRCALPHA)
        self.color = color
        pygame.draw.rect(self.image, color, pygame.FRect((0, 0), (100, 100)))
        self.rect = self.image.get_frect(center=(150 + x * 125, 250 + y * 125))


class Letter(pygame.sprite.Sprite):
    def __init__(self, letter, x, y, groups):
        super().__init__(groups)
        self.let = letter
        self.image = font_let.render(self.let, False, COLORS["text"])
        self.rect = self.image.get_rect(center=(150 + x * 125, 250 + y * 125))

    def update(self):
        self.kill()


class Game:
    def __init__(self):
        # setup
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Wordle")
        self.clock = pygame.time.Clock()
        self.running = True
        self.letter = [[None for j in range(5)] for i in range(5)]

        # groups
        self.box_sprites = pygame.sprite.Group()
        self.letter_sprites = pygame.sprite.Group()

        # self.setup()

        # sprites
        for x in range(5):
            for y in range(5):
                Box(x, y, self.box_sprites)

    def check_word(self, word_guess: str, word_ans: str, y):
        # 2 - буква на основном месте
        # 1 - буква есть в слове, но не на этом месте
        # 0 - остальное
        marks_list = [0 for i in range(5)]
        word_ans_copy = [x for x in word_ans]
        # сначала находим полное совпадение и удаляем эти буквы
        for i in range(5):
            if word_guess[i] == word_ans_copy[i]:
                marks_list[i] = 2
                word_ans_copy[i] = "&"
        # смотрим на оставшиеся буквы
        for i in range(5):
            if marks_list[i] != 2:
                for true_i in range(5):
                    if word_guess[i] == word_ans_copy[true_i] and true_i != i:
                        marks_list[i] = 1
                        word_ans_copy[true_i] = "&"
        answer = 0
        for i in range(5):
            Box(i, y, self.box_sprites, color=COLORS[marks_list[i]])
            answer += int(marks_list[i] == 2)
        return answer

    def run(self):
        x, y = 0, 0
        screen = 1
        try_num = 1
        lan = "eng"
        can = True
        result = 0
        while self.running:
            # event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if screen == 1:
                        if get_phrase("eng", "button", "right", True).collidepoint(
                            event.pos
                        ):
                            lan = "eng"
                            screen += 1
                        elif get_phrase("eng", "button", "left", True).collidepoint(
                            event.pos
                        ):
                            lan = "ru"
                            screen += 1
                        word_ans = random.choice(lc[lan]["vocab"])
                    elif screen == 3:
                        if result == 5:
                            screen = 5
                        elif try_num == 6:
                            screen = 4
                    elif screen == 4:
                        screen = 6
                    else:
                        screen += 1
                if event.type == pygame.KEYDOWN and screen == 3:
                    if lc[lan]["keys"].get(event.key) is not None and can is True:
                        self.letter[y][x] = Letter(
                            lc[lan]["keys"][event.key], x, y, self.letter_sprites
                        )
                        if x != 4:
                            x += 1
                        else:
                            can = False
                    if pygame.key.name(event.key) == "backspace" and x != 0:
                        if can is True:
                            x -= 1
                            self.letter[y][x].update()
                        else:
                            self.letter[y][x].update()
                            can = True
                    if (
                        pygame.key.name(event.key) == "return"
                        and can is False
                        and result != 5
                        and try_num != 6
                    ):  # enter
                        word = ""
                        for i in range(5):
                            word += self.letter[y][i].let

                        result = self.check_word(word, word_ans, y)
                        y += 1
                        x = 0
                        can = True
                        try_num += 1
                        if result == 5 or try_num > 5:
                            can = False

            # draw
            self.display_surface.fill(COLORS["back"])
            match screen:
                case 1:
                    self.display_surface.blit(
                        *get_phrase(
                            lc[lan]["message"]["choose lang"], "message", "center"
                        )
                    )
                    pygame.draw.rect(
                        self.display_surface,
                        COLORS["white"],
                        get_phrase("eng", "button", "right", True),
                        0,
                        6,
                    )
                    self.display_surface.blit(*get_phrase("eng", "button", "right"))
                    pygame.draw.rect(
                        self.display_surface,
                        COLORS["white"],
                        get_phrase("eng", "button", "left", True),
                        0,
                        6,
                    )
                    self.display_surface.blit(*get_phrase("ru", "button", "left"))
                case 2:
                    self.display_surface.blit(
                        *get_phrase(lc[lan]["message"]["welcome"], "message", "up")
                    )
                    self.display_surface.blit(
                        *get_phrase(lc[lan]["message"]["welcome2"], "message", "center")
                    )
                case 3:
                    self.display_surface.blit(
                        *get_phrase(lc[lan]["message"]["word request"], "message", "up")
                    )
                    self.box_sprites.draw(self.display_surface)
                    self.letter_sprites.draw(self.display_surface)
                case 4:
                    self.display_surface.blit(
                        *get_phrase(
                            lc[lan]["message"]["bad result"], "message", "center"
                        )
                    )
                case 5:
                    self.display_surface.blit(
                        *get_phrase(lc[lan]["message"]["congrats"], "message", "center")
                    )
                case 6:
                    self.running = False
            pygame.display.update()

        pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.run()
