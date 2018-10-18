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


    my.goto(-199, 102)
    my.write('+100$ каждый круг', align='center', font=("Arial", 8, "normal"))

    my.goto(-100, 102)
    my.write('10$', align='center', font=("Arial", 10, "normal"))

    my.goto(0, 102)
    my.write('15$', align='center', font=("Arial", 10, "normal"))

    my.goto(100, 102)
    my.write('20$', align='center', font=("Arial", 10, "normal"))

    my.goto(200, 102)
    my.write('25$', align='center', font=("Arial", 10, "normal"))

    my.goto(200, 2)
    my.write('30$', align='center', font=("Arial", 10, "normal"))

    my.goto(200, -98)
    my.write('35$', align='center', font=("Arial", 10, "normal"))

    my.goto(200, -198)
    my.write('40$', align='center', font=("Arial", 10, "normal"))

    my.goto(100, -198)
    my.write('45$', align='center', font=("Arial", 10, "normal"))

    my.goto(0, -198)
    my.write('50$', align='center', font=("Arial", 10, "normal"))

    my.goto(-100, -198)
    my.write('55$', align='center', font=("Arial", 10, "normal"))

    my.goto(-200, -198)
    my.write('60$', align='center', font=("Arial", 10, "normal"))

    my.goto(-200, -98)
    my.write('65$', align='center', font=("Arial", 10, "normal"))

    my.goto(-200, 2)
    my.write('70$', align='center', font=("Arial", 10, "normal"))

    my.goto(0, 212)
    my.color('Red')
    my.begin_fill()

    my.setheading(0)
    my.forward(116)
    my.left(90)
    my.forward(38)
    my.left(90)
    my.forward(232)
    my.left(90)
    my.forward(38)
    my.left(90)
    my.forward(116)

    my.end_fill()
    my.color('white')
    my.write('МОНОПОЛИЯ', align="center", font=("Arial", 25, "bold"))


if __name__ == '__main__':
    import turtle
    window = turtle.Screen()
    window.colormode(255)
    window.bgcolor(245, 255, 245)
    why()
    window.exitonclick()
