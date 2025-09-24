from turtle import Turtle, Screen
from random import randint
import sys


class Graphics():
    """Model the screen"""

    def __init__(self):
        """Initialize attributes of screen"""
        self.screen = Screen()
        self.screen.setup(800,600)
        self.screen.bgcolor("#FFBFF2")
        self.screen.title("Pong - Pride Edition")
        self.screen.addshape(image)
        self.screen.addshape(image2)

class Paddles:
    """Parent class for both paddes"""

    def __init__(self, setx):
        """Initialize attributes of paddles"""
        self.turtle = Turtle()
        self.turtle.hideturtle() 
        self.turtle.penup() 
        self.turtle.shape(image)
        self.turtle.setx(setx)
        self.turtle.showturtle()
    
class Ball():
    """Class to model the ball/unicorn"""

    def __init__(self):
        """Initialize attributes ball"""
        self.turtle = Turtle()
        self.turtle.penup()
        self.turtle.shape(image2)
        self.turtle.home()
        self.turtle.speed(0) 

class Scores():
    """Class for the scores of player and computer"""

    def __init__(self):
        """Initialize score attributes"""
        self.turtle = Turtle()
        self.turtle.hideturtle()
        self.turtle.penup()
        self.turtle.goto(-250, 270)
    
    def get_scores(self, player_score, comp_score):
        """Reset scores and write scors to screen again."""
        self.turtle.reset()
        self.turtle.hideturtle()
        self.turtle.penup()
        self.turtle.goto(-250, 270)
        return self.turtle.write(f"Player: {player_score} Computer: {comp_score}", align = "center", font= ("Courier", 16, "bold"))  

def move_up():
    """Control functions up"""
    y = left.turtle.ycor() + 15
    if y > 220:
        y = 220
    left.turtle.sety(y)

def move_down():
    """Control functions down"""
    y = left.turtle.ycor() - 15
    if y < -220:
        y = -220
    left.turtle.sety(y)

def esc():
    """Exit screen and terminate execution"""
    graphics.screen.bye()
    sys.exit(0)

def random_header():
    """Random direction/header of the ball"""
    quadrant = randint(0,3)
    match quadrant:
        case 0:
            rand_head = randint(0,45)
        case 1:
            rand_head = randint(135,180)
        case 2:
            rand_head = randint(180,225)
        case 3:
            rand_head = randint(315,360)
    return rand_head

def game_loop():
    """Set game loop"""

    #Create initial movement of ball
    rand_head = random_header()
    ball.turtle.setheading(rand_head)
    new_heading_paddle = 0
    new_heading_ceiling = 0
    player_score = 0
    comp_score = 0
    print(scores.get_scores(player_score,comp_score))

    while True:
        #MOETNOG for testing dat ik dit groter zet, normaal is 1 goed
        ball.turtle.forward(5)
        left_y_lower = left.turtle.ycor() - 60
        left_y_upper = left.turtle.ycor() + 60
        right_y_lower = right.turtle.ycor() - 60
        right_y_upper = right.turtle.ycor() + 60
        right.turtle.sety(ball.turtle.ycor())
        
        #Bounce ball from ceiling
        if ball.turtle.ycor() <= -300 or ball.turtle.ycor() >= 300:
            new_heading_ceiling = 360- ball.turtle.heading()
            ball.turtle.setheading(new_heading_ceiling)
            continue

        #Bounce ball from paddle
        if(((-385.0 <= ball.turtle.xcor() <= -375.0) and (left_y_lower <= ball.turtle.ycor() <= left_y_upper)) or 
        ((375.0 <= ball.turtle.xcor() <= 385.0) and (right_y_lower <= ball.turtle.ycor() <= right_y_upper))):
            new_heading_paddle = abs(ball.turtle.heading() - 180.0)
            ball.turtle.setheading(new_heading_paddle)
            continue
        
        #Scores
        if ball.turtle.xcor() > 400:
            player_score += 1    
            ball.turtle.home()
            rand_head = random_header()
            ball.turtle.setheading(rand_head)
            left.turtle.sety(0)
            scores.get_scores(player_score,comp_score)
            continue

        if ball.turtle.xcor() < -400:
            comp_score += 1
            ball.turtle.home()
            rand_head = random_header()
            ball.turtle.setheading(rand_head)
            left.turtle.sety(0)
            scores.get_scores(player_score,comp_score)
            continue

        #Game Over
        #MOETNOG for testing op 2 gezet maar beide scores moeten op == 10 staan
        if player_score == 2  or comp_score == 2:
            x = graphics.screen.textinput(title="GAME OVER", prompt="Do you want to play again (y/n): ")
            print(x)
            if x == "y":
                #MOETNOG dit werkt helemaal niet en de keyboard controls werken niet als je opnieuw speelt
                ball.turtle.home()
                rand_head = random_header()
                ball.turtle.setheading(rand_head)
                left.turtle.sety(0)
                continue
            elif x == "n":
                esc()
                break


def main():
    """Link control functions to keyboard keys"""
    graphics.screen.listen()
    graphics.screen.onkeypress(move_up, "Up")
    graphics.screen.onkeypress(move_down,"Down")
    graphics.screen.onkeypress(esc, "q")
    game_loop()       
    graphics.screen.mainloop()


if __name__ == "__main__":
    image = "pride_flag.gif"
    image2 = "unicorn.gif"
    
    #Initialize screen, paddles and ball
    graphics = Graphics()
    left = Paddles(-380)
    right = Paddles(380)
    ball = Ball()
    scores = Scores()
    
    main()






