# Turtle race
# Make program repeat after race is complete

import turtle
import random

wn = turtle.Screen()
wn.setup(width=800, height=600)
wn.title("Turtle Race!")
wn.bgcolor("black")
wn.tracer(0)

pen = turtle.Turtle()
pen.penup()
pen.hideturtle()
pen.speed(0)

class Racers():
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.heading = 90
        self.dy = random.randrange(5, 20, 1) / 100
        self.score = 0

    def update(self):
        self.y += self.dy

    def render(self, pen):
        pen.shape("turtle")
        pen.shapesize(stretch_wid=0.8,stretch_len=None)
        pen.setheading(self.heading)
        pen.color(self.color)
        pen.goto(self.x, self.y)
        pen.stamp()

        pen.clear()
        pen.goto(self.x, self.y - 20)
        pen.write("{}".format(self.score), align='center', font=("Courier", 8, 'normal'))
        
    def reset(self):
        if self.y > 285:
            self.score += 1
            for racer in racers:
                racer.y = 0
                racer.dy = random.randrange(5, 20, 1) / 100

racer_1 = Racers(0, 0, "green")
racer_2 = Racers(100, 0, "white")
racer_3 = Racers(-100, 0, "red")
racer_4 = Racers(50, 0, "aqua")
racer_5 = Racers(-50, 0, "yellow")

racers = []
racers.append(racer_1)
racers.append(racer_2)
racers.append(racer_3)
racers.append(racer_4)
racers.append(racer_5)

# Main loop

while True:
    pen.clear()

    for racer in racers:
        racer.update()
        racer.render(pen)
        racer.reset()

    wn.update()
















