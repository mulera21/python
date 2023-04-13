from sys import exit
def gold_room():
    print("this room is full of gold. how do you take it?")

    choice = input(" > ")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("man, lern to type a number")
    if how_much < 50:
        print("nice you'r not greedy you win")
        exit(0)
    else:
        dead("you gredy busterd!")

def bear_room():
    print("there is  bear here")
    print("the bear has a bunch of money")
    print("the fat bear s infront of another door")
    print("how are you going to move the bear")
    bear_moved = False

    while True:
        choice = input(" > ")
        if choice == "takinh money":
            dead("the bear look at you then slap your face off")
        elif choice == "taunt bear" and not bear_moved:
            print("the bear has moved from the door")
            print("you can go throught it now")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("this bear get pissed off and chew your leg")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print(" i got no idea what tht means")

def chilu_room():
    print("here is the great evil chilu")
    print("he is stare at you and you go insane")
    print("do you flee for your life or eaten")

    choice == input(" >")
    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("well tht was testy")
    else:
        chilu_room()

def dead(why):
    print(why, "Good job")
    exit(0)

def start():
    print("you are in dark room")
    print("there is a door to your right and left")
    print("which one do you take")

    choice = input(" > ")
    if choice == "left":
        bear_room()
    elif choice == "right":
        chilu_room()

    else:
        dead("you stumble in the room untill you dead")
start()

