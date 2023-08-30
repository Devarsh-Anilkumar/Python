w = int(input("Weight:"))
unit = input("(K)g or (L)bs:")
if unit.upper() == "K":
    nw = w * 2.2046226218
    print("Weight in pounds:" + str(nw))
if unit.upper() == "L":
    nw = w / 2.2046226218
    print("Weight in kilograms:" + str(nw))
