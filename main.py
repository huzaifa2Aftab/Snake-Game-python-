# import random
# import turtle
# from turtle import Turtle, Screen
# import time
#
# update = True
# screen = Screen()
# screen.bgcolor("black")
# screen.setup(width=600, height=600)
# positions = [(0, 0), (-20, 0), (-40, 0)]
# segments = []
# food = Turtle()
# food.penup()
# food.shape("circle")
# food.shapesize(1, 1)
# food.color("blue")
# screen.tracer(0)
# score = 0
# food_x = random.randint(-270, 270)
# food_y = random.randint(-270, 270)
# food.goto(food_x, food_y)
#
# print(food_x, food_y)
# for position in positions:
#     snake = Turtle('square')
#
#     snake.penup()
#     snake.color('white')
#     snake.penup()
#     snake.goto(position)
#     segments.append(snake)
#
# score_turtle = Turtle()
# score_turtle.penup()
# score_turtle.hideturtle()
# score_turtle.color('white')
# score_turtle.goto(0, 260)
#
#
# def left_moment():
#     segments[0].left(90)
#
#
# def right_moment():
#     segments[0].right(90)
#
#
# def check_collision():
#     global food_x, food_y, score
#     score_turtle.hideturtle()
#
#     x_2, y_2 = segments[0].position()
#     distance = abs(x_2 - food_x) + abs(y_2 - food_y)
#
#     if distance <= 30:
#         # for i in range(score):
#         food_x = random.randint(-270, 270)
#         food_y = random.randint(-270, 270)
#
#         food.goto(food_x, food_y)
#         new_segment = Turtle('square')
#         new_segment.penup()
#         new_segment.color('white')
#
#         segments.append(new_segment)
#         screen.tracer(0)
#         screen.update()
#         score_turtle.clear()
#         score += 1
#         score_turtle.write(f"Score: {score}", align='center', font=('Arial', 24, 'normal'))
#
#
# def check_wall():
#     x_2, y_2 = segments[0].position()
#     if x_2 > 280 or y_2 > 280 or x_2 < -280 or y_2 < -280:
#         score_turtle.clear()
#         screen.clear()
#         score_turtle.color("black")
#         score_turtle.write("Game Over", align='center', font=('Arial', 30, 'normal'))
#
#
# def check_snake_conclusion():
#     x_2, y_2 = segments[0].position()
#     for i in range(len(segments) - 1):
#         x_3, y_3 = segments[i + 1].position()
#         if x_3 == x_2 and y_3 == y_2:
#             score_turtle.clear()
#             screen.clear()
#             score_turtle.color("black")
#             score_turtle.write("Game Over", align='center', font=('Arial', 30, 'normal'))
#             break
#
#
# run = True
# while run:
#     screen.update()
#     time.sleep(.1)
#
#     for seg_num in range(len(segments) - 1, 0, -1):
#         new_x = segments[seg_num - 1].xcor()
#         new_y = segments[seg_num - 1].ycor()
#         segments[seg_num].goto(new_x, new_y)
#     segments[0].forward(20)
#     check_collision()
#     check_wall()
#     check_snake_conclusion()
#
#     screen.listen()
#
#     screen.onkey(right_moment, "d")
#     screen.onkey(left_moment, "a")
#
# screen.mainloop()
# screen.exitonclick()
from snake import Snake
import time
from turtle import Screen
from food import Food
from scoreboard import Score
# from collision import Collision
import random

screen = Screen()
screen.bgcolor('black')
screen.setup(width=600, height=600)
screen.tracer(0)
snake = Snake()
food = Food()
score = Score((-150, 270))
# wall = Wall()

screen.listen()
screen.onkeypress(snake.left, "a")
screen.onkeypress(snake.right, "d")

run = True
while run:
    x_1, y_1 = snake.head.pos()
    screen.update()
    time.sleep(.1)
    snake.move()

    if snake.head.distance(food) < 30:
        score.score_update()
        final_score = score.score_food
        snake.update_snake(final_score)
        screen.update()
        food.refresh()

    if x_1 > 280 or y_1 > 280 or x_1 < -280 or y_1 < -280:
        snake.reset()
        score.reset()

    if snake.check_self_collision():
        snake.reset()
        score.reset()


    # x_2, y_2 = snake.move()
    # distance = abs(x_2 - food_x) + abs(y_2 - food_y)

    # food.movement(random.randint(-270, 270), random.randint(-270, 270))

screen.exitonclick()
