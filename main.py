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


field = [cell_0, cell_1, cell_2, cell_3, cell_4, cell_5, cell_6, cell_7, cell_8, cell_9, cell_10,
         cell_11, cell_12, cell_13, cell_14]


if __name__ == '__main__':
    import random
    player_1 = Player('Anton')
    player_2 = Player('Donald')

    players = [player_1, player_2]

    player_1.info()
    player_2.info()

    while True:
        for i in range(len(players)):
            input('\n{}, ходи!'.format(players[i].name))
            players[i].move()
            players[i].info()  # инфа про игрока

            field[players[i].position].info()  # вся инфа про клетку, куда наступил игрок

            if field[players[i].position].owner is None:
                """ Если клетка еще не куплена """
                while True:
                    choose = input('[1] Купить [2] Пас\n')
                    if choose == '1':
                        field[players[i].position].purchase(players[i].name)
                        players[i].money -= field[players[i].position].price
                        break
                    elif choose == '2':
                        break
                    else:
                        continue

            elif field[players[i].position].owner == players[i].name:
                """ Если клетка уже куплена вами """
                print('Это ваша клетка')
                while True:
                    choose = input('[1] Улучшить [2] Пас\n')
                    # Тут будет функционал улучшение клетки. По типу постройки домов в оригинальной монополии
                    # Но улучшать можно только когда вы на своей клетке
                    if choose == '1':
                        print('Улучшение пока недоступно!')
                        break
                    elif choose == '2':
                        break
                    else:
                        continue

            else:
                """ Если клетка куплена кем-то другим """
                rent = int(field[players[i].position].price*0.1)  # арендая плата = 10% цены клетки
                print('Вы заплатили {}'.format(rent))
                players[i].money -= rent  # забираем у того, кто наступил на чужую клетку арендную плату

                for p in players:  # ищим владельца клетки по имени (В игре должны быть разные имена!!!)
                    if p.name == field[players[i].position].owner:  # нашли владельца - отдаем ему бабки
                        p.money += rent

            players[i].info()
