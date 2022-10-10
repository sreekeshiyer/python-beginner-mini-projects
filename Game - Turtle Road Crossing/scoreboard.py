from turtle import Turtle

FONT = ("Courier", 18, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.pu()
        self.level = 1
        self.goto(x=-235, y=270)
        self.update_score()
        
    def update_score(self):
        self.clear()    # Clear scoreboard
        self.write(f"Level: {self.level}", align="center", font=FONT)   # Write new level
        
    def increase_level(self):
        self.level += 1 # Increase level by 1
        self.update_score() # Update scoreboard by calling function
        
    def game_over(self):
        self.home()
        self.write("GAME OVER.", align="center", font=FONT) # Display game over once game ends