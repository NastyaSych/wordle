import pygame

pygame.init()


def get_mes(
    message: str, font="font/RussianRail.otf", size=30
) -> pygame.surface.Surface:
    f = pygame.font.Font(font, size)
    message_ren = f.render(message, False, (111, 196, 169))
    return message_ren


def get_rect(message: str, pos_x=500, pos_y=300) -> pygame.surface.Surface:
    message_ren = get_mes(message)
    message_rect = message_ren.get_rect(center=(pos_x, pos_y))
    return message_rect


def get_mes_n_rect(message: str, pos_x=500, pos_y=300):
    return get_mes(message), get_rect(message, pos_x, pos_y)
