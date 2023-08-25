from turtle import Turtle


class Snake:
    def __init__(self):
        self.starting_positions = [(0, 0), (-20, 0), (-40, 0)]
        self.segments = []
        self.directions = {"up": 90, "down": 270, "left": 180, "right": 0}
        self.direction = self.directions["right"]

        for position in self.starting_positions:
            self.add_segment(position)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            self.segments[seg_num].goto(self.segments[seg_num - 1].xcor(), self.segments[seg_num - 1].ycor())
        self.segments[0].forward(20)

    def up(self):
        if self.direction != self.directions["down"]:
            self.direction = self.directions["up"]
            self.segments[0].setheading(self.direction)

    def down(self):
        if self.direction != self.directions["up"]:
            self.direction = self.directions["down"]
            self.segments[0].setheading(self.direction)

    def left(self):
        if self.direction != self.directions["right"]:
            self.direction = self.directions["left"]
            self.segments[0].setheading(self.direction)

    def right(self):
        if self.direction != self.directions["left"]:
            self.direction = self.directions["right"]
            self.segments[0].setheading(self.direction)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())
