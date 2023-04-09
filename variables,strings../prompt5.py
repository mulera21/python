from sys import argv
script, user_name = argv
prompt = '>'

print(f"hi {user_name}, i'm the {script}.")
print("i'd would like to ask a few questions.")
print(f"do you like me {user_name}?")
like = input(prompt)

print(f"where do you live{user_name}?.")
live = input(prompt)

print("what kind of computer do you have")
computer = input(prompt)

print(f""" alright so you said {like} about likin me you live in {live}.
        oh that great ,and you have a {computer} computer, nice """)
