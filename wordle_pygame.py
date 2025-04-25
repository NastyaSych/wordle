import pygame

pygame.init() 

screen = pygame.display.set_mode((1000, 800)) 
pygame.display.set_caption("Wordle")
clock = pygame.time.Clock()

test_font = pygame.font.Font("Pixar.ttf", 50)
game_active = True

duck_surf = pygame.image.load("duck.jpg").convert()

game_message = test_font.render("Welcome to Wordle!", False, (111, 196, 169))
game_message_rect = game_message.get_rect(center=(500, 300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() 
            exit()  
    if game_active:
        screen.blit(duck_surf, (0, 0))
        screen.blit(game_message, game_message_rect)
    else:
        screen.fill((94, 129, 162))
    pygame.display.update()  # upper screen will stay forever
    clock.tick(60)        