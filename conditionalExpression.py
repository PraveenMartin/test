num1 = input("Enter number: ")
num2 = input("Enter number: ")
age = 10
temperature = 20
user_role = "guest"

max_num = num1 if num1 > num2 else num2
min_num = num1 if num1 < num2 else num2
print(f"Maximum Number:{max_num}","Minimum number {min_num}")

num = int(input("Enter the value: "))
print("Positive " if num >= 0 else "Negative ")
result = "Even" if num % 2 == 0 else "Odd"
print(result)

status="Adult" if age>=18 else"child"
print(status)

weather = "HOT" if temperature>20 else "COLD"
print(weather)

access_level="Full Access" if user_role == "admin" else "Limited Access "
print(access_level)

