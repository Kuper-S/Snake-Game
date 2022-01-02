import time
from turtle import Screen
from snake import Snake
from food import Food
from score import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
is_moving = True
while is_moving:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # distance method
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.add_score()

    if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285:
        score.reset()
        snake.reset()

    for snk in snake.all_snakes[1:]:
        if snake.head.distance(snk) < 10:
            score.reset()
            snake.reset()

screen.exitonclick()
