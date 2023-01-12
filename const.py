from pygame.sprite import Group
from pygame.transform import scale
from pygame.image import load

square_side = 30
SCREEN_WIDTH = square_side * 10
SCREEN_HEIGHT = square_side * 20
figureGroup = Group()
staticSquareGroup = Group()
squareGroup = Group()
scoreGroup = Group()
photos = [scale(load("images/colors/yellow.png"), (square_side, square_side)),
          scale(load("images/colors/blue.png"), (square_side, square_side)),
          scale(load("images/colors/green.png"), (square_side, square_side)),
          scale(load("images/colors/red.png"), (square_side, square_side)),
          scale(load("images/colors/pink.png"), (square_side, square_side)),
          scale(load("images/colors/purple.png"), (square_side, square_side)),
          scale(load("images/colors/orange.png"), (square_side, square_side)),
          ]
scores = [100, 300, 700, 1500, 0]
FPS = 60
speed = 20
background = load('images/background.jpg')
space_image = scale(load('images/Space.jpg'), (200, SCREEN_HEIGHT))
