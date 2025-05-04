import numpy as np
import pygame

from localization import localization as lc

WINDOW_WIDTH, WINDOW_HEIGHT = 800, 1000
COLORS = {"purple": (204, 204, 255), "iris": (93, 63, 211), "text": (25, 25, 112)}


pygame.init()

font = pygame.font.Font("font/RuthlessSketch.ttf", 50)
font_let = pygame.font.Font("font/RuthlessSketch.ttf", 95)

# class Letter(pygame.sprite.Sprite):
# def __init__(self, letter, pos, groups):
#     super().__init__(groups)
#     self.image = font.render(letter, False, COLLORS["b"])
#     self.rect = self.image.get_frect(center=pos)
#     self.hitbox_rect = self.rect.inflate(-60, -90)

lan = "ru"


class Game:
    def __init__(self):
        # setup
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Wordle")
        self.clock = pygame.time.Clock()
        self.running = True
        self.letter = np.empty(25, dtype=object)

        # groups
        self.phrases_sprites = pygame.sprite.Group()
        self.box_sprites = pygame.sprite.Group()
        self.letter_sprites = pygame.sprite.Group()

        # self.setup()

        # sprites

        Phrases(lc[lan]["message"]["welcome"], self.phrases_sprites)
        for x in range(5):
            for y in range(5):
                Box(x, y, self.box_sprites)

    def run(self):
        x, y, num = 0, 0, 0
        while self.running:
            # event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if lc[lan]["keys"].get(event.key) is not None:
                        self.letter[num] = Letter(
                            lc[lan]["keys"][event.key], x, y, self.letter_sprites
                        )

                        num += 1
                        y = num // 5
                        x = num % 5
                    if pygame.key.name(event.key) == "backspace" and num > 0:
                        num -= 1
                        y = num // 5
                        x = num % 5
                        self.letter[num].update()

            # draw
            self.display_surface.fill(COLORS["iris"])
            self.phrases_sprites.draw(self.display_surface)
            self.box_sprites.draw(self.display_surface)
            self.letter_sprites.draw(self.display_surface)
            pygame.display.update()

        pygame.quit()


class Phrases(pygame.sprite.Sprite):
    def __init__(self, message, groups):
        super().__init__(groups)
        self.image = font.render(message, False, COLORS["text"])
        self.rect = self.image.get_rect(center=(400, 50))


class Box(pygame.sprite.Sprite):
    def __init__(self, x, y, groups):
        super().__init__(groups)
        self.image = pygame.Surface((100, 100), pygame.SRCALPHA)
        pygame.draw.rect(self.image, COLORS["purple"], pygame.FRect((0, 0), (100, 100)))
        self.rect = self.image.get_frect(center=(150 + x * 125, 250 + y * 125))


class Letter(pygame.sprite.Sprite):
    def __init__(self, letter, x, y, groups):
        super().__init__(groups)
        self.image = font_let.render(letter, False, COLORS["text"])
        self.rect = self.image.get_rect(center=(150 + x * 125, 250 + y * 125))

    def update(self):
        self.kill()


if __name__ == "__main__":
    game = Game()
    game.run()
