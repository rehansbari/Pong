from turtle import Turtle
UP = 90
DOWN = 270

class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(350, 0)
        self.shapesize(stretch_wid=5, stretch_len=1)


    def up(self):
        new_y = self.ycor() + 20
        self.goto((self.xcor(), new_y))

    def down(self):
        new_x = self.ycor() - 20
        self.goto((self.xcor(), new_y))