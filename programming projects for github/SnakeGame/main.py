from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time



screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My snake game')
screen.tracer(0)



snake = Snake()
food = Food()
scoreboard = ScoreBoard()

# scoreboard.write_score()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")




game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.075)

    snake.move()

    #detect collison with food
    if snake.head.distance(food) < 20:
        food.refresh()
        for i in range(10):
            snake.extend()
        # snake.extend()
        # snake.extend()
        scoreboard.increase_score()

    #detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        snake.head.color('red')
        scoreboard.game_over()

    #detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            segment.color('red')
            scoreboard.game_over()
    #if head collides with any segment in the tail:
        # trigger game_over

screen.exitonclick()