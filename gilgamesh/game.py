import pygame
import random
import playsound

# Initialize Pygame
pygame.init()

#Music
playsound.playsound('Ancient Mesopotamian Music - Sumerians.mp3', False)
print ('Ancient Mesopotamian Music - Sumerians.mp3')

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("The Adventures of Gilgamesh")

# Load images
background = pygame.image.load("background.jpg")
background = pygame.transform.scale(background, (width, height))
gold_background = pygame.image.load("gold.png")
gold_background = pygame.transform.scale(gold_background, (width, height))
player = pygame.image.load("player.png")
player = pygame.transform.scale(player, (50, 50))
bullet_image = pygame.image.load("bullet.png")
bullet_image = pygame.transform.scale(bullet_image, (5, 15))
enemy_bullet_image = pygame.image.load("enemy_bullet.png")
enemy_bullet_image = pygame.transform.scale(enemy_bullet_image, (5, 15))
tree_image = pygame.image.load("tree.png")
tree_image = pygame.transform.scale(tree_image, (50, 50))  
red_image = pygame.image.load("red.png")
red_image = pygame.transform.scale(red_image, (50, 50))  
green_image = pygame.image.load("green.png")
green_image = pygame.transform.scale(green_image, (50, 50)) 
orange_image = pygame.image.load("orange.png")
orange_image = pygame.transform.scale(orange_image, (50, 50)) 
blue_image = pygame.image.load("blue.png")
blue_image = pygame.transform.scale(blue_image, (50, 50))
bull_image = pygame.image.load("bull.png")
bull_image = pygame.transform.scale(bull_image, (50, 50))
surprise_image = pygame.image.load("surprise.png")
surprise_image = pygame.transform.scale(surprise_image, (50, 50))

#Global Constants
WHITE = (255, 255, 255)
BIG = pygame.font.Font(None, 45)
MEDIUM = pygame.font.Font(None, 35)
SMALL = pygame.font.Font(None, 25)

# Define functions
def draw_player(gilgamesh, x, y):
    if gilgamesh == 1:
        screen.blit(player, (x, y))
    else:
        screen.blit(surprise_image, (x, y))

def fire_bullet(x, y, bullets):
    bullets.append({'x': x + 22.5, 'y': y})

def move_bullets(bullets):
    for bullet in bullets:
        bullet['y'] -= 7

def draw_bullets(bullets):
    for bullet in bullets:
        screen.blit(bullet_image, (bullet['x'], bullet['y']))

def fire_enemy_bullet(x, y, enemy_bullets):
    enemy_bullets.append({'x': x + 22.5, 'y': y})

def move_enemy_bullets(bullets, speed):
    for bullet in bullets:
        bullet['y'] += speed

def draw_enemy_bullets(bullets):
    for bullet in bullets:
        screen.blit(enemy_bullet_image, (bullet['x'], bullet['y']))

def draw_enemy(image, x, y):
    screen.blit(image, (x, y))

def move_down(enemies):
    for enemy in enemies:
        enemy['y'] += 10

def move_confetti(screen, confetti_particles):
    for particle in confetti_particles:
        particle['y'] += 1
        pygame.draw.circle(screen, particle['color'], (particle['x'], particle['y']), 5)


#change these to cutscene framework for consistent font
def main_menu():
    text1 = BIG.render("Welcome to The Adventures of Gilgamesh!", True, WHITE)
    text2 = MEDIUM.render("We hope you enjoy your journey.", True, WHITE)
    text_rect1 = text1.get_rect(center=(400, 150))
    text_rect2 = text2.get_rect(center=(400, 200))

    screen.blit(background, (0, 0))
    screen.blit(text1, text_rect1)
    screen.blit(text2, text_rect2)

    # Create button to click
    button_background_rect = pygame.Rect(width // 2 - 150, height - 120, 300, 40)
    pygame.draw.rect(screen, (0, 0, 128), button_background_rect)
    button_text = SMALL.render("Click Here to Begin", True, WHITE)
    button_rect = button_text.get_rect(center=(width // 2, height - 100))
    screen.blit(button_text, button_rect)

    pygame.display.update()

    # Wait for a mouse click on the button to continue
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    waiting = False

def tree_intro():
    text1 = SMALL.render("Your first task is to cut down trees in the cedar forest.", True, WHITE)
    text2 = SMALL.render("Press the arrow keys to move Gilgamesh, and the space bar to throw his swords upwards.", True, WHITE)
    text3 = SMALL.render("If you succeed, tales of your glorious deed will be sung for years to come.", True, WHITE)
    text4 = SMALL.render("Be careful, if the trees move down and hit Gilgamesh, the task is failed.", True, WHITE)
    text_rect1 = text1.get_rect(center=(400, 150))
    text_rect2 = text2.get_rect(center=(400, 190))
    text_rect3 = text3.get_rect(center=(400, 230))
    text_rect4 = text4.get_rect(center=(400, 270))

    screen.blit(background, (0, 0))
    screen.blit(text1, text_rect1)
    screen.blit(text2, text_rect2)
    screen.blit(text3, text_rect3)
    screen.blit(text4, text_rect4)

    # Create button to click
    button_background_rect = pygame.Rect(width // 2 - 150, height - 120, 300, 40)
    pygame.draw.rect(screen, (0, 0, 128), button_background_rect)
    button_text = SMALL.render("Click Here to Continue", True, WHITE)
    button_rect = button_text.get_rect(center=(width // 2, height - 100))
    screen.blit(button_text, button_rect)

    pygame.display.update()

    # Wait for a mouse click on the button to continue
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    waiting = False

# Cut scene between levels

def cut_scene(screen, text):
    texts = [MEDIUM.render(line, True, WHITE) for line in text]

    text_rects = [text.get_rect(center=(width // 2, height // 2 - 100 + i * 50)) for i, text in enumerate(texts)]

    screen.blit(background, (0, 0))
    for text, text_rect in zip(texts, text_rects):
        screen.blit(text, text_rect)

    # Create button to click
    button_background_rect = pygame.Rect(width // 2 - 150, height - 120, 300, 40)
    pygame.draw.rect(screen, (0, 0, 128), button_background_rect)
    button_text = SMALL.render("Click Here to Continue", True, WHITE)
    button_rect = button_text.get_rect(center=(width // 2, height - 100))
    screen.blit(button_text, button_rect)

    pygame.display.update()

    # Wait for a mouse click on the button to continue
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    waiting = False

    return texts, text_rects #required for Ishtar proposal cutscene


def draw_auras():
    draw_enemy(orange_image, 325, 50)
    draw_enemy(blue_image, 375, 50)
    draw_enemy(green_image, 425, 50)
    draw_enemy(orange_image, 475, 50)
    draw_enemy(green_image, 350, 100)
    draw_enemy(orange_image, 400, 100)
    draw_enemy(blue_image, 450, 100)

# Game loop
running = True
clock = pygame.time.Clock()

def confetti_animation(screen):
    confetti_particles = []

    for _ in range(50):
        x = random.randint(0, width)
        y = random.randint(0, height)
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        confetti_particles.append([x, y, color])  # Use lists instead of tuples

    for _ in range(50):
        for particle in confetti_particles:
            pygame.draw.circle(screen, particle[2], (particle[0], particle[1]), 5)
            particle[1] += 8  # Move confetti particles downward

        pygame.display.update()
        pygame.time.delay(50)  # Delay for a smoother animation
        screen.blit(gold_background, (0, 0))
    
    # Convert back to tuples
    #confetti_particles = [tuple(particle) for particle in confetti_particles]

    text1 = MEDIUM.render("Congratulations! You have completed your journey.", True, WHITE)
    text2 = SMALL.render("However, your quest for immortality has failed, as Enlil says to you (Tablet M, lines unclear):", True, WHITE)
    text3 = SMALL.render("'I made your destiny a destiny of kingship, but I did not make it a destiny of eternal life'", True, WHITE)
    text4 = SMALL.render("'Gilgamesh was established in the midst of Uruk a secure chamber.' (Tablet M, lines 261-262)", True, WHITE)
    text5 = SMALL.render("'The bar and threshold were hardest diorite, the bolts were hardest diorite,", True, WHITE)
    text6 = SMALL.render("the beams were cast in gold' (Tablet M, lines 253-255).", True, WHITE)
    text7 = SMALL.render("Enjoy your chamber, arrive in the Netherworld.", True, WHITE)

    text_rect1 = text1.get_rect(center=(400, 130))
    text_rect2 = text2.get_rect(center=(400, 190))
    text_rect3 = text3.get_rect(center=(400, 230))
    text_rect4 = text4.get_rect(center=(400, 270))
    text_rect5 = text5.get_rect(center=(400, 310))
    text_rect6 = text6.get_rect(center=(400, 350))
    text_rect7 = text7.get_rect(center=(400, 390))

    screen.blit(gold_background, (0, 0))

    pygame.draw.rect(screen, (0, 0, 128), text_rect1)
    pygame.draw.rect(screen, (0, 0, 128), text_rect2)
    pygame.draw.rect(screen, (0, 0, 128), text_rect3)
    pygame.draw.rect(screen, (0, 0, 128), text_rect4)
    pygame.draw.rect(screen, (0, 0, 128), text_rect5)
    pygame.draw.rect(screen, (0, 0, 128), text_rect6)
    pygame.draw.rect(screen, (0, 0, 128), text_rect7)

    screen.blit(text1, text_rect1)
    screen.blit(text2, text_rect2)
    screen.blit(text3, text_rect3)
    screen.blit(text4, text_rect4)
    screen.blit(text5, text_rect5)
    screen.blit(text6, text_rect6)
    screen.blit(text7, text_rect7)


    # text1 = BIG.render("Congratulations! You have completed your journey", True, WHITE)
    # text2 = MEDIUM.render("Insert more text here?.", True, WHITE)
    # text_rect1 = text1.get_rect(center=(width // 2, height // 2 - 50))
    # text_rect2 = text2.get_rect(center=(width // 2, height // 2 + 50))

    # screen.blit(gold_background, (0, 0))
    # screen.blit(text1, text_rect1)
    # screen.blit(text2, text_rect2)

    # Create button to click
    button_background_rect = pygame.Rect(width // 2 - 150, height - 120, 300, 40)
    pygame.draw.rect(screen, (0, 0, 128), button_background_rect)
    button_text = SMALL.render("Click Here to Play Again", True, WHITE)
    button_rect = button_text.get_rect(center=(width // 2, height - 100))
    screen.blit(button_text, button_rect)

    pygame.display.update()

    # Wait for a mouse click on the button to continue
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    waiting = False   

    restart()

def restart():
    main_menu()
    tree_intro()
    main_game()

def ishtar_proposal_cut_scene():
    text_tuple = cut_scene(screen, [
        "Ishtar approaches and proposes to Gilgamesh",
        "'On the beauty of Gilgamesh Lady Ishtar looked with longing:",
        "Come, Gilgamesh, be you my bridegroom!",
        "Grant me your fruits, grant me!",
        "Be you my husband and I your wife!' (Tablet VI, lines 6-9)."
    ])

    text1, text_rect1 = text_tuple[0][0], text_tuple[1][0]
    text2 = MEDIUM.render("Do you accept? (Y/N)", True, WHITE)
    text_rect2 = text2.get_rect(center=(width // 2, height // 2 + 50))

    screen.blit(background, (0, 0))
    screen.blit(text1, text_rect1)
    screen.blit(text2, text_rect2)
    pygame.display.update()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    cut_scene(screen, [
                        "All Ishtar’s spouses suffer a poor fate.",
                        "Mission failed.",
                        "Try again!"
                    ])
                    main_game()
                elif event.key == pygame.K_n:
                    cut_scene(screen, [
                        "You must fight the bull of heaven.",
                        "'Father, give me, please, the Bull of Heaven, so in his",
                        "dwelling I may slay Gilgamesh!'",
                        "(Tablet VI, lines 94-95)"
                    ])
                    return


def main_game():
    running = True
    clock = pygame.time.Clock()
    direction = 1
    gilgamesh = 1

     # Set player attributes
    player_x = 375
    player_y = 525
    player_speed = 5
    player_x_change = 0

    # Enemies attributes
    trees = [{'x': 50, 'y': 50},
           {'x': 100, 'y': 50},
           {'x': 150, 'y': 50},
           {'x': 200, 'y': 50},
           {'x': 250, 'y': 50},
           {'x': 300, 'y': 50},
           {'x': 350, 'y': 50},
           {'x': 400, 'y': 50},
           {'x': 450, 'y': 50},
           {'x': 500, 'y': 50},
           {'x': 75, 'y': 100},
           {'x': 125, 'y': 100},
           {'x': 175, 'y': 100},
           {'x': 225, 'y': 100},
           {'x': 275, 'y': 100},
           {'x': 325, 'y': 100},
           {'x': 375, 'y': 100},
           {'x': 425, 'y': 100},
           {'x': 475, 'y': 100},
           {'x': 525, 'y': 100},
           {'x': 50, 'y': 150},
           {'x': 100, 'y': 150},
           {'x': 150, 'y': 150},
           {'x': 200, 'y': 150},
           {'x': 250, 'y': 150},
           {'x': 300, 'y': 150},
           {'x': 350, 'y': 150},
           {'x': 400, 'y': 150},
           {'x': 450, 'y': 150},
           {'x': 500, 'y': 150},
           {'x': 75, 'y': 200},
           {'x': 125, 'y': 200},
           {'x': 175, 'y': 200},
           {'x': 225, 'y': 200},
           {'x': 275, 'y': 200},
           {'x': 325, 'y': 200},
           {'x': 375, 'y': 200},
           {'x': 425, 'y': 200},
           {'x': 475, 'y': 200},
           {'x': 525, 'y': 200},
           {'x': 50, 'y': 250},
           {'x': 100, 'y': 250},
           {'x': 150, 'y': 250},
           {'x': 200, 'y': 250},
           {'x': 250, 'y': 250},
           {'x': 300, 'y': 250},
           {'x': 350, 'y': 250},
           {'x': 400, 'y': 250},
           {'x': 450, 'y': 250},
           {'x': 500, 'y': 250}]

    auras = [{'x': 325, 'y': 50},
           {'x': 375, 'y': 50},
           {'x': 425, 'y': 50},
           {'x': 475, 'y': 50},
           {'x': 350, 'y': 100},
           {'x': 400, 'y': 100},
           {'x': 450, 'y': 100}]
    
    auras_copy = auras.copy() #this is for coloring the auras

    huwawas = [{'x': 400, 'y': 50}]

    bulls = [{'x': 400, 'y': 50}]
    bull_health = 5
    bull_cooldown = 0
    aura_cooldown = 0

    #dictionary to help draw different colored auras in the correct position
    image_map = {0: "o", 1: "b", 2: "g", 3: "o",
    4: "g", 5: "o", 6: "b"}

    #dictionary to make aura cooldown proportional to number of auras left
    aura_map = {1: 60, 2: 120, 3: 180, 4: 240, 5: 300, 6: 360, 7: 420}

    # Bullets attributes
    bullets = []
    enemy_bullets = []


    while running:
        screen.blit(background, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player_x_change = -player_speed
                if event.key == pygame.K_RIGHT:
                    player_x_change = player_speed
                if event.key == pygame.K_SPACE:
                    bullet_x = player_x
                    fire_bullet(bullet_x, player_y, bullets)
                if event.key == pygame.K_e:
                    gilgamesh *= -1

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    player_x_change = 0

        player_x += player_x_change
        player_x = max(0, player_x)
        player_x = min(width - 50, player_x)

        if bullets:
            move_bullets(bullets)
            draw_bullets(bullets)

        if enemy_bullets:
            if auras:
                move_enemy_bullets(enemy_bullets, 3)
            else:
                move_enemy_bullets(enemy_bullets, 6)
            draw_enemy_bullets(enemy_bullets)
        
        #Level 1
        if trees:
            for tree in trees:
                tree['x'] += direction
                if tree['x'] <= 0 or tree['x'] >= width - 50:
                    direction *= -1
                    move_down(trees)
                draw_enemy(tree_image, tree['x'], tree['y'])
                if tree['y'] > 525:
                    cut_scene(screen, ["Mission failed.",
                    "Try again!"])
                    main_game()

                for bullet in bullets[:]:
                    if (tree['x'] < bullet['x'] < tree['x'] + 50) and (tree['y'] < bullet['y'] < tree['y'] + 50):
                        bullets.remove(bullet)
                        trees.remove(tree)
                        break  # Break after removing an enemy
            if not trees:
                bullets.clear()
                cut_scene(screen, ["Congratulations! You've mastered the art of tree cutting.",
                "'I[Gilgamesh] will cut down the cedar,",
                "I will establish for ever a name eternal!' (Tablet Y, line 185)",
                "Prepare yourself for the next challenge!"])
                cut_scene(screen, ["After cutting down all the cedar trees in the forest,",
               "Huwawa has become very angry with Gilgamesh...",
               "'With all the commotion Gilgamesh disturbed Huwawa in his lair,",
               "...he launched against him his auras of terror.' (Version A, 66)"])
        
        #Level 2 part 1
        elif auras:

            for aura in auras:
                aura['x'] += 3*direction
                if aura['x'] <= 0 or aura['x'] >= width - 50:
                    direction *= -1
                    move_down(auras)
                if aura['y'] > 525:
                    cut_scene(screen, ["Mission failed.",
                    "Try again!"])
                    main_game()
                aura_cooldown -= 1
                if image_map[auras_copy.index(aura)] == "o":
                    draw_enemy(orange_image, aura['x'], aura['y'])
                elif image_map[auras_copy.index(aura)] == "g":
                    draw_enemy(green_image, aura['x'], aura['y'])
                elif image_map[auras_copy.index(aura)] == "b":
                    draw_enemy(blue_image, aura['x'], aura['y'])

                if aura_cooldown < 0:
                    fire_enemy_bullet(aura['x'], aura['y'], enemy_bullets)
                    aura_cooldown = aura_map[len(auras)]

                for bullet in bullets[:]:
                    if (aura['x'] < bullet['x'] < aura['x'] + 50) and (aura['y'] < bullet['y'] < aura['y'] + 50):
                        bullets.remove(bullet)
                        auras.remove(aura)
                        break 

                for bullet in enemy_bullets[:]:
                    if (player_x < bullet['x'] < player_x + 50) and (player_y < bullet['y'] < player_y + 50):
                        cut_scene(screen, ["Mission failed.",
                        "Try again!"])
                        main_game()

                if not auras:
                    bullets.clear()
                    enemy_bullets.clear()
                    cut_scene(screen, ["After destroying his seven auras,",
                    "Huwawa has become weak! Time to go in for the kill!",
                    "'Having stripped him[Huwawa] clean of his seven auras",
                    "of terror, he[Gilgamesh] drew near to his lair.'",
                    "(Version A, Tablet Unc, no lines given)"])

        #Level 2 part 2
        elif huwawas:
            for huwawa in huwawas:
                huwawa['x'] += 5*direction
                if huwawa['x'] <= 0 or huwawa['x'] >= width - 50:
                    direction *= -1
                    move_down(huwawas)
                draw_enemy(red_image, huwawa['x'], huwawa['y'])
                if huwawa['y'] > 525:
                    cut_scene(screen, ["Mission failed.",
                    "Try again!"])
                    main_game()

                for bullet in bullets[:]:
                    if (huwawa['x'] < bullet['x'] < huwawa['x'] + 50) and (huwawa['y'] < bullet['y'] < huwawa['y'] + 50):
                        bullets.remove(bullet)
                        huwawas.remove(huwawa)
                        break 

            if not huwawas:
                bullets.clear()
                ishtar_proposal_cut_scene()

        elif bulls:
            for bull in bulls:
                bull['x'] += 2*direction
                if bull['x'] <= 0 or bull['x'] >= width - 50:
                    direction *= -1
                    move_down(bulls)
                draw_enemy(bull_image, bull['x'], bull['y'])
                bull_cooldown -= 1
                if bull['y'] > 525:
                    cut_scene(screen, ["Mission failed.",
                    "Try again!"])
                    main_game()

                if bull_cooldown < 0:
                    fire_enemy_bullet(bull['x'], bull['y'], enemy_bullets)
                    bull_cooldown = 60

                for bullet in bullets[:]:
                    if (bull['x'] < bullet['x'] < bull['x'] + 50) and (bull['y'] < bullet['y'] < bull['y'] + 50):
                        bullets.remove(bullet)
                        bull_health -= 1
                        if bull_health <= 0:
                            bulls.remove(bull)
                            break
                
                for bullet in enemy_bullets[:]:
                    if (player_x < bullet['x'] < player_x + 50) and (player_y < bullet['y'] < player_y + 50):
                        cut_scene(screen, ["Mission failed.",
                        "Try again!"])
                        main_game()

            if not bulls:
                bullets.clear()
                enemy_bullets.clear()
                confetti_animation(screen)
            
            # Draw the bulls health on screen
            health_width = 50 
            health_height = 5  
            health_color = (255, 0, 0) 

            remaining_health = max(0, bull_health)
            pygame.draw.rect(screen, health_color, (bull['x'], bull['y'] - 10, health_width, health_height))
            pygame.draw.rect(screen, (0, 255, 0), (bull['x'], bull['y'] - 10, (remaining_health / 5) * health_width, health_height))


        draw_player(gilgamesh, player_x, player_y)
        pygame.display.update()
        clock.tick(60)

    # Quit Pygame
    pygame.quit()

main_menu()
tree_intro()
main_game() 