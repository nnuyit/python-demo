print("Welcome to calculator\n")
total = float(input("What total you pay? $"))
tip = int(input("What percentage tip you want to give? 10, 12, 15: "))
people = int(input("How many people you want to split? "))
billWithTip = (tip / 100 + 1) * total
billPerPerson = billWithTip / people
print(f"Each person should pay {round(billPerPerson, 2)}")
