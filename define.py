SCREEN_WIDTH = 300
SCREEN_HEIGHT = 600
BOARD_WIDTH = 10
BOARD_HEIGHT = 20
BOARD_ALL = BOARD_HEIGHT + BOARD_WIDTH
NAME = 'Tetris Game'
UPDATE = 60
DOWN_SPEED = UPDATE / 4
score = 0
bonus = 5

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,100,0)
YELLOW = (255,255,0)
BLUE = (0,0,250)
ORANGE = (255,140,0)
CYAN = (0,255,255)
MAGENTA = (255,0,255)
PURPLE = (128, 0, 128)
GREY = (28, 28, 28)

SHAPE_COLOR = [
    RED,
    GREEN,
    YELLOW,
    BLUE,
    ORANGE,
    CYAN,
    MAGENTA
]

SHAPE = [
    [[1,1,1,1]],
    [[1,1,1],[1,0,0]],
    [[0,1],[1,1],[0,1]],
    [[1,1,1],[0,0,1]],
    [[1,1],[1,1]],
    [[0,1,1],[1,1,0]],
    [[1,1,0],[0,1,1]],
]
