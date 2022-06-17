weight = int(input("weight: "))
unit   = input("(K)gs or (L)bs: ")
if unit.upper == "L":
    con = weight * 0.45
    print(f"{con} kg")
else:
    con = weight / 0.45
    print(f"{con} lbs")
