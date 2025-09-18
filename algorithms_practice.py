# 1
print("==Steps for brushing ur teeth==")
print("step 1- grab ur toothbrush")
print("step 2- take toothpaste and place it on toothbrush")
print("step 3- wet toothbrush")
print("step 4- brush")
print("step 5- rinse")

# 2
fav_color = input("whats ur fav color? ")
print(f"Cool! I like {fav_color} too!")

# 3
user_number = int(input("enter a positive or negative number"))
if user_number:
    if user_number > 0:
        print("positive #")
    elif user_number == 0:
        print("zero")
    elif user_number < 0:
        print("negative #")
    else:
        print("error")
else:
    print("enter a #")

# 4
user_name = input("name: ")
for i in range(3):
    print(user_name)
    i + 1

# 5
entered_num = int(input("enter num: "))
if entered_num:
    if entered_num % 2 == 0:
        print("even num")
    elif entered_num % 2 == 1:
        print("odd num")
    else:
        print("error enter valid num")
else:
    print("u didn't enter anything")

# 6
input_num = int(input("enter num"))
for i in range(10):
    print(f"{input_num} x {i+1} = {(i+1)*input_num}")

# 7
age = int(input("enter age: "))
if age:
    if 0 <= age < 13:
        print("child ticket, $8")
    elif 13 <= age <= 59:
        print("adult ticket, $12")
    elif age >= 60:
        print("senior ticket, $6")
    else:
        print("attention: negatives dont work. enter proper age")
else:
    print("!enter age!")
