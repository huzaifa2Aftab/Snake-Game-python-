from turtle import Turtle

DISTANCE = 20
POSITION = [(0, 0), (-20, 0), (-40, 0)]


class Snake:

    def __init__(self):
        self.segments = []
        self.pos()
        self.head = self.segments[0]

    def pos(self):
        for position in POSITION:
            snake_1 = Turtle("square")
            snake_1.penup()
            snake_1.color("white")
            snake_1.goto(position)
            # snake_2 = Turtle("square")
            # snake_2.penup()
            # snake_2.color("white")
            self.segments.append(snake_1)

    def update_snake(self, final_score):
        for segment in range(final_score):
            snake_2 = Turtle("square")
            snake_2.penup()
            snake_2.color("white")
            snake_2.goto(self.segments[-1].pos())
            self.segments.append(snake_2)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(DISTANCE)

    def check_self_collision(self):
        for segment in self.segments[1:]:  # Skip the head
            if self.head.distance(segment) < 10:
                return True

    def reset(self):
        for segment in self.segments:
            segment.goto(1000, 1000)
        self.segments.clear()
        self.pos()
        self.head = self.segments[0]




    def left(self):
        self.head.left(90)

    def right(self):
        self.head.right(90)
