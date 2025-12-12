print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("what is your age?" ))
    if age <= 12:
        bill = 5
        print(f"Child ticket is ${bill}.")
    elif age <= 18:
        bill = 7
        print(f"Youth ticket is ${bill}.")
    else:
        bill = 12
        print(f"Adult ticket is ${bill}.")
    wants_photo = input("Do you a rollercoaster photo taken? Type Y for Yes and N for No ")
    if wants_photo == "y":
        bill += 3
    print(f"Total ticket is ${bill}.")
else:
    print("Sorry you have to grow taller before you can ride.")
