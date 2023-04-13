from sys import exit
def punish_room():
    print("..................................")
    print("eithere you pass exams or caught")
    print("pass or caught")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

    choice = input(">")

    if choice == "pass":
        print("bustered you copy exams")
        exit(0)
    elif choice == "caught":
        print("bustered you going home")
        exit(0)

def start():
    print("<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    print("you are in the exams room and you don't understand")
    print("you have mwakenya in the pocket and the lecture is there")
    print("remove mwakenya or stare")
    print("............................................")

    choice = input(">")

    if choice == "remove":
        punish_room()
    elif choice == "stare":
        print("you failed exam busterd")
        exit(0)
start()
