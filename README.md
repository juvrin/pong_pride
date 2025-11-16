# Pong Pride Edition

Pong Pride Edition is a version of the classic pong game with a pride theme. This is a simple single player version in which you use a rainbow paddle to bounce a unicorn-shaped ball around. The game was built using the Turtle module in Python. 

![Pong screenshot](/img/screenshot.png)

## Background

I was interested in recreating this classic since as a novice coder it was challenging enough to learn but not too challenging to get discouraged. This project was used as a final project for the Harvard CS50 Introduction to Programming with Python course.

## Getting started

Download the repository to your computer. Use the up and down arrow keys to control the left paddle.


## How It's Made

The Turtle module in Python 3.13.7 was used. A screen is created as an instance of the Screen class and two paddles and a ball are created as instances of the Turtle class. In the game loop, an infinite while loop keeps the game in play. During game play, the while loop can be exited by pressing the ‘q’ key. The left paddle is the player's paddle which is controlled with the up and down arrow keys. The x- and y-coordinates of the ball are used to check whether the ball hits the borders of the screen or a paddle. If either of these things happen the ball will bounce back. If the ball exits the screen on the left or right side, the ball is “out” (pun intended) and subsequently the scores are updated and the game continues. A popup appears when either the player or the computer scores 10 points and the player can then choose to stop or continue the game. 


## Roadmap

- Change paddle behaviour to make it more similar to that of the original game (e.g. ball bounces off paddle with different angles, ball has a variable speed).

- Create a two-player version.

- Add different levels (easy, intermediate, hard).

- Add a pause button.



## Lessons learned

This project has challenged me to work with the Turtle module and to further advance my problem-solving skills. It also allowed me to practice my Python skills and to apply what I've learned so far. Furthermore, it was an interesting first step into tackling a project on my own and keeping momentum going.
## Contact

Jules Vrinten https://www.linkedin.com/in/jules-vrinten/ 
https://github.com/juvrin ~


## License

[MIT](https://choosealicense.com/licenses/mit/)
