import turtle
from monopoly.mapa import *
import random


class Cell:
    """ Клас клетки. Имеет название, позицию на поле, цену покупки и владельца"""
    def __init__(self, title, position, price):
        self.owner = None
        self.name = title
        self.position = position
        self.price = price

    def info(self):
        print('{}. Позиция - {}. Цена - {}. Владелец - {}'.format(self.name, self.position, self.price, self.owner))

    def purchase(self, new_owner):
        """ Функция покупки клетки """
        if self.owner is None:
            self.owner = new_owner
            print('Клетка куплена игроком {}'.format(new_owner))
        else:
            print('Клетка имеет владельца!')


class Player:
    """ Игрок имеет начальную позицию=0, деньги=100 и передается имя"""
    def __init__(self, name):
        self.position = 0
        self.money = 100
        self.name = name

    def move(self, movement):
        """ Один ход. Позиция игрока += рандомное число"""
        self.position += movement
        print(self.position)
        print('Вы походили на {}'.format(movement))

        if self.position >= 14:  # таким образом начинаем круг сначала
            self.position -= 14  # позиции опять начинают считаться с нуль (20->0, 23->3)
            self.money += 100  # когда прошли круг - начисляются деньги

    def info(self):
        print('{}. Деньги - {}. Позиция {}.'.format(self.name, self.money, self.position))


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
    tur.goto(-115, 70-mistake)
    tur.stamp()
    tur.forward(20)
    tur.right(90)
    tur.forward(12)
    tur.left(90)
    tur.write(name, font=("Arial", 15, "normal"))
    # tur.goto(-200, 150)
    tur.goto(-214 + mistake, 165 - mistake)


def step(tur, player):
    """ Функция передвижения черепашек. Шаг - 100 единиц. 8 if'ов - 4 условия поворота для 2 черепашек """
    global my_index, field, players

    # выравниваем наших черепашек (чтобы они ходили по одной линии)
    if tur.position() == (-214, 165) or tur.position() == (-189, 140):
        tur.goto(-200, 150)

    n = random.randint(1, 5)  # ход на n клеток
    my_index ^= 1  # иди нахрен. меняю 0 на 1 и наоборот.
    # my_index = my_index ^ 1  # смена 0 на 1 и наоборот. придумал.
    # my_index = 1 if my_index == 0 else 0  # смена 0 на 1 и наоборот. ничего лучше не придумал

    tur.speed(1)
    for e in range(n):
        # графическое отображение ходов
        tur.forward(100)

        if (round(tur.xcor()) == 200 and round(tur.ycor()) == 150) \
                or (round(tur.xcor()) == 200 and round(tur.ycor()) == -150) \
                or (round(tur.xcor()) == -200 and round(tur.ycor()) == -150) \
                or (round(tur.xcor()) == -200 and round(tur.ycor()) == 150):
            tur.right(90)

    player.move(n)  # функциональный ход
    player.info()
    field[player.position].info()
    money_turtles[my_index].clear()  # чистим поле, там где деньги и записываем обновленные деньги
    money_turtles[my_index].write('$ {}'.format(player.money), font=("Arial", 15, "normal"))

    # графическое отображение инфы о клетке (Зачем?)

    # cell_info_turtle.clear()
    # cell_info_turtle.write('{}\nЦена: $ {}'.format(field[player.position].name, field[player.position].price),
    #                        font=("Arial", 13, "normal"))

    if field[player.position].position == 0:
        """Если это 0-клетка"""
        info_turtle.clear()
        info_turtle.write('Нет доступных действий на клетке "Старт"!', align='center', font=("Arial", 9, "normal"))
        money_turtles[my_index].clear()  # чистим поле, там где деньги и записываем обновленные деньги
        money_turtles[my_index].write('$ {}'.format(player.money), font=("Arial", 15, "normal"))

    else:
        if field[player.position].owner is None:
            """ Если клетка еще не куплена """
            while True:
                choose = window.textinput('Выбор действия', '[1] Купить [2] Пас')
                if choose == '1':
                    if player.money >= field[player.position].price:
                        # дальше - махинации с отпечатком черепашки на клетка для наглядности покупки
                        some_stamp_colors = ['CornflowerBlue', 'LightCoral', 'Red', 'Blue']
                        tur.turtlesize(2, 2, 10)
                        tur.shape('square')
                        tur.color(some_stamp_colors[my_index])
                        tur.stamp()
                        tur.shape('turtle')
                        tur.color(some_stamp_colors[3-my_index])
                        tur.turtlesize(1, 1, 1)

                        field[player.position].purchase(player.name)  # клетка теперь пренадлежит <ИМЯ ИГРОКА>
                        player.money -= field[player.position].price  # Забираем у игрока бабки=цена клетки

                        money_turtles[my_index].clear()  # чистим поле, там где деньги и записываем обновленные деньги
                        money_turtles[my_index].write('$ {}'.format(player.money), font=("Arial", 15, "normal"))

                        info_turtle.clear()
                        info_turtle.write('{} купил {}!'.format(player.name, field[player.position].name),
                                          align='center', font=("Arial", 9, "normal"))
                        break
                    else:
                        info_turtle.clear()
                        info_turtle.write('Недостаточно денег для покупки!', align='center',
                                          font=("Arial", 9, "normal"))
                        break

                elif choose == '2':
                    info_turtle.clear()
                    info_turtle.write('{} воздержался от покупки!'.format(player.name), align='center',
                                      font=("Arial", 9, "normal"))
                    break
                else:
                    continue

        elif field[player.position].owner == player.name:
            """ Если клетка уже куплена вами """
            info_turtle.clear()
            info_turtle.write('Вы попали на свою клетку!', align='center', font=("Arial", 9, "normal"))
            while True:
                choose = window.textinput('Выбор действия', '[1] Улучшить [2] Пас')
                # Тут будет функционал улучшение клетки. По типу постройки домов в оригинальной монополии
                # Но улучшать можно только когда вы на своей клетке
                if choose == '1':
                    info_turtle.clear()
                    info_turtle.write('Улучшения пока недоступны!', align='center', font=("Arial", 9, "normal"))
                    break
                elif choose == '2':
                    info_turtle.clear()
                    info_turtle.write('{} воздержался от улучшения!'.format(player.name), align='center',
                                      font=("Arial", 9, "normal"))
                    break
                else:
                    continue

        else:
            """ Если клетка куплена кем-то другим """

            rent = int(field[player.position].price * 0.1)  # арендая плата = 10% цены клетки

            if player.money < rent:
                print('{} проиграл'.format(player.name))

            else:
                player.money -= rent  # забираем у того, кто наступил на чужую клетку, бабки

                other_player = players[my_index]
                other_player.money += rent

                info_turtle.clear()
                info_turtle.write('{} заплатил {} {}$ за аренду'.format(player.name, other_player.name, rent),
                                  align='center', font=("Arial", 9, "normal"))

                money_turtles[my_index].clear()  # чистим поле, там где деньги и записываем обновленные деньги
                money_turtles[my_index].write('$ {}'.format(player.money), font=("Arial", 15, "normal"))

                money_turtles[my_index ^ 1].clear()  # так же и для другого игрока
                money_turtles[my_index ^ 1].write('$ {}'.format(other_player.money), font=("Arial", 15, "normal"))

    write_hod(teh_turtle, my_index)  # наглядность чей ход (зелененькая стрелочка возле черепашки)
    window.listen()


def write_hod(t_t, mi):
    # указатель на черепашку, чей сейчас ход
    if mi == 0:
        t_t.goto(-130, 70)
    else:
        t_t.goto(-130, 45)


def create_turtle():
    """ функция создания черепашек с нужными настройками. не использую turtle.clone(), ибо при t.clear() идет очистка
        всего (объекты ссылаются друг на друга?) """
    new_turtle = turtle.Turtle()
    new_turtle.speed(0)
    new_turtle.up()
    new_turtle.hideturtle()
    return new_turtle


if __name__ == '__main__':

    teh_turtle = create_turtle()
    money_turtle_1 = create_turtle()
    money_turtle_2 = create_turtle()
    info_turtle = create_turtle()
    cell_info_turtle = create_turtle()

    info_turtle.goto(-0, -93)
    cell_info_turtle.goto(20, -70)
    info_turtle.write('Добро пожаловать!', align='center', font=("Arial", 9, "normal"))

    # каждой черепашке, ответсвенной за деньги даем свой цвет, координаты. Записываем начальный капитал.
    teh_turtle.color('dark green')
    money_turtle_1.color('Red')
    money_turtle_2.color('Blue')

    money_turtles = [money_turtle_2, money_turtle_1]  # созд. список, чтобы с помощью my_index вызывать нужную черепашку

    cell_0 = Cell('0-клетка', 0, None)
    cell_1 = Cell('1-клетка', 1, 10)
    cell_2 = Cell('2-клетка', 2, 15)
    cell_3 = Cell('3-клетка', 3, 20)
    cell_4 = Cell('4-клетка', 4, 25)
    cell_5 = Cell('5-клетка', 5, 30)
    cell_6 = Cell('6-клетка', 6, 35)
    cell_7 = Cell('7-клетка', 7, 40)
    cell_8 = Cell('8-клетка', 8, 45)
    cell_9 = Cell('9-клетка', 9, 50)
    cell_10 = Cell('10-клетка', 10, 55)
    cell_11 = Cell('11-клетка', 11, 60)
    cell_12 = Cell('12-клетка', 12, 65)
    cell_13 = Cell('13-клетка', 13, 70)
    cell_14 = Cell('14-клетка', 14, 75)
    field = [cell_0, cell_1, cell_2, cell_3, cell_4, cell_5, cell_6, cell_7, cell_8, cell_9, cell_10,
             cell_11, cell_12, cell_13, cell_14]
    # Создаем окно
    window = turtle.Screen()
    window.colormode(255)
    window.bgcolor(245, 255, 245)

    why()  # ваау. рисуем каждый раз новую карту при запуске программы ( не смог в скрин (пиксели неточные) )
    # window.bgpic('Screenshot_2.png') - так должно быть в идеале. используем бекграунд пикчу как карту

    # В окне запрашиваем имена игроков
    name_1 = window.textinput('Монополия', 'Введите имя первого игрока:')
    name_2 = window.textinput('Монополия', 'Введите имя второго игрока:')

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

    # пишем начальный кэш каждого игрока
    money_turtle_1.goto(50, 58)
    money_turtle_2.goto(50, 33)
    money_turtle_1.write('$ 100', font=("Arial", 15, "normal"))
    money_turtle_2.write('$ 100', font=("Arial", 15, "normal"))

    my_index = 0  # типа переключатель (см. функцию step)
    write_hod(teh_turtle, my_index)
    teh_turtle.showturtle()  # теперь видно кто ходит первый
    window.onkeypress(lambda: step(turtles[my_index], players[my_index]), 'g')
    # window.onkeypress(lambda: step(turtle_1, random.randint(1, 5)), 'g')
    # window.onkeypress(lambda: step(turtle_2, random.randint(1, 5)), 'h')
    window.listen()

    window.exitonclick()
