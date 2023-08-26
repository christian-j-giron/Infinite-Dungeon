
import pygame
import random
import math

pygame.init()

# Creating the Screen with Title and Icon
pygame.display.init()
windowIcon = pygame.image.load("Infinite_Dungeon_Assets/Knight Attacking Sprites/attacking1.png")
pygame.display.set_icon(windowIcon)
pygame.display.set_caption("Infinite Dungeon")
background_util = pygame.image.load("Infinite_Dungeon_Assets/dungeon_background.png")
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()


# Generating Knight Sprites
knightSprites = [pygame.image.load("Infinite_Dungeon_Assets/Knight Attacking Sprites/attacking1.png").convert_alpha(),
                 pygame.image.load("Infinite_Dungeon_Assets/Knight Attacking Sprites/attacking2.png").convert_alpha(),
                 pygame.image.load("Infinite_Dungeon_Assets/Knight Attacking Sprites/attacking3.png").convert_alpha(),
                 pygame.image.load("Infinite_Dungeon_Assets/Knight Attacking Sprites/attacking4.png").convert_alpha(),
                 pygame.image.load("Infinite_Dungeon_Assets/Knight Attacking Sprites/attacking5.png").convert_alpha(),
                 pygame.image.load("Infinite_Dungeon_Assets/Knight Attacking Sprites/attacking6.png").convert_alpha(),
                 pygame.image.load("Infinite_Dungeon_Assets/Knight Attacking Sprites/attacking7.png").convert_alpha(),
                 pygame.image.load("Infinite_Dungeon_Assets/Knight Attacking Sprites/attacking8.png").convert_alpha(),
                 pygame.image.load("Infinite_Dungeon_Assets/Knight Attacking Sprites/attacking9.png").convert_alpha(),
                 pygame.image.load("Infinite_Dungeon_Assets/Knight Attacking Sprites/attacking10.png").convert_alpha(),
                 pygame.image.load("Infinite_Dungeon_Assets/Knight Running Sprites/runningLeft1.png").convert_alpha(),
                 pygame.image.load("Infinite_Dungeon_Assets/Knight Running Sprites/runningLeft2.png").convert_alpha(),
                 pygame.image.load("Infinite_Dungeon_Assets/Knight Running Sprites/runningLeft3.png").convert_alpha(),
                 pygame.image.load("Infinite_Dungeon_Assets/Knight Running Sprites/runningLeft4.png").convert_alpha(),
                 pygame.image.load("Infinite_Dungeon_Assets/Knight Running Sprites/runningLeft5.png").convert_alpha(),
                 pygame.image.load("Infinite_Dungeon_Assets/Knight Running Sprites/runningLeft6.png").convert_alpha(),
                 pygame.image.load("Infinite_Dungeon_Assets/Knight Running Sprites/runningLeft7.png").convert_alpha(),
                 pygame.image.load("Infinite_Dungeon_Assets/Knight Running Sprites/runningLeft8.png").convert_alpha(),
                 pygame.image.load("Infinite_Dungeon_Assets/Knight Running Sprites/runningLeft9.png").convert_alpha()]

# Generating Rock Sprite
rock = pygame.image.load("Infinite_Dungeon_Assets/rock.png")

# Generating Bat Sprites
batSprites = [pygame.image.load("Infinite_Dungeon_Assets/Bat Sprites/bat1.png"),
              pygame.image.load("Infinite_Dungeon_Assets/Bat Sprites/bat2.png"),
              pygame.image.load("Infinite_Dungeon_Assets/Bat Sprites/bat3.png")]

# Rendering Font
font = pygame.font.SysFont('comicsans', 40)

# Making Tutorial
tutorial = [font.render("          Press \"W\" to move in the direction you're facing!", True, (255, 255, 255)),
            font.render("                 Press \"A\" or \"D\" to move left or right!", True, (255, 255, 255)),
            font.render("                   Left click to attack with your sword!", True, (255, 255, 255)),
            font.render("            Use your sword to kill bats! +250 points each!", True, (255, 255, 255)),
            font.render("           You can only swing your sword in the direction", True, (255, 255, 255)),
            font.render("                 you're facing! (Use your A and D keys.)", True, (255, 255, 255)),
            font.render("           There's a half-second cooldown to swing your", True, (255, 255, 255)),
            font.render("                 sword each time you run, so be careful!", True, (255, 255, 255)),
            font.render("                       You die if you get hit by a bat!", True, (255, 255, 255)),
            font.render("                                       GLHF!!!", True, (255, 255, 255))]
tutorialY = 50

# Default Character Variables
x = 350
y = 405
left = True
right = False
dead = False
score = 0
playAgain = False
deadTimePoint = 0

# Creating scoreboard
scoreboardX = 630


def draw_scoreboard():
    scoreboard_font = pygame.font.SysFont("comicsans", 50, False)
    scoreboard = scoreboard_font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(scoreboard, (scoreboardX, 10))


# Default Bat Spawn and Location Variables
bat1 = False
bat2 = False
bat3 = False
bat4 = False
bat1_Index = 0
bat2_Index = 0
bat3_Index = 0
bat4_Index = 0
bat1_x = 0
bat1_y = 0
bat2_x = 0
bat2_y = 0
bat3_x = 0
bat3_y = 0
bat4_x = 0
bat4_y = 0
bat1_direction = ""
bat2_direction = ""
bat3_direction = ""
bat4_direction = ""
bat1_dead = False
bat2_dead = False
bat3_dead = False
bat4_dead = False


# Loading Background
def background():
    load_background = pygame.image.load("Infinite_Dungeon_Assets/dungeon_background.png")
    screen.blit(load_background, (0, 0))
    load_floor = pygame.image.load("Infinite_Dungeon_Assets/dungeon_floor.png")
    screen.blit(load_floor, (0, 500))


# Loading play button, title, tutorial and game over images
def play_button():
    load_play_button = pygame.image.load("Infinite_Dungeon_Assets/playButton.png")
    screen.blit(load_play_button, (300, 300))


def game_over():
    game_over_image = pygame.image.load("Infinite_Dungeon_Assets/Game-Over-PNG.png")
    screen.blit(game_over_image, (200, 100))


def title():
    title_font = pygame.font.SysFont("comicsans", 140, True)
    load_title1 = title_font.render("Infinite", True, (255, 255, 255))
    load_title2 = title_font.render("Dungeon", True, (255, 255, 255))
    screen.blit(load_title1, (200, 100))
    screen.blit(load_title2, (160, 195))


def draw_game_over():
    game_over_font = pygame.font.SysFont("comicsans", 180, True)
    load_game_over1 = game_over_font.render("Game", True, (255, 255, 255))
    load_game_over2 = game_over_font.render("Over", True, (255, 255, 255))
    screen.blit(load_game_over1, (200, 90))
    screen.blit(load_game_over2, (225, 190))


def draw_tutorial_button():
    load_tutorial_button = pygame.image.load("Infinite_Dungeon_Assets/question_mark2.png")
    screen.blit(load_tutorial_button, (0, 0))


def draw_exit_button():
    load_exit_button = pygame.image.load("Infinite_Dungeon_Assets/exit_button.png")
    screen.blit(load_exit_button, (750, 0))


# Loading Start Screen
def start_screen():
    load_background = pygame.image.load("Infinite_Dungeon_Assets/dungeon_background.png")
    screen.blit(load_background, (0, 0))
    play_button()
    title()
    draw_tutorial_button()
    pygame.display.update()


start_screen()
pregameRunning = True
tutorialRunning = False
gameRunning = False

# Pregame Loop
while pregameRunning:

    # Gets the mouse position and finds if its pressed
    mousePosition = pygame.mouse.get_pos()
    pygame.event.get()
    mouseButtons = pygame.mouse.get_pressed(3)
    mouseIsPressed = mouseButtons[0]
    mouseX = mousePosition[0]
    mouseY = mousePosition[1]

    # Finding if user is pressing play
    mouseOnPlay = 300 < mouseX < 500 and 300 < mouseY < 500

    # Finding if user is clicking tutorial
    mouseOnTutorial = 0 < mouseX < 75 and 0 < mouseY < 100

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pregameRunning = False
            gameRunning = False

    # Loop once user has started the game
    if mouseOnPlay and mouseIsPressed:
        pregameRunning = False
        gameRunning = True

    if mouseOnTutorial and mouseIsPressed:
        tutorialRunning = True

    if tutorialRunning:
        screen.blit(background_util, (0, 0))
        draw_exit_button()
        pygame.display.update()
        for i in range(10):
            screen.blit(tutorial[i], (0, tutorialY))
            tutorialY = tutorialY + 50
            pygame.display.update()
        tutorialY = 50

    while tutorialRunning:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                tutorialRunning = False
                pregameRunning = False
                gameRunning = False

        mousePosition = pygame.mouse.get_pos()
        pygame.event.get()
        mouseButtons = pygame.mouse.get_pressed(3)
        mouseIsPressed = mouseButtons[0]
        mouseX = mousePosition[0]
        mouseY = mousePosition[1]

        # Checking if mouse is on escape button
        mouseOnExit = 750 < mouseX < 800 and 0 < mouseY < 50

        if mouseIsPressed and mouseOnExit:
            tutorialRunning = False
            start_screen()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                tutorialRunning = False
                pregameRunning = False
                gameRunning = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pregameRunning = False
            gameRunning = False

# Default knight values
knightIndex = 0
adj_x = x - 4
adj_y = y
# Saves X and Y-coordinates of each bat spawn
bat1StartX = 0
bat1StartY = 0
bat2StartX = 0
bat2StartY = 0
bat3StartX = 0
bat3StartY = 0
bat4StartX = 0
bat4StartY = 0
# Gets time that user starts game: helps keep track of time in game
startTime = (pygame.time.get_ticks()/1000)

while gameRunning:

    # Sets fps
    clock.tick(30)

    # Holds the sprites for each knight depending on animation stage and direction facing
    knightSpriteLeft = knightSprites[knightIndex]
    knightSpriteRight = pygame.transform.flip(knightSprites[knightIndex], True, False)

    # Main function for drawing each bat
    def draw_bat(bat_index, bat_direction, bat_x, bat_y):

        # Holds the sprites for the bat depending on animation stage and direction facing
        bat_sprite_left = pygame.transform.flip(batSprites[bat_index], True, False)
        bat_sprite_right = batSprites[bat_index]

        # Draws bat depending on direction
        if bat_direction == "left":
            screen.blit(bat_sprite_left, (bat_x, bat_y))
        if bat_direction == "right":
            screen.blit(bat_sprite_right, (bat_x, bat_y))

    # Function that checks if a bat was killed by player
    def bat_killed(bat_x, bat_y, bat_direction):
        if left and bat_direction == "left":
            return False
        elif left and bat_direction == "right":
            if x - 48 < bat_x < x + 40 and y - 22 < bat_y + 14 < 500 and mouseIsPressed:
                return True
        elif right and bat_direction == "left":
            if x < bat_x < x + 88 and y - 22 < bat_y + 14 < 500 and mouseIsPressed:
                return True
        elif right and bat_direction == "right":
            return False

    # Creating knight and bat hitboxes
    knightHitbox = pygame.Rect(x + 4, y - 1, 38, 95)
    bat1Hitbox = pygame.Rect(bat1_x, bat1_y, 18, 18)
    bat2Hitbox = pygame.Rect(bat2_x, bat2_y, 18, 18)
    bat3Hitbox = pygame.Rect(bat3_x, bat3_y, 18, 18)
    bat4Hitbox = pygame.Rect(bat4_x, bat4_y, 18, 18)

    # Draws background and scoreboard
    if score >= 100:
        scoreboardX = 600
    if score >= 1000:
        scoreboardX = 580
    if score >= 10000:
        scoreboardX = 550
    if score >= 100000:
        scoreboardX = 530
    background()
    draw_scoreboard()

    # Draws bat sprite depending on location
    if bat1:
        draw_bat(bat1_Index, bat1_direction, bat1_x, bat1_y)
    if bat2:
        draw_bat(bat2_Index, bat2_direction, bat2_x, bat2_y)
    if bat3:
        draw_bat(bat3_Index, bat3_direction, bat3_x, bat3_y)
    if bat4:
        draw_bat(bat4_Index, bat4_direction, bat4_x, bat4_y)

    # Draws knight sprite depending on direction
    if left:
        screen.blit(knightSpriteLeft, (adj_x, adj_y))
    if right:
        screen.blit(knightSpriteRight, (adj_x, adj_y))

    pygame.display.update()

    # Checking if each bat has killed a player
    if pygame.Rect.colliderect(knightHitbox, bat1Hitbox):
        dead = True
    if pygame.Rect.colliderect(knightHitbox, bat2Hitbox):
        dead = True
    if pygame.Rect.colliderect(knightHitbox, bat3Hitbox):
        dead = True
    if pygame.Rect.colliderect(knightHitbox, bat4Hitbox):
        dead = True

    # Determines if each bat has been killed or flown off screen
    if bat1:
        bat1_dead = bat_killed(bat1_x, bat1_y, bat1_direction)
        if bat1_dead:
            bat1 = False
            bat1_dead = False
            bat1_x = 0
            bat1_y = 0
            score = score + 250
        elif bat1_direction == "left" and bat1_x < -50:
            bat1 = False
            bat1_x = 0
            bat1_y = 0
        elif bat1_direction == "right" and bat1_x > 850:
            bat1 = False
            bat1_x = 0
            bat1_y = 0
    if bat2:
        bat2_dead = bat_killed(bat2_x, bat2_y, bat2_direction)
        if bat2_dead:
            bat2 = False
            bat2_dead = False
            bat2_x = 0
            bat2_y = 0
            score = score + 250
        elif bat2_direction == "left" and bat2_x < -50:
            bat2 = False
            bat2_x = 0
            bat2_y = 0
        elif bat2_direction == "right" and bat2_x > 850:
            bat2 = False
            bat2_x = 0
            bat2_y = 0
    if bat3:
        bat3_dead = bat_killed(bat3_x, bat3_y, bat3_direction)
        if bat3_dead:
            bat3 = False
            bat3_dead = False
            bat3_x = 0
            bat3_y = 0
            score = score + 250
        elif bat3_direction == "left" and bat3_x < -50:
            bat3 = False
            bat3_x = 0
            bat3_y = 0
        elif bat3_direction == "right" and bat3_x > 850:
            bat3 = False
            bat3_x = 0
            bat3_y = 0
    if bat4:
        bat4_dead = bat_killed(bat4_x, bat4_y, bat4_direction)
        if bat4_dead:
            bat4 = False
            bat4_dead = False
            bat4_x = 0
            bat4_y = 0
            score = score + 250
        elif bat4_direction == "left" and bat4_x < -50:
            bat4 = False
            bat4_x = 0
            bat4_y = 0
        elif bat4_direction == "right" and bat4_x > 850:
            bat4 = False
            bat4_x = 0
            bat4_y = 0

    # Loading game over screen
    if dead:
        deadTimePoint = pygame.time.get_ticks()/1000
        deadTime = 0
        draw_game_over()
        pygame.display.update()

    # Game over loop
    while dead:

        # Draws play again button after 5 seconds
        deadTime = pygame.time.get_ticks()/1000 - deadTimePoint
        if not playAgain and deadTime >= 3:
            play_button()
            pygame.display.update()
            playAgain = True

        # Finding if player is clicking on play again
        mouseX = pygame.mouse.get_pos()[0]
        mouseY = pygame.mouse.get_pos()[1]
        mouseIsPressed = pygame.mouse.get_pressed(3)[0]
        mouseOnPlay = 300 < mouseX < 500 and 300 < mouseY < 500

        if mouseIsPressed and mouseOnPlay and playAgain:
            # Ends game over screen
            dead = False
            playAgain = False

            # Resets all default variables
            x = 350
            y = 405
            left = True
            right = False
            score = 0
            scoreboardX = 630
            bat1 = False
            bat2 = False
            bat3 = False
            bat4 = False
            bat1_Index = 0
            bat2_Index = 0
            bat3_Index = 0
            bat4_Index = 0
            bat1_x = 0
            bat1_y = 0
            bat2_x = 0
            bat2_y = 0
            bat3_x = 0
            bat3_y = 0
            bat4_x = 0
            bat4_y = 0
            bat1_direction = ""
            bat2_direction = ""
            bat3_direction = ""
            bat4_direction = ""
            bat1_dead = False
            bat2_dead = False
            bat3_dead = False
            bat4_dead = False
            # Default knight values
            knightIndex = 0
            adj_x = x - 4
            adj_y = y
            # Saves X and Y-coordinates of each bat spawn
            bat1StartX = 0
            bat1StartY = 0
            bat2StartX = 0
            bat2StartY = 0
            bat3StartX = 0
            bat3StartY = 0
            bat4StartX = 0
            bat4StartY = 0
            # Gets time that user starts game: helps keep track of time in game
            startTime = (pygame.time.get_ticks() / 1000)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameRunning = False
                dead = False

    if not dead:
        score = score + 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameRunning = False

    # Gets the mouse position and finds if its pressed
    mousePosition = pygame.mouse.get_pos()
    pygame.event.get()
    mouseButtons = pygame.mouse.get_pressed(3)
    mouseIsPressed = mouseButtons[0]
    mouseX = mousePosition[0]
    mouseY = mousePosition[1]

    # Gets directional key presses
    W = pygame.key.get_pressed()[pygame.K_w]
    A = pygame.key.get_pressed()[pygame.K_a]
    S = pygame.key.get_pressed()[pygame.K_s]
    D = pygame.key.get_pressed()[pygame.K_d]

    # Changes directional values, x-coordinate, and animation stage based on user input
    if mouseIsPressed:
        knightIndex = knightIndex + 1
    elif 0 < knightIndex < 9:
        knightIndex = knightIndex + 1
    elif A or (W and left) or (S and right):
        left = True
        right = False
        if knightIndex == 0:
            knightIndex = knightIndex + 10
        else:
            knightIndex = knightIndex + 1
        if x > 0:
            x = x - 2
    elif D or (W and right) or (S and left):
        left = False
        right = True
        if knightIndex == 0:
            knightIndex = knightIndex + 10
        else:
            knightIndex = knightIndex + 1
        if x < 700:
            x = x + 2
    elif 10 <= knightIndex < 18:
        knightIndex = knightIndex + 1
    if knightIndex == 9 or knightIndex == 18:
        knightIndex = 0

    # Adjusting "blit" location based on sprite and direction facing
    if knightIndex == 0:
        if left:
            adj_x = x - 4
        if right:
            adj_x = x - 29
    if knightIndex == 1:
        if left:
            adj_x = x - 15
        if right:
            adj_x = x - 30
    if knightIndex == 2:
        adj_y = y - 3
        if left:
            adj_x = x - 27
        if right:
            adj_x = x - 39
    if knightIndex == 3:
        adj_y = y - 25
        if left:
            adj_x = x - 27
        if right:
            adj_x = x - 30
    if knightIndex == 4:
        adj_y = y
        if left:
            adj_x = x - 34
        if right:
            adj_x = x - 28
    if knightIndex == 5:
        if left:
            adj_x = x - 48
        if right:
            adj_x = x - 28
    if knightIndex == 6:
        if left:
            adj_x = x - 37
        if right:
            adj_x = x - 29
    if knightIndex == 7:
        if left:
            adj_x = x - 11
        if right:
            adj_x = x - 29
    if knightIndex == 8:
        if left:
            adj_x = x - 7
        if right:
            adj_x = x - 29
    if knightIndex == 9:
        if left:
            adj_x = x - 7
        if right:
            adj_x = x - 30
    if knightIndex == 10:
        if left:
            adj_x = x - 19
        if right:
            adj_x = x - 41
    if knightIndex == 11:
        if left:
            adj_x = x - 13
        if right:
            adj_x = x - 43
    if knightIndex == 12:
        if left:
            adj_x = x - 10
        if right:
            adj_x = x - 43
    if knightIndex == 13:
        if left:
            adj_x = x - 11
        if right:
            adj_x = x - 43
    if knightIndex == 14:
        if left:
            adj_x = x - 12
        if right:
            adj_x = x - 42
    if knightIndex == 15:
        if left:
            adj_x = x - 10
        if right:
            adj_x = x - 43
    if knightIndex == 16:
        if left:
            adj_x = x - 8
        if right:
            adj_x = x - 41
    if knightIndex == 17:
        if left:
            adj_x = x - 13
        if right:
            adj_x = x - 42
    if knightIndex == 18:
        if left:
            adj_x = x - 15
        if right:
            adj_x = x - 43

    # Setting spawn probability variables based on time in game
    runningTime = (pygame.time.get_ticks()/1000) - startTime
    batSpawnProbability = (math.sqrt(2 * runningTime)) / 100
    rockSpawnProbability = (math.sqrt(runningTime) + 10) / 100

    # Setting bat spawn values: x, y, direction, location
    randomNumber1 = random.random()
    randomInt2 = random.randint(1, 10)
    randomY = random.randint(100, 300)
    if randomNumber1 <= batSpawnProbability and int(runningTime) % randomInt2 == 0:
        if not bat1:
            bat1 = True
            bat1_y = randomY
            bat1StartY = randomY
            if randomNumber1 <= (batSpawnProbability / 2):
                bat1_direction = "left"
                bat1_x = 800
                bat1StartX = 800
            else:
                bat1_direction = "right"
                bat1_x = -100
                bat1StartX = -100
        elif not bat2:
            bat2 = True
            bat2_y = randomY
            bat2StartY = randomY
            if randomNumber1 <= (batSpawnProbability / 2):
                bat2_direction = "left"
                bat2_x = 800
                bat2StartX = 800
            else:
                bat2_direction = "right"
                bat2_x = -100
                bat2StartX = -100
        elif not bat3:
            bat3 = True
            bat3_y = randomY
            bat3StartY = randomY
            if randomNumber1 <= (batSpawnProbability / 2):
                bat3_direction = "left"
                bat3_x = 800
                bat3StartX = 800
            else:
                bat3_direction = "right"
                bat3_x = -100
                bat3StartX = -100
        elif not bat4:
            bat4 = True
            bat4_y = randomY
            bat4StartY = randomY
            if randomNumber1 <= (batSpawnProbability / 2):
                bat4_direction = "left"
                bat4_x = 800
                bat4StartX = 800
            else:
                bat4_direction = "right"
                bat4_x = -100
                bat4StartX = -100

    # Setting equation for y-coordinate of each bat with respect to their x-coordinate (relative to their original x)
    bat1ProgressionX = math.fabs(bat1_x - bat1StartX)
    bat2ProgressionX = math.fabs(bat2_x - bat2StartX)
    bat3ProgressionX = math.fabs(bat3_x - bat3StartX)
    bat4ProgressionX = math.fabs(bat4_x - bat4StartX)

    def get_bat_y(bat_start_point, bat_progression):
        return 10 * (math.sqrt(bat_progression)) + bat_start_point


    if bat1:
        if bat1_direction == "left":
            bat1_x = bat1_x - 3
        else:
            bat1_x = bat1_x + 3
        if bat1_y < 425:
            bat1_y = get_bat_y(bat1StartY, bat1ProgressionX)
        bat1_Index = bat1_Index + 1
        if bat1_Index == 3:
            bat1_Index = 0
    if bat2:
        if bat2_direction == "left":
            bat2_x = bat2_x - 3
        else:
            bat2_x = bat2_x + 3
        if bat2_y < 425:
            bat2_y = get_bat_y(bat2StartY, bat2ProgressionX)
        bat2_Index = bat2_Index + 1
        if bat2_Index == 3:
            bat2_Index = 0
    if bat3:
        if bat3_direction == "left":
            bat3_x = bat3_x - 3
        else:
            bat3_x = bat3_x + 3
        if bat3_y < 425:
            bat3_y = get_bat_y(bat3StartY, bat3ProgressionX)
        bat3_Index = bat3_Index + 1
        if bat3_Index == 3:
            bat3_Index = 0
    if bat4:
        if bat4_direction == "left":
            bat4_x = bat4_x - 3
        else:
            bat4_x = bat4_x + 3
        if bat4_y < 425:
            bat4_y = get_bat_y(bat4StartY, bat4ProgressionX)
        bat4_Index = bat4_Index + 1
        if bat4_Index == 3:
            bat4_Index = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameRunning = False

pygame.display.update()
pygame.quit()
