#string methods
name = input("ENter your name: ")
result= name.rfind("q")
name= name.capitalize()
name= name.upper()
name =name.lower()
result = name.isdigit()
result = name.isalpha()

phone_number = input("enter your phone number: ")
result = phone_number.count("-")
phone_number = phone_number.replace("-", "")
print(phone_number)


#string indexing 
#indexing = accessing elements of a sequence using () (indexing operator)
#[start: end: step]

credit_number = "1234-5678-9012-3456"
last_digits= credit_number[-4:]
print(f"XXXX-XXXX-XXXX-{last_digits}")

print(credit_number[0])
print(credit_number[:4])
print(credit_number[5:9])
print(credit_number[5:])
print(credit_number[-1])
print(credit_number[::3])
