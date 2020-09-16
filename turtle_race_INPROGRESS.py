# Turtle race

import turtle

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
        self.dy = 0.05

    def update(self):
        self.y += self.dy

    def render(self, pen):
        pen.shape("turtle")
        pen.shapesize(stretch_wid=0.8,stretch_len=None)
        pen.setheading(self.heading)
        pen.color(self.color)
        pen.goto(self.x, self.y)
        pen.stamp()

racer_1 = Racers(0, 0, "green")

racers = []
racers.append(racer_1)

# Main loop
while True:
    pen.clear()

    for racer in racers:
        racer.update()

    for racer in racers:
        racer.render(pen)

    wn.update()
