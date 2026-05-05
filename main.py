from karel.stanfordkarel import *


def main():
   
    build_efes()
    
#replace missing colums by beepers  
def build_efes():
    for i in range(3):
        build_column()
        move_to_ground()
        move_to_next_column()
    build_column()
    move_to_ground()

#build a column 5 units height
def build_column():
    turn_left()
    for i in range(4):
        put_beeper()
        move()
    put_beeper()


#after building a column moves to the ground
def move_to_ground():
    turn_right()
    turn_right()

    while front_is_clear():
        move()
    turn_left()


#after landing moves to next column
def move_to_next_column():
    for i in range(4):
        move()


#turns right
def turn_right():
    for i in range(3):
        turn_left()

if __name__ == '__main__':
    main()