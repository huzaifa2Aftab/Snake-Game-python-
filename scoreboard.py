from turtle import Turtle


class Score(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.position = position
        self.score_food = 0
        with open("score.txt") as file:
            self.high_score = int(file.read())

        self.color("white")
        self.goto(position)
        self.update_food()
        self.hideturtle()

    def update_food(self):
        self.clear()  # Clear previous score before updating

        self.write(f"Score : {self.score_food}  High Score : {self.high_score}", align='center',
                   font=('Arial', 16, 'bold'))

    def score_update(self):
        self.score_food += 1
        self.update_food()

    def reset(self):
        if self.score_food > self.high_score:
            self.high_score = self.score_food
            with open("score.txt", "w") as file:
                file.write(f"{self.high_score}")

        self.score_food = 0
        self.update_food()
