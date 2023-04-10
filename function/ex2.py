def cheese_and_cracker(cheese_count, boxes_of_crackers):
    print(f"you have {cheese_count} cheeses!:")
    print(f"you have {boxes_of_crackers} boxes of crackers!")
    print("man that's enough for a party!")
    print("get a blanket.\n")

    print("we can just give the function numbers directly")
    cheese_and_cracker(20, 30)

    print("we can use vrible from our script")
    amount_of_cheese = 10
    amount_of_cracker = 50

    cheese_and_cracker(amount_of_cheese, amount_of_cracker)

    print("we can even do math inside too")
    chees_and_cracker(10 + 20, 5 + 5)

    print("and we can combine the two vriable and math")
    cheese_and_cracker(amount_of_cheese + 100, amount_of_cracker + 200)
