import os
import random
import pygame


# Class for the orange dude
class Player(object):

    def __init__(self):
        self.rect = pygame.Rect(16, 16, 16, 16)
        self.antibomberinos = 0
        self.defusedBombs = 0

    def move(self, dx, dy):
        # Move each axis separately. Note that this checks for collisions both times.
        if dx != 0:
            self.move_single_axis(dx, 0)
        if dy != 0:
            self.move_single_axis(0, dy)

    def move_single_axis(self, dx, dy):

        # Move the rect
        self.rect.x += dx
        self.rect.y += dy

        # If you collide with a wall, move out based on velocity
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                if dx > 0:  # Moving right; Hit the left side of the wall
                    self.rect.right = wall.rect.left
                if dx < 0:  # Moving left; Hit the right side of the wall
                    self.rect.left = wall.rect.right
                if dy > 0:  # Moving down; Hit the top side of the wall
                    self.rect.bottom = wall.rect.top
                if dy < 0:  # Moving up; Hit the bottom side of the wall
                    self.rect.top = wall.rect.bottom

        for bomb in bombs:
            if self.rect.colliderect(bomb.rect):
                if self.antibomberinos >= 1:
                    if dx > 0:  # Moving right; Hit the left side of the wall
                        self.rect.right = bomb.rect.left
                        bombs.remove(bomb)
                        self.antibomberinos-=1
                        self.defusedBombs+=1
                    if dx < 0:  # Moving left; Hit the right side of the wall
                        self.rect.left = bomb.rect.right
                        bombs.remove(bomb)
                        self.antibomberinos -= 1
                        self.defusedBombs+=1
                    if dy > 0:  # Moving down; Hit the top side of the wall
                        self.rect.bottom = bomb.rect.top
                        bombs.remove(bomb)
                        self.antibomberinos -= 1
                        self.defusedBombs+=1
                    if dy < 0:  # Moving up; Hit the bottom side of the wall
                        self.rect.top = bomb.rect.bottom
                        bombs.remove(bomb)
                        self.antibomberinos -= 1
                        self.defusedBombs+=1
                else:
                    raise SystemExit("BOOOOOOOOOOOM")
                if dx > 0:  # Moving right; Hit the left side of the wall
                    self.rect.right = bomb.rect.left
                if dx < 0:  # Moving left; Hit the right side of the wall
                    self.rect.left = bomb.rect.right
                if dy > 0:  # Moving down; Hit the top side of the wall
                    self.rect.bottom = bomb.rect.top
                if dy < 0:  # Moving up; Hit the bottom side of the wall
                    self.rect.top = bomb.rect.bottom
        for antibomb in antibombs:
            if self.rect.colliderect(antibomb.rect):
                if dx > 0:  # Moving right; Hit the left side of the wall
                    self.antibomberinos+=1
                    antibombs.remove(antibomb)
                if dx < 0:  # Moving left; Hit the right side of the wall
                    self.antibomberinos+=1
                    antibombs.remove(antibomb)
                if dy > 0:  # Moving down; Hit the top side of the wall
                    self.antibomberinos+=1
                    antibombs.remove(antibomb)
                if dy < 0:  # Moving up; Hit the bottom side of the wall
                    self.antibomberinos+=1
                    antibombs.remove(antibomb)

        for door in doors:
            if self.rect.colliderect(door.rect):
                print(self.defusedBombs)
                if dx > 0:  # Moving right; Hit the left side of the wall
                    self.rect.right = door.rect.left
                    if self.defusedBombs >= 2:
                        doors.remove(door)
                if dx < 0:  # Moving left; Hit the right side of the wall
                    self.rect.left = door.rect.right
                    if self.defusedBombs >= 2:
                        doors.remove(door)
                if dy > 0:  # Moving down; Hit the top side of the wall
                    self.rect.bottom = door.rect.top
                    if self.defusedBombs >= 2:
                        doors.remove(door)
                if dy < 0:  # Moving up; Hit the bottom side of the wall
                    self.rect.top = door.rect.bottom
                    if self.defusedBombs >= 2:
                        doors.remove(door)


# Nice class to hold a wall rect
class Wall(object):

    def __init__(self, pos):
        walls.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)

class Bomb(object):

    def __init__(self,pos):
        bombs.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)

class AntiBomb(object):

    def __init__(self, pos):
        antibombs.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)

class Door(object):

    def __init__(self, pos):
        doors.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)

YELLOW=(255, 200, 0)
ORANGE=(255,97,3)
# Initialise pygame
os.environ["SDL_VIDEO_CENTERED"] = "300"
pygame.init()

# Set up the display
pygame.display.set_caption("Get out!                                                                                                                                                                                                                                                Now!")
screen = pygame.display.set_mode((960, 720))

clock = pygame.time.Clock()
walls = []  # List to hold the walls
bombs = []  # List to hold the bombs
doors = []  # List for Door objects
antibombs = []
bomblocation = []
player = Player()  # Create the player

# Holds the level layout in a list of strings.
level = [
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
    "W                                                          W",
    "W WWWW    WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
    "W    W                                                     W",
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW W W W W W W W WW",
    "W                W         W             W                 W",
    "W W WWWWWWWWWWWW W    W            W                       W",
    "W W            W W   WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
    "W WWWWWWWWWWWW W W   W                      WAAD           W",
    "W W            W W   W    WWWWWWWWWWWWWW    WAAW  WWWW     W",
    "W W WWWWWWWWWWWW W   W    W            W    WWWW  W        W",
    "W W            W W                     W          W   WWWW W",
    "W WWWWWWWWWWWW W WWWWWW   WWWWWWWWWWWWWWWWWWWWWWWWWW       W",
    "W W            W      W                   WW               W",
    "WWWBWWWWWWWWWWWWWWWWW W            WWWWWWW    WWWWWW W W   W",
    "W   W               W WWWWWWWWWWWWWW        WWW      W W   W",
    "W WWW WWWWWWWWWWWWW W                 WWWWWW    WWWWWW W   W",
    "W W   W           W WWWWWWWWWW WWWWWWWW    W         W W   W",
    "W W   W   WWWWWWW W          W W         W WWWWWWWWWWW W   W",
    "W W WWWWW W     W WWWWWWWWWW W W WWWWWWW W    W        WWWWW",
    "W W     W W W W W      W W W W W W     W WWWW W WWWWWWWW   W",
    "W WWWWW W W W W W WWWW W W W W W WWWWW W    W W W          W",
    "W W   W W W W W W    W W W W W W     W WWWW W W W  WWWWWWW W",
    "W W W W W W W WWWWWW W   W W W WWWWW W    W W W      W   W W",
    "W W W W W   W      W W WWW W W     W W WW W W WWWWWWWW   W W",
    "W W W W WWWWWWWWW  W W       W     W W    W W              W",
    "W W W           W  W WWWWWWWWWWWWW W W WWWW WWWWWWWWWWWWWWWW",
    "W W WWWWWWWWWWW W  W   W           W                       W",
    "W W           W W  WW  W WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
    "W W WWWWWWW W WWW   W  W    W   W   W   W   W   W   W   W  W",
    "W W   W   W W  W    W  W  W   W   W   W   W   W   W   W    W",
    "W WWWWW W W WW W    WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW W",
    "W W   W W W W  W    W   W   W   W   W   W   W  W        AW W",
    "W W W   W W W  W      W   W   W   W   W   W    W WWWWW WWW W",
    "W W WWWWW W WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWBBW    AW   W W",
    "W W W        W                              WBBWWWWWWW W W W",
    "W W WWWWWWWWWWWWWWWWWWWWWW WWWWWW WWWWWWWWWWWAAAAAAAAW W W W",
    "W W          W             W      W         WAAAAAAAAW W W W",
    "W WWWWWWWWWW W WWWWWWWWWWWWW WWWWWW WWWWWWW WWWAAAAAAW W W W",
    "W W        W                 W      W     W   WAAAAAAW W W W",
    "W W WWWWWW W WWWWWWWWWWWWWWWWW WWWWWW W W WWW WAAAAAAW W W W",
    "W W      W W W                 W      W W     WAAAAAAW W   W",
    "WBWWWWWW W W W WWWWWWWWWWWWWWWWW WWWWWW WWWWWWWWWW WWWWWWWWW",
    "W        W                       W               W         E",
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",

]

# Parse the level string above. W = wall, E = exit
x = y = 0
for row in level:
    for col in row:
        if col == "W":
            Wall((x, y))
        if col == "E":
            endakubbur = pygame.Rect(x, y, 16, 16)
        if col == "B":
            Bomb((x, y))
            bomblocation.append(pygame.Rect(x, y, 16, 16))
        if col == "A":
            AntiBomb((x, y))
        if col == "D":
            Door((x,y))
        x += 16
    y += 16
    x = 0

running = True
while running:
    clock.tick(60)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            running = False

    # Move the player if an arrow key is pressed
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        player.move(-4, 0)
    if key[pygame.K_RIGHT]:
        player.move(4, 0)
    if key[pygame.K_UP]:
        player.move(0, -4)
    if key[pygame.K_DOWN]:
        player.move(0, 4)

    # Just added this to make it slightly fun ;)
    if player.rect.colliderect(endakubbur):
        raise SystemExit("You Win!")

    # Draw the scene
    screen.fill((0, 0, 0))
    for wall in walls:
        pygame.draw.rect(screen, (255, 255, 255), wall.rect)
    for bomb in bombs:
        pygame.draw.rect(screen, (255,0,255), bomb.rect)
    for antibomb in antibombs:
        pygame.draw.rect(screen, (50,150,120), antibomb.rect)
    for door in doors:
        if player.defusedBombs<=1:
            pygame.draw.rect(screen, (255,0,0), door.rect)
        else:
            pygame.draw.rect(screen, (124,252,0), door.rect)
    pygame.draw.rect(screen, (0, 255, 255), endakubbur)
    if player.antibomberinos >= 1:
        pygame.draw.rect(screen, (YELLOW), player.rect)
    else:
        pygame.draw.rect(screen, (ORANGE), player.rect)
    pygame.display.flip()
