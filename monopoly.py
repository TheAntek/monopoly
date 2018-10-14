import turtle


def player_create(color):
    """ Создаем черепашек """
    player = turtle.Turtle()
    player.shape('turtle')
    player.color(color)
    player.speed(0)

    return player


def first_move(player, mistake, name):
    """ Занимаем иначальную позицию """
    player.up()
    player.goto(1, mistake)
    player.stamp()
    player.forward(20)
    player.right(90)
    player.forward(12)
    player.left(90)
    player.write(name, font=("Arial", 15, "normal"))
    player.goto(-175, 132+mistake)


def step(player):
    player.forward(65)


if __name__ == '__main__':

    window = turtle.Screen()
    window.bgpic('mon_map_v1.png')

    player_1 = player_create('red')
    player_2 = player_create('blue')

    first_move(player_1, 0, 'Anton')
    first_move(player_2, 20, 'Chris')

    window.onkeypress(lambda: step(player_1), 'g')
    window.listen()

    window.onkeypress(lambda: step(player_2), 'h')
    window.listen()


    window.exitonclick()
