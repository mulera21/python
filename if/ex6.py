ten_things = "apple orange crows light sugar salt"

print("wait there are no 10 things in that list lets fix it")

stuff = ten_things.split(" ")
more_stuff = ["day", "night", "song", "girl"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("adding", next_one)
    stuff.append(next_one)
    print(f"there are {len(stuff)} items now.")

    print("there we go", stuff)
    print(f"lets do some things with stuff")

    print(stuff[1])
    print(stuff[-1])
    print(stuff.pop())

