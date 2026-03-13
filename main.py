print("Welcome to Python Pizza Deliveries!")

small_pizza = 15
medium_pizza = 20
large_pizza = 25
pepperoni_on_small_p = 2
pepperoni_on_m_p = 3
cheese = 1

bill = 0

size = input(f"What size pizza do you want? S ${small_pizza}, M ${medium_pizza} or L ${large_pizza}: \n").lower()
pepperoni = input(f"Do you want pepperoni on your pizza? Y or N (S - ${pepperoni_on_small_p}, M & L - ${pepperoni_on_m_p})\n").lower()
extra_cheese = input(f"Do you want extra cheese? Y or N: ${cheese} for all the pizza sizes \n").lower()

if pepperoni not in ["y", "n"]:
    print("invalid Entry, please try again.")

if extra_cheese not in ["y", "n"]:
    print("invalid Entry, please try again.")

if size == "s":
    bill += small_pizza
    if pepperoni == "y":
        bill += pepperoni_on_small_p
    if extra_cheese == "y":
        bill += cheese

if size == "m":
    bill += medium_pizza
    if pepperoni == "y":
        bill += pepperoni_on_m_p
    if extra_cheese == "y":
        bill += cheese

if size == "l":
    bill += large_pizza
    if pepperoni == "y":
        bill += pepperoni_on_m_p
    if extra_cheese == "y":
        bill += cheese

print(f"Your final bill is: ${bill}.")