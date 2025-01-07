# Exercise 1:
print("Check In")
print("Data=")
first_name = "John Smith"
age = 20
new_patient = True
print("Name:", first_name)
print("Age:", age, "Years Old")
print("New Patient?", "Yes")

# Exercise 2:
first = input("First: ")
second = input("Second: ")
sum = float(first) + float(second)
strsum = str(sum)
print("Sum: " + strsum)

# if statements:
temperature = 25
if temperature > 30:
    print("It's a Hot Day")
    print("Drink plenty of water")
elif temperature > 20:  # (20, 30]
    print("It's a Nice Day")
elif temperature > 10:  # (10, 20]
    print("It's a bit cold")
else:
    print("It's Cold")
print("Done")

# Exercise 3:
weight = input("Weight: ")
unit = input("(K)g or (L)bs: ")
if unit.upper() == "L":
    weightk = float(weight) / 2.205
    print("Weight in Kg: " + str(int(weightk)) + " kg")  # (lbs to kg]
elif unit.upper() == "K":
    weightl = float(weight) * 2.205
    print("Weigth in Lbs: " + str(int(weightl)) + " lbs")  # (kg to lbs]
