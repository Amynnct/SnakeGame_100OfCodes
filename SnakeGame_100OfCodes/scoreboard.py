from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0, 280)
        self.color("white")
        self.hideturtle()
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        super().clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Courier"))
    
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
    
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()
    
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", align="center", font=("Courier"))