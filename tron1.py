import pygame, random

#Initialize pygame
pygame.init()

#Set display window
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Tron light cycle")

#Set FSP and clock
FPS = 20
clock = pygame.time.Clock()

#Set game values
CELL_SIZE = 20

tron_x = WINDOW_WIDTH//2
tron_y = WINDOW_HEIGHT//2 + 100

tron_dx = CELL_SIZE
tron_dy = 0

score = 0

#Set colors
GREEN = (0, 255, 0)
DARKGREEN = (10, 50, 10)
RED = (255, 0, 0)
DARKRED = (150, 0, 0)
WHITE = (255, 255, 255)

#Set fonts
font = pygame.font.SysFont('gabriola', 48)

game_over_text = font.render("GAMEOVER", True, RED, DARKGREEN)
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

#Set sounds and music
miss_sound = pygame.mixer.Sound("C:/Users/pc/Desktop/python/Pygames/clown/miss_sound.wav")

tron_coord = (tron_x, tron_y, CELL_SIZE, CELL_SIZE)
tron_rect = pygame.draw.rect(display_surface, GREEN, tron_coord)

trail= []
score=0
#The main game loop
running = True
while running:
    #Check to see if the user wants to quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #Move the snake
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                tron_dx = -1*CELL_SIZE
                tron_dy = 0
            if event.key == pygame.K_RIGHT:
                tron_dx = CELL_SIZE
                tron_dy = 0
            if event.key == pygame.K_UP:
                tron_dx = 0
                tron_dy = -1*CELL_SIZE
            if event.key == pygame.K_DOWN:
                tron_dx = 0
                tron_dy = CELL_SIZE

    #Update the x,y position of the snakes head and make a new coordinate
    tron_x += tron_dx
    tron_y += tron_dy
    tron_coord = (tron_x, tron_y, CELL_SIZE, CELL_SIZE)
    
    if  (tron_x, tron_y) in trail:
        running = False
        display_surface.blit(game_over_text, game_over_rect)
    

    trail.append((tron_x,tron_y))
    #Update HUD
    score_text = font.render("Score: " + str(score), True, GREEN, DARKRED)

    #Fill the surface
    display_surface.fill(WHITE)
    
    #Blit HUD
    #display_surface.blit(game_over_rect, game_over_text)

    #Blit assets
    for i in trail:
       pygame.draw.rect(display_surface, DARKGREEN,(i[0],i[1],CELL_SIZE,CELL_SIZE))
    tron_rect = pygame.draw.rect(display_surface, GREEN, tron_coord)


    #Update display and tick clock
    pygame.display.update()
    clock.tick(FPS)

#End the game
pygame.quit()