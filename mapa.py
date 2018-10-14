def why():
    import turtle
    my = turtle.Turtle()
    my.speed(0)
    my.hideturtle()

    my.up()
    my.goto(-250, 200)
    my.down()
    my.goto(250, 200)
    my.goto(250, -200)
    my.goto(-250, -200)
    my.goto(-250, 200)

    my.right(90)

    for i in range(5):
        my.forward(100)
        my.left(90)
        my.forward(100)
        my.left(90)
        my.forward(100)
        my.left(180)

    my.up()
    my.goto(-250, -200)
    my.down()

    my.left(180)

    for i in range(5):
        my.forward(100)
        my.right(90)
        my.forward(100)
        my.right(90)
        my.forward(100)
        my.right(180)

    my.forward(100)
    my.left(90)
    my.forward(100)
    my.right(90)

    for i in range(3):
        my.forward(100)
        my.right(90)
        my.forward(100)
        my.right(180)
        my.forward(100)
        my.right(90)

    my.left(90)
    my.forward(300)
    my.left(90)

    for i in range(3):
        my.forward(100)
        my.right(90)
        my.forward(100)
        my.right(180)
        my.forward(100)
        my.right(90)


if __name__ == '__main__':
    import turtle
    window = turtle.Screen()
    why()
    window.exitonclick()
