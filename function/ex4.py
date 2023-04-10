print("lets practise everything")
print('you \'d need to know \'bout escape with \\ that do:')
print('\n newline and \t tabs')


poem = """
\tthe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuituion
and requires an explanation \n\twhere there none
"""
print(".....................")
print(poem)
print(".........................")

five = 10 - 2 + 3 - 6
print(f"this shoul be five:{five}")

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 1000
beans, jars, crates = secret_formula(start_point)
print(f"with a starting point of {start_point}")
print(f"we'd have{beans} beans, {jars} jars, and {crates} crates")
start_point = start_point / 10
print("we can also do this way")
formula = secret_formula(start_point)
#this is a easy way to apply a list to a format string
print("we'd have {} beans, {} jars, and {} crates".format(*formula))
