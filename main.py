"""
Monopoly Game
version 0
10.10.18
"""


class Player:
    """ Игрок имеет начальную позицию=0, деньги=100 и передается имя"""
    def __init__(self, name):
        self.position = 0
        self.money = 100
        self.name = name

    def move(self):
        """ Один ход. Позиция игрока += рандомное число"""
        movement = random.randint(1, 5)
        self.position += movement
        print('Вы походили на {}'.format(movement))

        if self.position >= 20:  # таким образом начинаем круг сначала
            self.position -= 20  # позиции опять начинают считаться с нуль (20->0, 23->3)
            self.money += 100  # когда прошли круг - начисляются деньги

    def info(self):
        print('{}. Деньги - {}. Позиция {}.'.format(self.name, self.money, self.position))


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


class Field:
    def __init__(self):
        pass


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
cell_15 = Cell('15-клетка', 15, 80)
cell_16 = Cell('16-клетка', 16, 85)
cell_17 = Cell('17-клетка', 17, 90)
cell_18 = Cell('18-клетка', 18, 95)
cell_19 = Cell('19-клетка', 19, 100)


field = [cell_0, cell_1, cell_2, cell_3, cell_4, cell_5, cell_6, cell_7, cell_8, cell_9, cell_10,
         cell_11, cell_12, cell_13, cell_14, cell_15, cell_16, cell_17, cell_18, cell_19]


if __name__ == '__main__':
    import random
    player_1 = Player('Anton')

    player_1.info()

    while True:
        input('\nХодить!')
        player_1.move()
        player_1.info()

        field[player_1.position].info()

        choose = input('[1] Купить [2] Пас\n')
        if choose == '1':
            field[player_1.position].purchase(player_1.name)
            player_1.money -= field[player_1.position].price

        elif choose == '2':
            pass

        else:
            print('[1] Купить [2] Пас')

        player_1.info()
