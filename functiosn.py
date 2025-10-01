def create_name(first,last):
    first = input("enter first name:")
    last = input("enter last name: ")
    return first +" "+ last

full_name = create_name("Prav", "Marvi")
print(full_name)

# default arguments A default value for certain parameters
# default is used when that argument is omitted
# make your functions more flexible, reduces # of arguments
# 1. positional, 2. DEFAULT, 3. keyword, 4. arbitrary

def net_price(list_price, discount=0, tax=0.05): # discount & tax -> default variables
    return list_price* (1 - discount) * (1 + tax)

print(net_price(500))
print(net_price(500,0.1)) # updating the default args - discount
print(net_price(500,0.1,0))# updating the default args - sales tax
