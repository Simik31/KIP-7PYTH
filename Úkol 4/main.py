import turtle as t


def square(x, d, depth):
    if d is depth:
        for _ in range(4):
            t.forward(x)
            t.right(90)
            square(x / 2, d - 1, depth)
    else:
        for _ in range(3):
            t.forward(x)
            if d > 0:
                t.right(90)
                square(x / 2, d - 1, depth)
            else:
                t.left(90)
        t.forward(x)
        t.right(90)


# depth 1 - 6
depth = 6

t.shape("turtle")
t.bgcolor("black")
t.goto(-100, -100)
t.color("white", "white")
t.begin_fill()
square(200, depth, depth)
t.end_fill()
t.home()
t.exitonclick()
