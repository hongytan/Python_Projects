# Space invasion game by TokyoEdTech - Learning to code

import turtle
import math

# Setting up screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
wn = turtle.Screen()
wn.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
wn.title("Space Arena! by @TokyoEdTech")
wn.bgcolor("black")
wn.tracer(0)

# Creates a pen object
pen = turtle.Turtle()
pen.speed(0)
pen.penup()
pen.hideturtle()

class Game():
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def render_border(self, pen):
        pen.color("white")
        pen.width(3)
        pen.penup()

        left = self.width / -2.0
        right = self.width / 2.0
        top = self.height / 2.0
        bottom = self.height / -2.0

        pen.goto(left,top)
        pen.pendown()
        pen.goto(right,top)
        pen.goto(right, bottom)
        pen.goto(left, bottom)
        pen.goto(left, top)
        pen.penup()

class Sprite():
    def __init__(self, x, y, shape, color):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = color
        self.dx = 0
        self.dy = 0
        self.heading = 0
        self.da = 0
        self.thrust = 0.0
        self.acceleration = 0.1
        self.health = 100
        self.max_health = 100
        
    def update(self):
        """ Updates position of sprites """ 
        
        # Rotates player ship
        self.heading += self.da
        self.heading %= 360

        # Moves player ship forward
        self.dx += math.cos(math.radians(self.heading)) * self.thrust
        self.dy += math.sin(math.radians(self.heading)) * self.thrust
        self.x += self.dx
        self.y += self.dy

        # Border patrol
        self.border_check()

    def render(self, pen):
        """ Renders sprite after every update """

        # Renders the sprites
        pen.goto(self.x, self.y)
        pen.setheading(self.heading)
        pen.shape(self.shape)
        pen.color(self.color)
        pen.stamp()

        # Renders the health meter
        self.render_health_meter(pen)

    def border_check(self):
        # Creates a border
        if self.x > game.width / 2.0 - 10:
            self.x = game.width / 2.0 - 10
            self.dx *= -1
        if self.x < -game.width / 2.0 + 10:
            self.x = -game.width / 2.0 + 10
            self.dx *= -1
        if self.y > game.height / 2.0 - 10:
            self.y = game.height / 2.0 - 10
            self.dy *= -1
        if self.y < -game.height / 2.0 + 10:
            self.y = -game.height / 2.0 + 10
            self.dy *= -1
        

    def render_health_meter(self, pen):
        # Draw health meter
        pen.goto(self.x - 10, self.y + 20)
        pen.width(3)
        pen.pendown()
        pen.setheading(0)

        # Determines health bar color depending on current health
        if self.health / self.max_health < 0.3:
            pen.color("red")
        elif self.health / self.max_health < 0.7:
            pen.color("yellow")
        else:
            pen.color("green")
        pen.fd(20 * (self.health / self.max_health))
        
        # Creates a grey bar
        if self.health != self.max_health:
            pen.color("grey")
            pen.fd(20 * ((self.max_health - self.health) / self.max_health))
            
        # Stops drawing
        pen.penup()

class Player(Sprite):
    def __init__(self, x, y, shape, color):
        Sprite.__init__(self, 0, 0, shape, color)
        self.lives = 3
        self.score = 0
        self.heading = 90

    def rotate_left(self):
        # Rotates ship right
        self.da = 5

    def rotate_right(self):
        # Rotates ship right
        self.da = -5

    def stop_rotation(self):
        # Stops rotation
        self.da = 0

    def accelerate(self):
        # Accelerates ship
        self.thrust += self.acceleration

    def decelerate(self):
        # Stops ship acceleration
        self.thrust = 0

    def brake(self):
        # Stops the player completely
        self.thrust = 0
        self.dx = 0
        self.dy = 0

    def fire(self):
        # Fires a missile
        missile.fire(self.x, self.y, self.heading, self.dx, self.dy)

    def render(self, pen):
        # Renders ship
        pen.shapesize(0.5, 1, None)
        pen.goto(self.x, self.y)
        pen.setheading(self.heading)
        pen.shape(self.shape)
        pen.color(self.color)
        pen.stamp()
        pen.shapesize(1, 1, None)

        # Renders health meter
        self.render_health_meter(pen)

class Missile(Sprite):
    def __init__(self, x, y, shape, color):
        Sprite.__init__(self, x, y, shape, color)
        self.state = "ready"
        self.thrust = 4.0
        self.max_fuel = 200
        self.fuel = self.max_fuel

    def fire(self, x, y, heading, dx, dy):
        # Fires a missile
        self.state = "active"
        self.x = x
        self.y = y
        self.heading = heading
        self.dx = dx
        self.dy = dy

        self.dx += math.cos(math.radians(self.heading)) * self.thrust
        self.dy += math.sin(math.radians(self.heading)) * self.thrust
        
    def render(self, pen):
        # Renders missile
        if self.state == "active":
            pen.shapesize(0.2, 0.2, None)
            pen.goto(self.x, self.y)
            pen.setheading(self.heading)
            pen.shape(self.shape)
            pen.color(self.color)
            pen.stamp()

    def update(self):
        """ Updates position of missiles """ 
        if self.state == "active":
            self.fuel -= self.thrust
            if self.fuel <= 0:
                self.reset()
            
            # Rotates missile
            self.heading += self.da
            self.heading %= 360

            # Moves missle forward
            self.x += self.dx
            self.y += self.dy

            # Border patrol
            self.border_check()

    def reset(self):
        self.fuel = self.max_fuel
        self.dx = 0
        self.dy = 0
        self.state = "ready"
        

# Creates the game objects
game = Game(600, 300)

# Create player object
player = Player(100, 10, "triangle", "white")

# Create missle object
missile = Missile(0, 100, "circle", "yellow")

# Create enemy object
enemy = Sprite(0, 100, "square", "red")
enemy.dx = 0.5
enemy.dy = -0.4

# Create powerup object
powerup = Sprite(0, -100, "circle", "blue")
powerup.dx = -0.3
powerup.dy = 0.5

# Sprites list
sprites = []
sprites.append(player)
sprites.append(enemy)
sprites.append(powerup)
sprites.append(missile)

# Keyboard bindings
wn.listen()

# Rotating player
wn.onkeypress(player.rotate_left, "Left")
wn.onkeypress(player.rotate_right, "Right")
wn.onkeyrelease(player.stop_rotation, "Left")
wn.onkeyrelease(player.stop_rotation, "Right")

# Moving player
wn.onkeypress(player.accelerate, "Up")
wn.onkeyrelease(player.decelerate, "Up")
wn.onkeypress(player.brake, "Down")

# Firing missiles
wn.onkeypress(player.fire, "space")

# Main loop
while True:
    # Clear screen
    pen.clear()

    # Update sprites
    for sprite in sprites:
        sprite.update()
    
    # Render sprites
    for sprite in sprites:
        sprite.render(pen)

    # Render border
    game.render_border(pen)
    
    # Update screen
    wn.update()









































    
