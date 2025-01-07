# Exercise

weight = int(input("Weight: "))
unit = input("(K)g or (L)bc: ")
if unit.upper() == "K":
    converted = weight / 0.45
    print("Weight in Lbc: " + str(converted))
else:
    converted = weight * 0.45
    print("Weight in Kgs: " + str(converted))
