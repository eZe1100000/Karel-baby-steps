
from karel.stanfordkarel import *

def main():

    """
    Builds a zebra crossing pattern:
    - 2-wide beeper column
    - 3-wide gap
    Repeats until the end of the world
    """
    while front_is_clear():
        build_zebra_crossing_column()
        zebra_crossing_gap()

#Builds a 2-wide vertical column of beepers
def build_zebra_crossing_column():
    turn_left()
    put_beepers()
    put_beeper()
    turn_right()
    move()
    turn_right()
    put_beepers()
    put_beeper()
    turn_left()

#Fills a vertical line with beepers
def put_beepers(): 
    while front_is_clear():
        put_beeper()
        move() 

#Moves Karel across the gap between columns
def zebra_crossing_gap():
    if front_is_clear():
        for i in range(4):
            move()

#Karel turns right
def turn_right():
    for i in range(3):
        turn_left()


    
if __name__ == '__main__':
    main()
