from turtle import Screen
from snake import Snake
from scoreboard import Score
import time
from food import Food


screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor('black')
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


is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 15:
        snake.create_snake1()
        food.refresh()
        score.increase()


    #detect collision with wall
    if snake.head.xcor() > 280 or snake.head.ycor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280:
        is_game_on = False
        score.game_over()

    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            score.game_over()
            is_game_on = False




screen.exitonclick()

