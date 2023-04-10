# this is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args

    print(f" {arg1}, arg2: {arg2}")

    #ok that *args is pointless we can do this
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

    #this one take one argument
def print_one(arg1):
    print(f"arg1: arg1")
    
    #this one take no argument
def print_no():
    print("no argument")

print_two("hello", "edmond")
print_two_again("i", "programing")
print("nice")
print_no()

