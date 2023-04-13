i = 0

number = []

while i < 6:
     print(f"at the top of i is {i}")
     number.append(i)

     i = i + 1
     print("number now is ", number)
     print(f"all the bottom i is {i}")

     print("the number")
     for num in number:
         print(num)
