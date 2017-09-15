import arcade.key
DIR_UP = 65362
DIR_RIGHT = 65363
DIR_DOWN = 65364
DIR_LEFT = 65361
DIR = 0
DIR_OFFSET = { DIR_UP: (0,1),
               DIR_RIGHT: (1,0),
               DIR_DOWN: (0,-1),
               DIR_LEFT:(-1,0) }

class Snake:
    BLOCK_SIZE = 16
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y
        self.wait_time = 0
        self.direction = DIR_RIGHT
    
    def switch_direction(self, key):
         self.direction = key
 
    def update(self, delta):
        self.wait_time += delta
        if self.wait_time < Snake.MOVE_WAIT:
            return
        if self.x > self.world.width:
            self.x = 0
        if self.x < 0:
            self.x = self.world.width
        if self.y > self.world.height:
            self.y = 0
        if self.y < 0:
            self.y = self.world.width
        self.x += DIR_OFFSET[self.direction][0]*Snake.BLOCK_SIZE
        self.y += DIR_OFFSET[self.direction][1]*Snake.BLOCK_SIZE
        self.wait_time = 0
    MOVE_WAIT = 0.2
 
 
class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
 
        self.snake = Snake(self, width // 2, height // 2)

    def update(self, delta):
        self.snake.update(delta)
    def on_key_press(self, key, key_modifiers):
        if key >= 65361 and key <= 65364:
            self.snake.switch_direction(key)
        