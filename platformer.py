import pygame
from sys import exit

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
blob_surf = pygame.transform.scale(blob_surf,(60//3,25))

coin_surf = pygame.image.load("./img/coin.png").convert_alpha()

dirt_surf = pygame.image.load("./img/dirt.png").convert()
dirt_surf = pygame.transform.scale(dirt_surf,(25,25))
door_surf = pygame.image.load("./img/exit.png").convert_alpha()
            
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
    


LEVEL1 = [
    "5555555555555555555555555",
    "5                       5",
    "5                       5",
    "5                       5",
    "5                       5",
    "5                       5",
    "5                       5",
    "5                       5",
    "5                       5",
    "5                       5",
    "5                       5",
    "5                       5",
    "5                       5",
    "5                       5",
    "5                       5",
    "5                       5",
    "5                       5",
    "5                       5",
    "5                       5",
    "5                       5",
    "5                 111  75",
    "5           # # ########5",
    "5      ####00000########5",
    "5     ##################5",
    "5    ###################5",
    "5########################5",

]

LEVEL2 = [
    "5555555555555555555555555",
    "5                       5",
    "5                       5",
    "5                       5",
    "5                       5",
    "5                       5",
    "5                       5",
    "5                       5",
    "5                       5",
    "5                       5",
    "5                       5",
    "5                       5",
    "5                       5",
    "5                       5",
    "5                       5",
    "5                       5",
    "5         7    9        5",
    "5         ##########    5",
    "5                    1  5",
    "5                    ## 5",
    "5                 111   5",
    "5           # # ########5",
    "5      ####00000########5",
    "5     ##################5",
    "5    ###################5",
    "5#######################5",
]

LEVEL3 = [
    "5555555555555555555555555",
    "5                       5",
    "5                       5",
    "5                       5",
    "5                       5",
    "5                       5",
    "5                       5",
    "5                       5",
    "5                       5",
    "5                       5",
    "5                       5",
    "5                       5",
    "5                 7     5",
    "5                ##     5",
    "5         #####         5",
    "5      #                5",
    "5       #      9        5",
    "5         ##########    5",
    "5                    1  5",
    "5                    ## 5",
    "5                 111   5",
    "5           # # ########5",
    "5      ####00000########5",
    "5     ##################5",
    "5    ###################5",
    "5#######################5",
]
LEVEL4 = [
    "5555555555555555555555555",
    "5                       5",
    "5                       5",
    "5                       5",
    "5                       5",
    "5                       5",
    "5                       5",
    "5                       5",
    "5                       5",
    "5                       5",
    "5        7               5",
    "5        ###            5",
    "5            ###        5",
    "5                ##     5",
    "5         #####         5",
    "5      #                5",
    "5       #      9        5",
    "5         ##########    5",
    "5                    1  5",
    "5                    ## 5",
    "5                 111   5",
    "5           # # ########5",
    "5      ####00000########5",
    "5     ##################5",
    "5    ###################5",
    "5#######################5",
]
LEVEL5 = [
    "5555555555555555555555555",
    "5                       5",
    "5                       5",
    "5                       5",
    "5                       5",
    "5                       5",
    "5           7            5",
    "5           ###         5",
    "5               ###     5",
    "5          ###          5",
    "5    ###                5",
    "5        ###            5",
    "5            ###        5",
    "5                ##     5",
    "5         #####         5",
    "5      #                5",
    "5       #      9        5",
    "5         ##########    5",
    "5                    1  5",
    "5                    ## 5",
    "5                 111   5",
    "5           # # ########5",
    "5      ####00000########5",
    "5     ##################5",
    "5    ###################5",
    "5#######################5",
]



levels = [LEVEL1,LEVEL2,LEVEL3,LEVEL4,LEVEL5]
level_index = 0

def load_levels(level_index):
    global grass , lava , coin , blob , dirt , door 
    global on_ground , velocity_y

    grass = []
    lava = []
    coin =  []
    blob = []
    dirt = []
    door = []

    for index, item in enumerate(levels[level_index]):
        for letter_index, letter in enumerate(item):
            if letter == "0":
                x = letter_index * 25 
                y = index * 25 
                rect = lava_surf.get_rect(topleft=(x,y))
                lava.append(rect)

            if letter == "1":
                x = letter_index * 25
                y = index * 25
                rect = coin_surf.get_rect(topleft=(x,y))
                coin.append(rect)

            if letter == "#":
                x = letter_index * 25
                y = index * 25
                rect = grass_surf.get_rect(topleft=(x,y))
                grass.append(rect)

            if letter == "9":
                x = letter_index * 25
                y = index * 25
                rect = blob_surf.get_rect(topleft=(x,y))
                blob.append(rect)

            if letter == "5":
                x = letter_index * 25
                y = index * 25
                rect = dirt_surf.get_rect(topleft=(x,y))
                dirt.append(rect)

            if letter == "7":
                x = letter_index * 25
                y = index * 25
                rect = door_surf.get_rect(topleft=(x,y))
                door.append(rect)



    player_rect.midbottom = (50,500)
    velocity_y = 0
    on_ground = True
    
load_levels(level_index)
coin_sound =  pygame.mixer.Sound("./img/coin.wav")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and on_ground :
        velocity_y =-8
        on_ground = False

    if keys[pygame.K_d]:
        player_rect.x = player_rect.x + speed
        
        player_animation(left = False, right = True)
        

    if keys[pygame.K_a]:
        player_rect.x = player_rect.x - speed

        player_animation(left = True, right = False)

    for tile in grass:
        if player_rect.colliderect(tile):
            if keys[pygame.K_d]:
                player_rect.right = tile.left
            elif keys[pygame.K_a]:
                player_rect.left = tile.right

    for tile in dirt:
        if player_rect.colliderect(tile):
            if keys[pygame.K_d]:
                player_rect.right = tile.left
            elif keys[pygame.K_a]:
                player_rect.left = tile.right

    velocity_y += 0.5
    player_rect.y += velocity_y 

    for item in grass:
        if player_rect.colliderect(item):
            if velocity_y > 0:
                velocity_y = 0
                player_rect.bottom = item.top
                on_ground = True
            elif velocity_y < 0:
                player_rect.top = item.bottom
                velocity_y = 0
                    
                    
    for item in lava:
        if player_rect.colliderect(item):
            pygame.quit()
            exit()

    for item in blob:
        if player_rect.colliderect(item):
            pygame.quit()
            exit()

    for item in door:
        if player_rect.colliderect(item):
            level_index += 1
            if level_index < len(levels):
                load_levels(level_index)
            else:
                print("Победа!")
                pygame.quit()
                exit()
            



                
    for item in coin:
        if player_rect.colliderect(item):
            score += 1
            print(score)
            coin_sound.play()
            coin.remove(item)


            

    
    screen.blit(sky_surf, (0,0))
    screen.blit(sun_surf, (100,100))

    for item in grass:
        screen.blit(grass_surf,item)

    for item in blob:
        screen.blit(blob_surf,item)

    for item in lava:
        screen.blit(lava_surf,item)

    for item in coin:
        screen.blit(coin_surf,item)

    for item in dirt:
        screen.blit(dirt_surf,item)

    for item in door:
        screen.blit(door_surf,item)

    screen.blit(player_surf,player_rect)


    pygame.display.update()
    clock.tick(60)