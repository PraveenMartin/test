# principle = 0
# rate = 0
# time=0 


# while True:
#     principle = float(input("Enter the principle amount: "))
#     if principle <= 0:
#         print("Principle can't be less than or equal to zero")
#     else:
#         break

# while True:
#     rate = float(input("Enter the interest rate: "))
#     if rate <= 0:
#         print("Interest rate can't be less than or equal to zero")
#     else:
#         break

# while True:
#     time = float(input("Enter the time: "))
#     if time <= 0:
#         print("time can't be less than or equal to zero")
#     else:
#         break


# total = principle *pow((1+rate/100),time)
# print(f"Balance after {time} year's: {total:.2f}")


# # for loop = execute a block of code a fixed number of times
# #            You can iterate over a range, string,sequence,etc.

# for i in reversed(range(1,11,2)):
#     print(i)
# print("Happy Learning")


# # countdown timer 
# import time

# my_time= int(input("Enter the time in seconds:"))
# for x in range(my_time,0,-1):
#     seconds = x % 60
#     minutes = int(x/60)% 60
#     hours = int(x/3600)% 24
#     print(f"{hours:02}:{minutes:02}:{seconds:02}")
#     #print(x)
#     time.sleep(1)
# print("Time's UP!")


#nested loops 
rows =int(input("Enter the rows: "))
col =int(input("Enter the columns: "))
symbol =int(input("Enter the symbol: "))

for x in range(rows):
    for y in range(col):
        print(y,end="")
    print()