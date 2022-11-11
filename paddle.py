from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, pos_tuple):
        super().__init__()
        self.create_paddle()
        self.goto(pos_tuple)

    def create_paddle(self):
        self.shape("square")
        self.shapesize(5, 1)
        self.color("white")
        self.penup()
        self.speed("fastest")

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)



