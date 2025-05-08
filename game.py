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
        self.x_point = 0
        self.y_point = 0
        self.screen = 1
        self.try_num = 1
        self.lan = "eng"
        self.can = True
        self.result = 0
        self.word_ans = ""

        # groups
        self.box_sprites = pygame.sprite.Group()
        self.letter_sprites = pygame.sprite.Group()

        # box sprites
        for x in range(5):
            for y in range(5):
                Box(x, y, self.box_sprites)

    def get_phrase(self, message, type="message", place="up", only_rect=False):
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

    def check_word(self, word_guess: str, y: int):
        # 2 - буква на основном месте
        # 1 - буква есть в слове, но не на этом месте
        # 0 - остальное
        marks_list = [0 for i in range(5)]
        word_ans_copy = [x for x in self.word_ans]
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

    def letter_check(self, event):
        self.letter[self.y_point][self.x_point] = Letter(
            lc[self.lan]["keys"][event.key],
            self.x_point,
            self.y_point,
            self.letter_sprites,
        )
        if self.x_point != 4:
            self.x_point += 1
        else:
            self.can = False

    def bakscpace_check(self):
        if self.can is True:
            self.x_point -= 1
            self.letter[self.y_point][self.x_point].update()
        else:
            self.letter[self.y_point][self.x_point].update()
            self.can = True

    def enter_check(self):
        word = ""
        for i in range(5):
            word += self.letter[self.y_point][i].let
        self.result = self.check_word(word, self.y_point)
        self.y_point += 1
        self.x_point = 0
        self.can = True
        self.try_num += 1
        if self.result == 5 or self.try_num > 5:
            self.can = False

    def run(self):
        while self.running:
            # event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.screen == 1:
                        if self.get_phrase("eng", "button", "right", True).collidepoint(
                            event.pos
                        ):
                            self.lan = "eng"
                            self.screen += 1
                        elif self.get_phrase(
                            "eng", "button", "left", True
                        ).collidepoint(event.pos):
                            self.lan = "ru"
                            self.screen += 1
                        self.word_ans = random.choice(lc[self.lan]["vocab"])
                    elif self.screen == 3:
                        if self.result == 5:
                            self.screen = 5
                        elif self.try_num == 6:
                            self.screen = 4
                    elif self.screen == 4:
                        self.screen = 6
                    else:
                        self.screen += 1
                if event.type == pygame.KEYDOWN and self.screen == 3:
                    if (
                        lc[self.lan]["keys"].get(event.key) is not None
                        and self.can is True
                    ):
                        self.letter_check(event)
                    if pygame.key.name(event.key) == "backspace" and self.x_point != 0:
                        self.bakscpace_check()
                    if (
                        pygame.key.name(event.key) == "return"
                        and self.can is False
                        and self.result != 5
                        and self.try_num != 6
                    ):
                        self.enter_check()

            # draw
            self.display_surface.fill(COLORS["back"])
            match self.screen:
                case 1:
                    self.display_surface.blit(
                        *self.get_phrase(
                            lc[self.lan]["message"]["choose lang"], "message", "center"
                        )
                    )
                    pygame.draw.rect(
                        self.display_surface,
                        COLORS["white"],
                        self.get_phrase("eng", "button", "right", True),
                        0,
                        6,
                    )
                    self.display_surface.blit(
                        *self.get_phrase("eng", "button", "right")
                    )
                    pygame.draw.rect(
                        self.display_surface,
                        COLORS["white"],
                        self.get_phrase("eng", "button", "left", True),
                        0,
                        6,
                    )
                    self.display_surface.blit(*self.get_phrase("ru", "button", "left"))
                case 2:
                    self.display_surface.blit(
                        *self.get_phrase(
                            lc[self.lan]["message"]["welcome"], "message", "up"
                        )
                    )
                    self.display_surface.blit(
                        *self.get_phrase(
                            lc[self.lan]["message"]["welcome2"], "message", "center"
                        )
                    )
                case 3:
                    self.display_surface.blit(
                        *self.get_phrase(
                            lc[self.lan]["message"]["word request"], "message", "up"
                        )
                    )
                    self.box_sprites.draw(self.display_surface)
                    self.letter_sprites.draw(self.display_surface)
                case 4:
                    self.display_surface.blit(
                        *self.get_phrase(
                            lc[self.lan]["message"]["bad result"], "message", "center"
                        )
                    )
                case 5:
                    self.display_surface.blit(
                        *self.get_phrase(
                            lc[self.lan]["message"]["congrats"], "message", "center"
                        )
                    )
                case 6:
                    self.running = False
            pygame.display.update()

        pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.run()
