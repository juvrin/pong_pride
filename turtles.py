from turtle import Turtle, Screen
from random import randint
import sys

class Graphics():
    """Model the screen"""

    def __init__(self,image,image2):
        """Initialize attributes of screen"""
        self.screen = Screen()
        self.screen.setup(800,600)
        self.screen.bgcolor("#FFBFF2")
        self.screen.title("Pong - Pride Edition")
        self.screen.addshape(image)
        self.screen.addshape(image2)

class Paddles:
    """Parent class for both paddes"""

    def __init__(self, setx, image):
        """Initialize attributes of paddles"""
        self.turtle = Turtle()
        self.turtle.hideturtle() 
        self.turtle.penup() 
        self.turtle.shape(image)
        self.turtle.setx(setx)
        self.turtle.showturtle()
    
class Ball():
    """Class to model the ball/unicorn"""

    def __init__(self,image2):
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

def move_up(left):
    """Control functions up"""
    y = left.turtle.ycor() + 15
    if y > 220:
        y = 220
    left.turtle.sety(y)

def move_down(left):
    """Control functions down"""
    y = left.turtle.ycor() - 15
    if y < -220:
        y = -220
    left.turtle.sety(y)

def esc(graphics):
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

def reset_game(ball, left):
    """Reset position and header of ball, reset positon of left paddle"""
    ball.turtle.home()
    rand_head = random_header()
    ball.turtle.setheading(rand_head)
    left.turtle.sety(0)

def game_loop(graphics, left, right, ball, scores):
    """Set game loop"""
    
    reset_game(ball, left)
    new_heading_paddle = 0
    new_heading_ceiling = 0
    player_score = 0
    comp_score = 0
    print(scores.get_scores(player_score,comp_score))

    while True:
        ball.turtle.forward(8)
        left_y_lower = left.turtle.ycor() - 60
        left_y_upper = left.turtle.ycor() + 60
        right_y_lower = right.turtle.ycor() - 60
        right_y_upper = right.turtle.ycor() + 60

        #Computer paddles copies ycor of ball
        if -220 < ball.turtle.ycor() < 220:
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
            reset_game(ball, left)
            scores.get_scores(player_score,comp_score)
            continue

        if ball.turtle.xcor() < -400:
            comp_score += 1
            reset_game(ball, left) 
            scores.get_scores(player_score,comp_score)
            continue

        #Game Over
        if player_score == 10  or comp_score == 10:
            x = graphics.screen.textinput(title="GAME OVER", prompt="Do you want to play again (y/n): ")
            if x == "y":
                main()
            elif x == None:
                esc(graphics) 
                break
            elif x == "n":
                esc(graphics)
                break

def main():
    """Link control functions to keyboard keys"""
    graphics.screen.listen()
    graphics.screen.onkeypress(lambda: move_up(left), "Up")
    graphics.screen.onkeypress(lambda: move_down(left),"Down")
    graphics.screen.onkeypress(lambda: esc(graphics), "q")
    game_loop(graphics, left, right, ball, scores)       
    graphics.screen.mainloop()


if __name__ == "__main__":
    image = "pride_flag.gif"
    image2 = "unicorn.gif"
    
    #Initialize screen, paddles and ball
    graphics = Graphics(image,image2)
    left = Paddles(-380,image)
    right = Paddles(380,image)
    ball = Ball(image2)
    scores = Scores()

    main()






