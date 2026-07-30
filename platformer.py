import pygame
from sys import exit
from pygame import mixer
from levels import LEVEL1,LEVEL2,LEVEL3,LEVEL4,LEVEL5
from world import World

pygame.mixer.pre_init(44100, -16, 2, 512)
mixer.init()
pygame.init() 

SCREEN_WIDTH = 625
SCREEN_HEIGHT = 650
speed = 2

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Platformer") 

clock = pygame.time.Clock()

sun_surf = pygame.image.load("./img/sun.png").convert_alpha()
sky_surf = pygame.image.load("./img/sky.png").convert()

grass_surf = pygame.image.load("./img/grass.png").convert()
grass_surf = pygame.transform.scale(grass_surf,(25,25))

lava_surf = pygame.image.load("./img/lava.png").convert_alpha()
score = 0
lava_surf = pygame.transform.scale(lava_surf,(25,25))
blob_surf = pygame.image.load("./img/blob.png").convert_alpha()
blob_surf = pygame.transform.scale(blob_surf,(60//3,20))

coin_surf = pygame.image.load("./img/coin.png").convert_alpha()

dirt_surf = pygame.image.load("./img/dirt.png").convert()
dirt_surf = pygame.transform.scale(dirt_surf,(25,25))
door_surf = pygame.image.load("./img/exit.png").convert_alpha()


coin_fx = pygame.mixer.Sound("img/coin.wav")
coin_fx.set_volume(0.5)
jump_fx = pygame.mixer.Sound("img/jump.wav")
jump_fx.set_volume(0.5)            
game_over_fx = pygame.mixer.Sound("img/game_over.wav")
game_over_fx.set_volume(0.5)
music = pygame.mixer.Sound("img/music.wav")
music.set_volume(0.5)

def player_animation(left, right):
    global player_surf, player_index

    if right == True:    
        player_index += 0.1
        if player_index >= len(player): player_index = 0
        player_surf = player[int(player_index)]
    
    if left == True:
        player_index += 0.1
        if player_index >= len(player): player_index = 0
        player_surf = player[int(player_index)]
        player_surf = pygame.transform.flip(player_surf, True, False)

player = []
player_index = 0
for i in range(1,5):
    player_image = pygame.image.load(f"./img/guy{i}.png").convert_alpha()
    player_image = pygame.transform.scale(player_image,(20,40))
    player.append(player_image)



player_surf = player[player_index]
player_rect = player_surf.get_rect(midbottom = (25,500))
    


surfs = {
    'grass': grass_surf, 'lava': lava_surf, 'coin': coin_surf,
    'blob':  blob_surf,  'dirt': dirt_surf, 'door': door_surf,
}


levels = [LEVEL1,LEVEL2,LEVEL3,LEVEL4,LEVEL5]
level_index = 0


world = World(levels,level_index,surfs)


player_rect.midbottom = (50,500)
velocity_y = 0
on_ground = True

coin_sound =  pygame.mixer.Sound("./img/coin.wav")

text_font = pygame.font.Font("./font/Pixeltype.ttf", 50)

text_surface = text_font.render(f"press enter to continue",False,"skyblue")
text_rect = text_surface.get_rect(center = (625//2,650//2))

def score_display():
    text_surface = text_font.render(f"Score{score}",False,"black")
    text_rect = text_surface.get_rect(center = (100,50))
    screen.blit(text_surface,text_rect)






isGameOver = False


show_debug = False
def draw_debug():
    for item in world.grass:
        pygame.draw.rect(screen, (0, 255, 0), item, 1)
    for item in world.dirt:
        pygame.draw.rect(screen, (150, 75, 0), item, 1)
    for item in world.lava:
        pygame.draw.rect(screen, (255, 0, 0), item, 1)
    for item in world.coin:
        pygame.draw.rect(screen, (255, 255, 0), item, 1)
    for item in world.blob:
        pygame.draw.rect(screen, (255, 0, 255), item, 1)
    for item in world.door:
        pygame.draw.rect(screen, (0, 150, 255), item, 1)
    pygame.draw.rect(screen, (255, 255, 255), player_rect, 1)

music.play()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN and isGameOver:
                isGameOver = False 
                player_rect.midbottom = (50,575)
                

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F1:
                show_debug = not show_debug

    if isGameOver:
        screen.fill("black")
        screen.blit(text_surface,text_rect)
    else:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE] and on_ground :
            velocity_y =-8
            on_ground = False
            jump_fx.play()
            


        if keys[pygame.K_d]:
            player_rect.x = player_rect.x + speed
            
            player_animation(left = False, right = True)
            

        if keys[pygame.K_a]:
            player_rect.x = player_rect.x - speed

            player_animation(left = True, right = False)

        for tile in world.grass:
            if player_rect.colliderect(tile):
                if keys[pygame.K_d]:
                    player_rect.right = tile.left
                elif keys[pygame.K_a]:
                    player_rect.left = tile.right

        for tile in world.dirt:
            if player_rect.colliderect(tile):
                if keys[pygame.K_d]:
                    player_rect.right = tile.left
                elif keys[pygame.K_a]:
                    player_rect.left = tile.right

        velocity_y += 0.5
        player_rect.y += velocity_y 

        for item in world.grass:
            if player_rect.colliderect(item):
                if velocity_y > 0:
                    velocity_y = 0
                    player_rect.bottom = item.top
                    on_ground = True
                elif velocity_y < 0:
                    player_rect.top = item.bottom
                    velocity_y = 0
                        
                        
        for item in world.lava:
            if player_rect.colliderect(item):
                score = 0
                isGameOver = True
                world.load_levels(level_index)

                game_over_fx.play()

        for item in world.blob:
            if player_rect.colliderect(item):
                score = 0
                isGameOver = True
                world.load_levels(level_index)

                game_over_fx.play()

        for item in world.door:
            if player_rect.colliderect(item):
                level_index += 1
                score = 0
                if level_index < len(levels):
                    world.load_levels(level_index)
                    player_rect.midbottom = (50,500)
                else:
                    print("Победа!")
                    pygame.quit()
                    exit()
                



                    
        for item in world.coin:
            if player_rect.colliderect(item):
                score += 1
                print(score)
                coin_sound.play()
                world.coin.remove(item)


                

        
        screen.blit(sky_surf, (0,0))
        screen.blit(sun_surf, (100,100))

        world.draw(screen)
        score_display()

        screen.blit(player_surf,player_rect)
        

    if show_debug:
        draw_debug()

    pygame.display.update()
    clock.tick(60)