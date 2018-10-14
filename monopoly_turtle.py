import turtle
from monopoly.main import *
from monopoly.mapa import *
import random


def player_create(color):
    """ Создаем черепашек """
    player = turtle.Turtle()
    player.shape('turtle')
    player.color(color)
    player.speed(0)

    return player


def first_move(tur, mistake, name):
    """ Отпечатываем черепашку (для наглядности цвета игрока), записываем напротив имя игрока
     и занимаем начальную позицию (0 клетка) """
    tur.up()
    tur.goto(1, -mistake)
    tur.stamp()
    tur.forward(20)
    tur.right(90)
    tur.forward(12)
    tur.left(90)
    tur.write(name, font=("Arial", 15, "normal"))
    tur.goto(-214 + mistake, 165 - mistake)


def step(tur, n):
    """ Функция передвижения черепашек. Шаг - 100 единиц. 8 if'ов - 4 условия поворота для 2 черепашек """
    global my_index
    my_index = 1 if my_index == 0 else 0  # смена 0 на 1 и наоборот. ничего лучше не придумал

    tur.speed(1)
    for e in range(n):
        tur.forward(100)

        if (round(tur.xcor()) == 186 and round(tur.ycor()) == 165)\
                or (round(tur.xcor()) == 186 and round(tur.ycor()) == -135)\
                or (round(tur.xcor()) == -214 and round(tur.ycor()) == -135)\
                or (round(tur.xcor()) == -214 and round(tur.ycor()) == 165)\
                or (round(tur.xcor()) == 211 and round(tur.ycor()) == 140) \
                or (round(tur.xcor()) == 211 and round(tur.ycor()) == -160) \
                or (round(tur.xcor()) == -189 and round(tur.ycor()) == -160) \
                or (round(tur.xcor()) == -189 and round(tur.ycor()) == 140):
            tur.right(90)

        print('x -', tur.xcor())
        print('y -', tur.ycor())
        print()


if __name__ == '__main__':
    # Создаем окно
    window = turtle.Screen()

    why()  # ваау. рисуем каждый раз новую карту при запуске программы ( не смог в скрин (пиксели неточные) )
    # window.bgpic('Screenshot_2.png') - так должно быть в идеале. используем бекграунд пикчу как карту

    # В окне запрашиваем имена игроков
    name_1 = window.textinput('Monopoly', 'Name of first player')
    name_2 = window.textinput('Monopoly', 'Name of second player')

    # Функционал - создаем объекты игроков. Закидываем их в список, по которому будем итерировать для очередности ходов
    player_1 = Player(name_1)
    player_2 = Player(name_2)
    players = [player_1, player_2]
    player_1.info()
    player_2.info()

    # Создаем объекты черепашек
    turtle_1 = player_create('red')
    turtle_2 = player_create('blue')
    turtles = [turtle_1, turtle_2]

    # Делаем дефолтный первый мув
    first_move(turtle_1, 0, name_1)
    first_move(turtle_2, 25, name_2)

    my_index = 0  # типа переключатель (см. функцию step)
    window.onkeypress(lambda: step(turtles[my_index], random.randint(1, 5)), 'g')
    # window.onkeypress(lambda: step(turtle_1, random.randint(1, 5)), 'g')
    # window.onkeypress(lambda: step(turtle_2, random.randint(1, 5)), 'h')
    window.listen()

    window.exitonclick()
