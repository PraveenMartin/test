# #collection = single "variable" used to store multiple values
# # List = [] ordered and changeable. Duplicates OK
# # Set = {} unordered and immutable, but Add/Remove OK. NO duplicates
# # Tuple() ordered and unchangeable. Duplicates OK. FASTER
# #dictionary = a collection of {key:values} pairs ordered and changeable
# #                no duplicates
# # shipping list prj

# foods = []
# prices = []
# total = 0

# while True:
#     food = input("Enter the food to buy(q,Q to quit)")
#     if food.lower() == "q":
#         break
#     else:
#         price = float(input(f"enter the price of a{food}:$ "))
#         foods.append(food)
#         prices.append(price)

# print("Check your CART")

# for food in foods:
#     print(food,end='')

# for price in prices:
#     total += price

# price()
# print(f"Your total is: ${total}")

#dictionary
menu = {"pizza": 3.00,
    "nachos": 4.50,
    "popcorn": 6.00,
    "fries": 2.50,
    "chips": 1.00,
    "pretzel": 3.50,
    "soda": 3.00,
    "lemonade": 4.25}
cart =[]
total=0
print("     Menu    ")
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")
    print("       ")

while True:
    food=input("Select an item (q to Quit): ").lower()
    if food =="q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

for food in cart:
    total = total + menu.get(food)
    print(food,end=" ")
     
print()
print(f"Total is: ${total:.2f}")
