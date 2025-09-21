from turtle import *


def move_up():
    """Control functions up"""
    y = left.ycor() + 15
    if y > 220:
        y = 220
    left.sety(y)

def move_down():
    """Control functions down"""
    y = left.ycor() - 15
    if y < -220:
        y = -220
    left.sety(y)

def set_screen(image,image2):
    """Initialize screen"""
    screen = Screen()
    screen.setup(800,600)
    screen.bgcolor("#FFBFF2")
    screen.title("Pong - Pride Edition")
    screen.addshape(image)
    screen.addshape(image2)
    return screen


def game_loop():
    """Set game loop"""
    #Create movement of ball
    #NOTES: here I was struggling with understanding the heading parameter,
    #especially since I was using a circle. But it's about which way the turtle is
    #turned, which is easier to see if you're using an arrow shape
    ball.left(150)
    new_heading_paddle = 0
    new_heading_ceiling = 0
    
    while True:

        #MOETNOG for testing dat ik dit groter zet, normaal is 1 goed
        ball.forward(5)
        left_y_lower = left.ycor() - 60
        left_y_upper = left.ycor() + 60
        right_y_lower = right.ycor() - 60
        right_y_upper = right.ycor() + 60
        right.sety(ball.ycor())
        old_heading = ball.heading()
       
        #Bounce ball from ceiling
        if ball.ycor() <= -300 or ball.ycor() >= 300:
            new_heading_ceiling = 360- ball.heading()
            ball.setheading(new_heading_ceiling)
            # print(f"BOUNCE FROM CEILING\nball x: {ball.xcor()}\nball y: {ball.ycor()}\nball old heading: {old_heading}\n"
            #         f"bal new heading: {new_heading_ceiling}\nleft x: {left.xcor()}\nright x:{right.xcor()}\n"
            # f"left y: {left.ycor()}\nleft y lower: {left_y_lower}\nleft y upper: {left_y_upper}\n"
            # f"right y: {right.ycor()}\nright y lower:{right_y_lower}\nright y upper:{right_y_upper}\n\n") 
            continue

        #Bounce ball from paddle
        if(((-385.0 <= ball.xcor() <= -375.0) and (left_y_lower <= ball.ycor() <= left_y_upper)) or 
        ((375.0 <= ball.xcor() <= 385.0) and (right_y_lower <= ball.ycor() <= right_y_upper))):
            new_heading_paddle = abs(ball.heading() - 180.0)
            ball.setheading(new_heading_paddle)
            # print(f"BOUNCE FROM PADDLE\nball x: {ball.xcor()}\nball y: {ball.ycor()}\nball old heading: {old_heading}\n"
            #         f"bal new heading: {new_heading_ceiling}\nleft x: {left.xcor()}\nright x:{right.xcor()}\n"
            # f"left y: {left.ycor()}\nleft y lower: {left_y_lower}\nleft y upper: {left_y_upper}\n"
            # f"right y: {right.ycor()}\nright y lower:{right_y_lower}\nright y upper:{right_y_upper}\n\n") 
            continue
        
        #Game Over
        if ball.xcor() > 400 or ball.xcor() < -400:
            x = screen.textinput(title="GAME OVER", prompt="Do you want to play again (y/n): ")
            # print(f"GAME OVER\nball x: {ball.xcor()}\nball y: {ball.ycor()}\nball old heading: {old_heading}\n"
            #         f"bal new heading: {new_heading_ceiling}\nleft x: {left.xcor()}\nright x:{right.xcor()}\n"
            # f"left y: {left.ycor()}\nleft y lower: {left_y_lower}\nleft y upper: {left_y_upper}\n"
            # f"right y: {right.ycor()}\nright y lower:{right_y_lower}\nright y upper:{right_y_upper}\n\n") 
            if x == "y":
                #MOETNOG dit werkt nog niet
                ball.home
            if x == "n":
                screen.bye()
                break


def main():
    #Link control functions to keyboard keys
    screen.onkeypress(move_up, "Up")
    screen.onkeypress(move_down,"Down")
    screen.listen()
    game_loop()       
    screen.mainloop()


if __name__ == "__main__":
    image = "pride_flag.gif"
    image2 = "unicorn.gif"
    screen = set_screen(image,image2)

    #Initialize turtles
    left = Turtle()
    left.hideturtle() 
    left.penup() 
    left.shape(image)
    left.setx(-380)
    left.showturtle()

    right = Turtle()
    right.hideturtle() 
    right.penup() 
    right.shape(image)
    right.setx(380)
    right.showturtle()

    #Add ball
    ball = Turtle()
    ball.penup()
    ball.shape(image2)
    ball.home()
    ball.speed(0) 

    main()






