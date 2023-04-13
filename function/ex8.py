from sys import exit
def river_room():
    print("there are alot of snakes")
    print("they are coming for you they is water flowing downstream")
    print("what will you do? jump to the water or stand")

    choice = input(">")
    if choice == "jump":
        print("you are safe")
        exit(0)
    elif choice == "stand":
        print("you are eten burstard")
        exit(0)

def man_house():
    print("you are safe")
    exit(0)

def lion_room():
    print("there the lion stare at you")
    print("what will you do")
    print("run! or eat your head")

    choice = input(">")

    if choice == "run":
        man_house()
    elif choice == "head":
        print("you will be testy")
        exit(0)

def start():
    print(" you are in the middle of the forest two road are in front")
    print("one on the left the other on the right")
    print("which one will you take?")

    choice = input(">")

    if choice == "left":
        lion_room()
    elif choice == "right":
        river_room()
    else:
        dead("you are eaten in the wilderness")
start()
