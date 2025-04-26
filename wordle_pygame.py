import pygame

pygame.init() 

screen = pygame.display.set_mode((1000, 800)) 
pygame.display.set_caption("Wordle")
clock = pygame.time.Clock()

comic_font = pygame.font.Font("Pixar.ttf", 50)
trash_font = pygame.font.Font("Trash.ttf", 50)
game_active = True

duck_surf = pygame.image.load("duck.jpg").convert()

game_message = comic_font.render("Welcome to Wordle!", False, (111, 196, 169))
game_message_rect = game_message.get_rect(center=(500, 300))

# input_box = pygame.Rect(175, 375, 100, 50) # (x, y, width, high)

word_enter = ""

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() 
            exit()  
        if event.type == pygame.TEXTINPUT:
            word_enter += event.text
    if game_active:
        screen.blit(duck_surf, (0, 0))
        screen.blit(game_message, game_message_rect)
        word_enter_box = trash_font.render(word_enter, False, (240, 128, 128))
        input_box = word_enter_box.get_rect(center = (500, 400))
        screen.blit(word_enter_box, input_box)
        
    else:
        screen.fill((94, 129, 162))
    pygame.display.update()  # upper screen will stay forever
    clock.tick(60)        