from sys import argv

script, filename = argv

print(f"we are going to erase {filename}.")
print("if you don't want that hit CRTL-C(^C).")
print("if you do want that hit RETURN.")
input("?")

print("open the file")
target = open(filename, 'w')
print("trunacte the file.Goodbye!")
target.truncate()

print("now i'm goin to ask you for three lines")

line1 = input("line 1:")
line2 = input("line 2:")
line3 = input("line 3:")

print("am going to write to this files")
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it")
target.close()
