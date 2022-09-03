from random import randint


# Keeping track of my Taxi poition using this class
class Pos:
    xpos = 0
    ypos = 0

    def __init__(self, x, y):
        Pos.xpos = Pos.xpos + x
        Pos.ypos = Pos.ypos + y


# This is my game board
game_path = ["| | | | | | | | | | |",
             "| | | | | | | | | | |",
             "| | | | | | | | | | |",
             "| | | | | | | | | | |",
             "| | | | | | | | | | |"]


# This function prints the board
def print_path():
    for i in game_path:
        print(i)


# This function takes the col, row and pointer as the argument and adds the pointer in that element
def add_value(num, cell, pointer):
    # print(num, cell)
    temp_string = ""
    for character in game_path[cell]:
        temp_string += character
    index = (num * 2) + 1
    temp_string = temp_string[:index] + pointer + temp_string[index + 1:]
    game_path[cell] = temp_string


# This function is used to move the taxi until it reaches its target element
def moving_taxi(target_x, target_y):
    moving = True
    while moving:
        if Pos.xpos == target_x and Pos.ypos == target_y:
            add_value(Pos.xpos, Pos.ypos, " ")
            add_value(passenger_posx, passenger_posy, " ")
            break
        move = input("\nMake your move (WASD) or press any other key to quit. Position: " + str(Pos.xpos) + "," + str(
            Pos.ypos) + "\n")
        if move == "w":
            add_value(Pos.xpos, Pos.ypos, " ")
            Pos(0, -1)
            if Pos.ypos < 0:
                print("Invalid move!")
                Pos(0, 1)
                add_value(Pos.xpos, Pos.ypos, "T")
                print_path()
                continue
            else:
                add_value(Pos.xpos, Pos.ypos, "T")
                print_path()
        elif move == "a":
            add_value(Pos.xpos, Pos.ypos, " ")
            Pos(-1, 0)
            if Pos.xpos < 0:
                print("Invalid move!")
                Pos(1, 0)
                add_value(Pos.xpos, Pos.ypos, "T")
                print_path()
                continue
            else:
                add_value(Pos.xpos, Pos.ypos, "T")
                print_path()
        elif move == "s":
            add_value(Pos.xpos, Pos.ypos, " ")
            Pos(0, 1)
            if Pos.ypos > 4:
                print("Invalid move!")
                Pos(0, -1)
                add_value(Pos.xpos, Pos.ypos, "T")
                print_path()
                continue
            else:
                add_value(Pos.xpos, Pos.ypos, "T")
                print_path()
        elif move == "d":
            add_value(Pos.xpos, Pos.ypos, " ")
            Pos(1, 0)
            if Pos.xpos > 9:
                print("Invalid move!")
                Pos(-1, 0)
                add_value(Pos.xpos, Pos.ypos, "T")
                print_path()
                continue
            else:
                add_value(Pos.xpos, Pos.ypos, "T")
                print_path()
        else:
            exit()
            # add_value(Pos.xpos, Pos.ypos, " ")
            # add_value(passenger_posx, passenger_posy, " ")
            # moving = False


print("WELCOME TO THE TAXI GAME!!")
game = True

while game:
    main_menu = input("Press P to play, I for instructions and press anything else to exit the game! ")
    if main_menu == "p":

        print("```````````````````````````````````````````````````````````````````````````````````````````````````````")
        print("Passanger is waiting. Pick up the passanger!")
        print("```````````````````````````````````````````````````````````````````````````````````````````````````````")
        passenger_posx, passenger_posy = randint(0, 9), randint(0, 4)

        # Passanger pointer P is added to the board using the passanger position
        add_value(passenger_posx, passenger_posy, "P")

        # Taxi position is saved to Pos class. It can be modifed by using Pos(x,y). For example, Pos(0, 1) would
        # move the taxi one unit down
        Pos.xpos = 0
        Pos.ypos = 0

        # Sets Taxi at (0,0)
        add_value(0, 0, "T")
        print_path()

        # Moves taxi until it reaches passanger location
        moving_taxi(passenger_posx, passenger_posy)

        print("```````````````````````````````````````````````````````````````````````````````````````````````````````")
        print("\nYou picked up the passanger. Now drop the passanger off to their home!\n")
        print("```````````````````````````````````````````````````````````````````````````````````````````````````````")

        home_posx, home_posy = randint(0, 9), randint(0, 4)

        # Adds home pointer onto the board
        add_value(home_posx, home_posy, "H")
        add_value(Pos.xpos, Pos.ypos, "T")
        print_path()

        # Moves taxi until it reaches homes location
        moving_taxi(home_posx, home_posy)

        print("```````````````````````````````````````````````````````````````````````````````````````````````````````")
        print("You dropped off the passanger safely! Thanks for playing the Taxi Game")
        print("```````````````````````````````````````````````````````````````````````````````````````````````````````")

    elif main_menu == "i":
        print("```````````````````````````````````````````````````````````````````````````````````````````````````````")
        print("\nIn this game you will be driving a taxi. Your goal is to pick up you passangers and drop them off \n"
              "at their drop off locations. You can move around using the W A S D keys. You also have to stay in   \n"
              "bounds so be cautious of ur bondary!")
        print("```````````````````````````````````````````````````````````````````````````````````````````````````````")

    else:
        game = False
