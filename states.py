from turtle import Turtle

class States(Turtle):

    def __init__(self):
        super().__init__()


    def correct(self, state, x, y):
        self.penup()
        self.hideturtle()
        self.goto(x, y)
        self.write(f"{state}", align="center", font=("Arial", 8, "normal"))
