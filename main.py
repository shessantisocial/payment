# print("What is your first name?")
# fname = str(input())

# print("What is your last name?")
# lname = str(input())

# print("Input your phone number:")
# contact = int(input())

# name = str(input())
# print(f"Hello, {fname} {lname} your account has been created.")

# name = str(input("What is your name")).lower
# print(name)

# a = 2 + 2 == 4
# print(a)

# name = str(input("what is your name")).lower()
# gender = str(input("what is you sex")).lower()
# if gender = "male":
# print("you are a guy")
# elif gender == "female":
# print("you are a lady")
# else:
# print("invalid gender")

print("welcome\nwhat was the cost of your purchase")
response = float(input())
tip = 0.01 * response
total_purchase = tip + response
print(total_purchase)

print("what type of payment is this\na. Joint\nb. Single")
reply = str(input(">> ")).lower()
if reply == "a":
    no_p = int(input("how many of you are paying\n>> "))
    each_tip = total_purchase / no_p
    print(each_tip)
elif reply == 'b':
    print(total_purchase)
else:
    print('invalid payment')        






