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

    my.up()
    my.goto(-200, 180)
    my.write('Начало', align='center', font=("Arial", 13, "normal"))
    my.goto(-100, 180)
    my.write('1', align='center', font=("Arial", 13, "normal"))
    my.goto(0, 180)
    my.write('2', align='center', font=("Arial", 13, "normal"))
    my.goto(100, 180)
    my.write('3', align='center', font=("Arial", 13, "normal"))
    my.goto(200, 180)
    my.write('4', align='center', font=("Arial", 13, "normal"))
    my.goto(200, 80)
    my.write('5', align='center', font=("Arial", 13, "normal"))
    my.goto(200, -20)
    my.write('6', align='center', font=("Arial", 13, "normal"))
    my.goto(200, -120)
    my.write('7', align='center', font=("Arial", 13, "normal"))
    my.goto(100, -120)
    my.write('8', align='center', font=("Arial", 13, "normal"))
    my.goto(0, -120)
    my.write('9', align='center', font=("Arial", 13, "normal"))
    my.goto(-100, -120)
    my.write('10', align='center', font=("Arial", 13, "normal"))
    my.goto(-200, -120)
    my.write('11', align='center', font=("Arial", 13, "normal"))
    my.goto(-200, -20)
    my.write('12', align='center', font=("Arial", 13, "normal"))
    my.goto(-200, 80)
    my.write('13', align='center', font=("Arial", 13, "normal"))


if __name__ == '__main__':
    import turtle
    window = turtle.Screen()
    why()
    window.exitonclick()
