class Cell:
    """ Клас клетки. Имеет название, позицию на поле, цену покупки и владельца"""
    def __init__(self, title, position, price, rent):
        self.owner = None
        self.name = title
        self.position = position
        self.price = price
        self.rent = rent
        self.upgrade_level = 0

    def info(self):
        pass
        # print('{}. Позиция - {}. Цена - {}. Владелец - {}'.format(self.name, self.position, self.price, self.owner))

    def purchase(self, new_owner):
        """ Функция покупки клетки """
        if self.owner is None:
            self.owner = new_owner
            # print('Клетка куплена игроком {}'.format(new_owner))
        else:
            pass
            # print('Клетка имеет владельца!')


class Player:
    """ Игрок имеет начальную позицию=0, деньги=100 и передается имя"""
    def __init__(self, name):
        self.position = 0
        self.money = 100
        self.name = name
        self.prison = False
        self.release = False

    def move(self, movement):
        """ Один ход. Позиция игрока += рандомное число"""
        self.position += movement
        # print(self.position)

        if self.position >= 14:  # таким образом начинаем круг сначала
            self.position -= 14  # позиции опять начинают считаться с нуль (14->0, 17->3)
            self.money += 100  # когда прошли круг - начисляются деньги

    def info(self):
        pass
        # print('{}. Деньги - {}. Позиция {}.'.format(self.name, self.money, self.position))


def why():
    import turtle
    my = turtle.Turtle()
    my.speed(0)
    my.hideturtle()

    my.color('#023A02')
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
    my.color('#032A03')
    my.write('Старт', align='center', font=("Arial", 13, "normal"))
    my.goto(-100, 180)
    my.write('1', align='center', font=("Arial", 13, "normal"))
    my.goto(0, 180)
    my.write('2', align='center', font=("Arial", 13, "normal"))
    my.goto(100, 180)
    my.write('3', align='center', font=("Arial", 13, "normal"))
    my.goto(200, 180)
    my.write('Казино', align='center', font=("Arial", 13, "normal"))
    my.goto(200, 80)
    my.write('5', align='center', font=("Arial", 13, "normal"))
    my.goto(200, -20)
    my.write('6', align='center', font=("Arial", 13, "normal"))
    my.goto(200, -120)
    my.write('Тюрьма', align='center', font=("Arial", 13, "normal"))
    my.goto(100, -120)
    my.write('8', align='center', font=("Arial", 13, "normal"))
    my.goto(0, -120)
    my.write('9', align='center', font=("Arial", 13, "normal"))
    my.goto(-100, -120)
    my.write('10', align='center', font=("Arial", 13, "normal"))
    my.goto(-200, -120)
    my.write('Налоговая', align='center', font=("Arial", 13, "normal"))
    my.goto(-200, -20)
    my.write('12', align='center', font=("Arial", 13, "normal"))
    my.goto(-200, 80)
    my.write('13', align='center', font=("Arial", 13, "normal"))

    my.goto(-199, 102)
    my.write('+100$ за круг!', align='center', font=("Arial", 9, "normal"))

    my.goto(-100, 102)
    my.write('10$', align='center', font=("Arial", 10, "normal"))

    my.goto(0, 102)
    my.write('20$', align='center', font=("Arial", 10, "normal"))

    my.goto(100, 102)
    my.write('30$', align='center', font=("Arial", 10, "normal"))

    my.goto(200, 102)
    my.write('Испытай удачу!', align='center', font=("Arial", 9, "normal"))

    my.goto(200, 2)
    my.write('40$', align='center', font=("Arial", 10, "normal"))

    my.goto(200, -98)
    my.write('50$', align='center', font=("Arial", 10, "normal"))

    my.goto(200, -198)
    my.write('Пропуск хода!', align='center', font=("Arial", 9, "normal"))

    my.goto(100, -198)
    my.write('60$', align='center', font=("Arial", 10, "normal"))

    my.goto(0, -198)
    my.write('70$', align='center', font=("Arial", 10, "normal"))

    my.goto(-100, -198)
    my.write('80$', align='center', font=("Arial", 10, "normal"))

    my.goto(-200, -198)
    my.write('Оплатите счет!', align='center', font=("Arial", 9, "normal"))

    my.goto(-200, -98)
    my.write('90$', align='center', font=("Arial", 10, "normal"))

    my.goto(-200, 2)
    my.write('100$', align='center', font=("Arial", 10, "normal"))

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
    tur.goto(-214 + mistake, 165 - mistake)


def step(tur, player):
    """ Функция передвижения черепашек. Шаг - 100 единиц. 8 if'ов - 4 условия поворота для 2 черепашек """
    global my_index, field, players

    # выравниваем наших черепашек (чтобы они ходили по одной линии)
    if tur.position() == (-214, 165) or tur.position() == (-189, 140):
        tur.goto(-200, 150)

    n = randint(1, 5)  # ход на n клеток

    if player.prison:
        n = 0
        player.prison = False
    # если игрок был в тюрьме - на этот ход он выходит и меняет цвет из серого на свой
    if player.release:
        tur.color(['red', 'blue'][my_index])
        player.release = False

    my_index ^= 1  # меняю 0 на 1 и наоборот.

    # графическое отображение ходов
    for e in range(n):
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

    if field[player.position].position == 0:
        # Если позиция - "Старт"
        info_turtle.clear()
        info_turtle.write('{} попал на клетку "Старт"!'.format(player.name), align='center',
                          font=("Arial", 9, "normal"))
        money_turtles[my_index].clear()  # чистим поле, там где деньги и записываем обновленные деньги
        money_turtles[my_index].write('$ {}'.format(player.money), font=("Arial", 15, "normal"))

    elif field[player.position].position == 4:
        # Если позиция - "Казино"
        while True:
            choose_kaz = window.textinput('Добро пожаловать в Казино!', '[1] Играть\n[2] Пас')
            if choose_kaz == '1':
                info_turtle.clear()
                info_turtle.write('{} зашел в Казино!'.format(player.name), align='center', font=("Arial", 9, "normal"))

                while True:
                    player_bet = window.textinput('Делайте Ваши ставки!', 'Введите сумму:')
                    try:
                        player_bet = int(player_bet)
                    except ValueError:
                        info_turtle.clear()
                        info_turtle.write('Введите корректную сумму!', align='center', font=("Arial", 9, "normal"))
                        continue

                    if player_bet > player.money:
                        # если ставка больше чем у вас денег
                        info_turtle.clear()
                        info_turtle.write('У Вас недостаточно денег!', align='center', font=("Arial", 9, "normal"))
                        continue

                    elif player_bet <= player.money:
                        # если ставка коректна
                        player.money -= player_bet

                        money_turtles[my_index].clear()  # чистим поле, там где деньги и записываем обновленные деньги
                        money_turtles[my_index].write('$ {}'.format(player.money), font=("Arial", 15, "normal"))

                        info_turtle.clear()
                        info_turtle.write('Идет игра!', align='center', font=("Arial", 9, "normal"))

                        winning = casino(player_bet)  # бабки + или -
                        player.money += winning

                        casino_turtle.up()
                        casino_turtle.goto(1, -51)
                        casino_turtle.color('#336F24')
                        casino_turtle.write('$', align='center', font=("Arial", 20, "bold"))
                        casino_turtle.goto(0, -60)
                        casino_turtle.down()
                        casino_turtle.color('gold')
                        casino_turtle.circle(25)
                        casino_turtle.color('#1D620C')
                        casino_turtle.circle(25)
                        # sleep(1)

                        if winning < player_bet:
                            info_turtle.clear()
                            info_turtle.write('{} проиграл {}$ в Казино!'.format(player.name, player_bet-winning),
                                              align='center', font=("Arial", 9, "normal"))

                        elif winning == player_bet:
                            info_turtle.clear()
                            info_turtle.write('{} сыграл в ничью с Казино!'.format(player.name),
                                              align='center', font=("Arial", 9, "normal"))

                        elif winning > player_bet:
                            info_turtle.clear()
                            info_turtle.write('{} выиграл {}$ в Казино!'.format(player.name, winning-player_bet),
                                              align='center', font=("Arial", 9, "normal"))

                        casino_turtle.clear()
                        money_turtles[my_index].clear()  # чистим поле, там где деньги и записываем обновленные деньги
                        money_turtles[my_index].write('$ {}'.format(player.money), font=("Arial", 15, "normal"))

                        break

                break

            elif choose_kaz == '2':
                info_turtle.clear()
                info_turtle.write('{} отказался играть в Казино!'.format(player.name), align='center',
                                  font=("Arial", 9, "normal"))
                break
            else:
                info_turtle.clear()
                info_turtle.write('Введите коректные данные!', align='center', font=("Arial", 9, "normal"))
                continue

    elif field[player.position].position == 7:
        # Если позиция - "Тюрьма"
        if n == 0:
            # tur.color(['red', 'blue'][my_index ^ 1])
            info_turtle.clear()
            info_turtle.write('{} сидит в тюрьме!'.format(player.name), align='center', font=("Arial", 9, "normal"))
            player.release = True
        else:
            tur.color('#4E4E4E')
            player.prison = True
            info_turtle.clear()
            info_turtle.write('{} попал в тюрьму!'.format(player.name), align='center', font=("Arial", 9, "normal"))

    elif field[player.position].position == 11:
        # Если позиция - "Налоговая"
        info_turtle.clear()
        info_turtle.write('{} попал в налоговую. Выписываем счёт!'.format(player.name), align='center',
                          font=("Arial", 9, "normal"))

        tax = 0
        # считаем сколько клеток пренадлежит игроку и заставляем оплатить 10 процентов от стоимости каждой
        # + игрок платит за каждый домик (апгрейд) по 1$
        for i in field:
            if i.owner == player.name:
                tax += int(i.price * 0.1) + int(i.upgrade_level*5)

        tax_visualize()  # визуализируем "$ $ $"

        if tax <= player.money:
            # если достаточно денег для оплаты
            player.money -= tax
            info_turtle.clear()
            info_turtle.write('{} оплатил счета на сумму {}$!'.format(player.name, tax), align='center',
                              font=("Arial", 9, "normal"))

            money_turtles[my_index].clear()  # чистим поле, там где деньги и записываем обновленные деньги
            money_turtles[my_index].write('$ {}'.format(player.money), font=("Arial", 15, "normal"))

        else:
            # если недостаточно денег для оплаты
            end_game(player)

    else:
        if field[player.position].owner is None:
            """ Если клетка еще не куплена """
            if player.money >= field[player.position].price:
                while True:
                    choose = window.textinput('Выбор действия', '[1] Купить за {}$\n[2] Пас'.
                                              format(field[player.position].price))
                    if choose == '1':
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

                    elif choose == '2':
                        info_turtle.clear()
                        info_turtle.write('{} воздержался от покупки!'.format(player.name), align='center',
                                          font=("Arial", 9, "normal"))
                        break
                    else:
                        info_turtle.clear()
                        info_turtle.write('Введите коректные данные!', align='center', font=("Arial", 9, "normal"))
                        continue
            else:
                info_turtle.clear()
                info_turtle.write('Недостаточно денег для покупки!', align='center', font=("Arial", 9, "normal"))

        elif field[player.position].owner == player.name:
            """ Если клетка уже куплена вами """
            info_turtle.clear()
            info_turtle.write('{} попал на свою клетку!'.format(player.name), align='center',
                              font=("Arial", 9, "normal"))
            while True:
                upgrade_price = field[player.position].rent * 2

                if field[player.position].upgrade_level == 5:
                    info_turtle.clear()
                    info_turtle.write('Да тут монополия максимального уровня!', align='center',
                                      font=("Arial", 9, "normal"))
                    break

                elif field[player.position].upgrade_level == 4:

                    monopoly = True
                    all_monopolies = [[1, 2, 3], [5, 6], [8, 9, 10], [12, 13]]

                    for m in all_monopolies:
                        if player.position in m:
                            for i in m:
                                if field[i].owner == player.name:
                                    pass
                                else:
                                    monopoly = False
                                    break

                    if monopoly:

                        monopoly_price = int(field[player.position].price*5)

                        if player.money >= monopoly_price:
                            choose_m = window.textinput('Выбор действия (М)', '[1] Улучшить за {}$\n[2] Пас'.
                                                        format(monopoly_price))
                            info_turtle.clear()
                            info_turtle.write('{} может сделать монополию!'.format(player.name),
                                              align='center', font=("Arial", 9, "normal"))

                            if choose_m == '1':
                                player.money -= monopoly_price
                                field[player.position].rent = int(field[player.position].rent*2)
                                monopolization(tur)
                                field[player.position].upgrade_level += 1

                                money_turtles[my_index].clear()
                                money_turtles[my_index].write('$ {}'.format(player.money), font=("Arial", 15, "normal"))
                                info_turtle.clear()
                                info_turtle.write('{} сделал монополию!'.format(player.name), align='center',
                                                  font=("Arial", 9, "normal"))
                                break

                            elif choose_m == '2':
                                info_turtle.clear()
                                info_turtle.write('{} воздержался от улучшения!'.format(player.name), align='center',
                                                  font=("Arial", 9, "normal"))
                                break

                            else:
                                info_turtle.clear()
                                info_turtle.write('Введите коректные данные!', align='center',
                                                  font=("Arial", 9, "normal"))
                                continue

                        elif player.money < monopoly_price:
                            info_turtle.clear()
                            info_turtle.write('{} недостаточно денег для монополии!'.format(player.name),
                                              align='center', font=("Arial", 9, "normal"))

                    else:
                        info_turtle.clear()
                        info_turtle.write('{} имеет максимальный уровень улучшения!'.
                                          format(field[player.position].name),
                                          align='center', font=("Arial", 9, "normal"))
                        break

                elif field[player.position].upgrade_level < 4:
                    choose = window.textinput('Выбор действия', '[1] Улучшить за {}$\n[2] Пас'.format(upgrade_price))
                    # Тут будет функционал улучшение клетки. По типу постройки домов в оригинальной монополии
                    # Но улучшать можно только когда вы на своей клетке

                    if choose == '1':
                        if player.money < upgrade_price:
                            info_turtle.clear()
                            info_turtle.write('Не хватает денег на улучшение!', align='center',
                                              font=("Arial", 9, "normal"))
                        else:
                            # если хватает денег на улучшение
                            upgrade_cell(tur, field[player.position].upgrade_level)  # рисуем улучшение

                            if field[player.position].upgrade_level == 0:
                                field[player.position].rent = int(field[player.position].rent*2)

                            elif field[player.position].upgrade_level == 1:
                                field[player.position].rent = int(field[player.position].rent*3/2)

                            elif field[player.position].upgrade_level == 2:
                                field[player.position].rent = int(field[player.position].rent*4/3)

                            elif field[player.position].upgrade_level == 3:
                                field[player.position].rent = int(field[player.position].rent*5/4)

                            field[player.position].upgrade_level += 1
                            player.money -= upgrade_price

                            info_turtle.clear()
                            info_turtle.write('{} улучшил {} за {}!'.format(player.name, field[player.position].name,
                                              upgrade_price), align='center', font=("Arial", 9, "normal"))

                            money_turtles[my_index].clear()
                            money_turtles[my_index].write('$ {}'.format(player.money), font=("Arial", 15, "normal"))

                        break
                    elif choose == '2':
                        info_turtle.clear()
                        info_turtle.write('{} воздержался от улучшения!'.format(player.name), align='center',
                                          font=("Arial", 9, "normal"))
                        break
                    else:
                        info_turtle.clear()
                        info_turtle.write('Введите коректные данные!', align='center', font=("Arial", 9, "normal"))
                        continue

        else:
            """ Если клетка куплена кем-то другим """
            rent = field[player.position].rent

            if player.money < rent:
                end_game(player)

            else:
                player.money -= rent  # забираем у того, кто наступил на чужую клетку, бабки

                other_player = players[my_index]

                if other_player.position == 7:
                    # если владелец клетки в тюрьме - мы ему не платим!
                    info_turtle.clear()
                    info_turtle.write('Владелец в тюрьме!', align='center', font=("Arial", 9, "normal"))
                else:
                    other_player.money += rent
                    info_turtle.clear()
                    info_turtle.write('{} заплатил {} {}$ за аренду!'.format(player.name, other_player.name, rent),
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


def upgrade_cell(t, lvl):
    """ Улучшение клетки """
    upgrade_stamp_colors = ['#66D5B3', '#F8DE8D', 'Red', 'Blue']
    if lvl == 0:
        t.goto(t.xcor() - 10, t.ycor() + 10)
        t.shape('square')
        t.color(upgrade_stamp_colors[my_index])
        t.stamp()
        t.color(upgrade_stamp_colors[3 - my_index])
        t.shape('turtle')
        t.goto(t.xcor() + 10, t.ycor() - 10)

    elif lvl == 1:
        t.goto(t.xcor() + 10, t.ycor() + 10)
        t.shape('square')
        t.color(upgrade_stamp_colors[my_index])
        t.stamp()
        t.color(upgrade_stamp_colors[3 - my_index])
        t.shape('turtle')
        t.goto(t.xcor() - 10, t.ycor() - 10)

    elif lvl == 2:
        t.goto(t.xcor() + 10, t.ycor() - 10)
        t.shape('square')
        t.color(upgrade_stamp_colors[my_index])
        t.stamp()
        t.color(upgrade_stamp_colors[3 - my_index])
        t.shape('turtle')
        t.goto(t.xcor() - 10, t.ycor() + 10)

    elif lvl == 3:
        t.goto(t.xcor() - 10, t.ycor() - 10)
        t.shape('square')
        t.color(upgrade_stamp_colors[my_index])
        t.stamp()
        t.color(upgrade_stamp_colors[3 - my_index])
        t.shape('turtle')
        t.goto(t.xcor() + 10, t.ycor() + 10)


def create_turtle():
    """ функция создания черепашек с нужными настройками. не использую turtle.clone(), ибо при t.clear() идет очистка
        всего (объекты ссылаются друг на друга?) """
    new_turtle = turtle.Turtle()
    new_turtle.hideturtle()
    new_turtle.speed(0)
    new_turtle.up()
    return new_turtle


def casino(money):
    """ рандомно определяем выиграш """
    new_list = [0, int(money/2), money, int(money*1.5), int(money*2)]
    winning = choice(new_list)
    return winning


def casino_t_create():
    new_t = turtle.Turtle()
    new_t.hideturtle()
    new_t.up()
    new_t.speed(1)
    new_t.shape('circle')
    new_t.color('gold')
    new_t.width(10)
    new_t.goto(0, -60)
    new_t.down()
    return new_t


def tax_visualize():
    tax_turtle.color('#126626')
    tax_turtle.up()
    tax_turtle.goto(-20, -60)
    tax_turtle.write('$', align='center', font=("Arial", 25, "bold"))
    sleep(0.4)
    tax_turtle.goto(0, -60)
    tax_turtle.write('$', align='center', font=("Arial", 25, "bold"))
    sleep(0.4)
    tax_turtle.goto(20, -60)
    tax_turtle.write('$', align='center', font=("Arial", 25, "bold"))
    sleep(1)
    tax_turtle.clear()


def monopolization(t):
    """ Если у игрока куплена монополия (2 или 3 клетки подряд) и полностью улучшена текущая клетка"""
    colors = ['Red', 'Blue']

    t.speed(0)
    t.goto(t.xcor(), t.ycor()-20)
    t.color('#AF00E0')
    t.write('M', align='center', font=("Arial", 25, "bold"))

    t.goto(t.xcor(), t.ycor()+20)
    t.color(colors[my_index ^ 1])
    t.speed(10)


def end_game(p):
    info_turtle.clear()
    info_turtle.color('#BA02F2')
    info_turtle.write('{} победил!'.format(players[players.index(p) ^ 1].name), align='center',
                      font=("Arial", 15, "bold"))
    sleep(10)
    window.bye()


if __name__ == '__main__':
    import turtle
    from time import sleep
    from random import randint, choice

    # Создаем окно
    window = turtle.Screen()
    window.title('Монополия')
    window.colormode(255)
    window.bgcolor(245, 255, 245)

    # создаем черепашек
    teh_turtle = create_turtle()
    money_turtle_1 = create_turtle()
    money_turtle_2 = create_turtle()
    info_turtle = create_turtle()
    cell_info_turtle = create_turtle()
    casino_turtle = casino_t_create()
    tax_turtle = casino_t_create()

    info_turtle.goto(-0, -93)
    info_turtle.color('#0B2C0B')
    cell_info_turtle.goto(20, -70)
    info_turtle.write('Добро пожаловать! Нажмите <Space>, чтобы походить!', align='center', font=("Arial", 8, "normal"))

    teh_turtle.color('dark green')
    money_turtle_1.color('Red')
    money_turtle_2.color('Blue')

    money_turtles = [money_turtle_2, money_turtle_1]  # созд. список, чтобы с помощью my_index вызывать нужную черепашку

    # создание клеток
    cell_0 = Cell('Старт', 0, None, None)
    cell_1 = Cell('1-клетка', 1, 10, 1)
    cell_2 = Cell('2-клетка', 2, 20, 2)
    cell_3 = Cell('3-клетка', 3, 30, 3)
    cell_4 = Cell('4-клетка', 4, None, None)
    cell_5 = Cell('5-клетка', 5, 40, 4)
    cell_6 = Cell('6-клетка', 6, 50, 5)
    cell_7 = Cell('7-клетка', 7, None, None)
    cell_8 = Cell('8-клетка', 8, 60, 6)
    cell_9 = Cell('9-клетка', 9, 70, 7)
    cell_10 = Cell('10-клетка', 10, 80, 8)
    cell_11 = Cell('11-клетка', 11, None, None)
    cell_12 = Cell('12-клетка', 12, 90, 9)
    cell_13 = Cell('13-клетка', 13, 100, 10)
    field = [cell_0, cell_1, cell_2, cell_3, cell_4, cell_5, cell_6, cell_7, cell_8, cell_9, cell_10,
             cell_11, cell_12, cell_13]

    why()  # ваау. рисуем каждый раз новую карту при запуске программы ( не смог в скрин (пиксели неточные) )
    # window.bgpic('pic.png') - так должно быть в идеале. используем бекграунд пикчу как карту

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
    turtle_1.speed(1)
    turtle_2.speed(1)

    # пишем начальный кэш каждого игрока
    money_turtle_1.goto(50, 58)
    money_turtle_2.goto(50, 33)
    money_turtle_1.write('$ 100', font=("Arial", 15, "normal"))
    money_turtle_2.write('$ 100', font=("Arial", 15, "normal"))

    my_index = 0  # типа переключатель (см. функцию step)
    write_hod(teh_turtle, my_index)
    teh_turtle.showturtle()  # теперь видно кто ходит первый
    window.onkeypress(lambda: step(turtles[my_index], players[my_index]), 'space')
    window.listen()

    window.mainloop()
