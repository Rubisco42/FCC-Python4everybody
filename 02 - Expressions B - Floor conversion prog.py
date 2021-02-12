def prgm():
    ctry = input("In which country are you? ")
    if ctry == "USA":
        inp1 = input("Europe floor? ")
        usf = int(inp1) + 1
        print("US Floor", usf)
    else:
        print("good luck")
    if ctry == "Europe":
        inp2 = input("US Floor? ")
        euf = int(inp2) - 1
        if inp2 == "0":
            euf = "RDC"
        print("Europe floor", euf)
    else:
        print("good luck")


name = input("Who are you? ")
ext = input ("Do you want to determine floor equivalence? ")
while ext:
    if ext == "no":
        print("good bye")
        break
    if ext == "yes":
        prgm()
        tex = input ("Again? ")
        if tex != "yes":
            print("See you soon!", name)
            break








