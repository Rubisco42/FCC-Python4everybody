ctry = input("In which country are you")
if ctry == "USA":
    inp1 = input("Europe floor?")
    usf = int(inp1) + 1
    print("US Floor", usf)
if ctry == "Europe":
    inp2 = input("US Floor?")
    euf = int(inp2) - 1
    if inp2 == "0":
        euf = "RDC"
    print("Europe floor", euf)
else:
    print("good luck mofo")

