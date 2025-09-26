import pytest
from turtles import *


@pytest.fixture
def graphics():
    image = "pride_flag.gif"
    image2 = "unicorn.gif"
    graphics = Graphics(image,image2)
    return graphics

@pytest.fixture
def left(graphics):
    image = "pride_flag.gif"
    graphics.screen.addshape(image)
    left = Paddles(-380, image)
    return left

@pytest.fixture
def ball(graphics):
    image2 = "unicorn.gif"
    graphics.screen.addshape(image2)
    ball = Ball(image2)
    return ball 

def test_reset_game(ball, left):
    reset_game(ball, left)
    assert left.turtle.ycor() == 0
    assert ball.turtle.xcor() == 0

def test_graphics(graphics):
    assert graphics.screen.screensize() == (400,300)

def test_random_header():
    rand_head = random_header()
    assert 0 <= rand_head <= 360

def test_move_up(left):
    move_up(left)
    assert left.turtle.ycor() == 15

def main():
    test_reset_game()
    test_graphics()
    test_random_header()
    test_move_up()

if __name__ == "__main__":
    main()
