from sys import argv
script, user_name = argv

prompt = '>'

print(f"hi {user_name} this is your {script}")
print("i really love what you are doing")

print(f"were do you live {user_name}")
live = input(prompt)
print(f"do you love programming {user_name}")
love = input(prompt)
print("that's great")

print(f""" you said your name is {user_name} and you live {live} so love programing {love} oh that is great news """)
