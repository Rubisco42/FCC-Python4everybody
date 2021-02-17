#elif : multi way conditional

x = int(input("enter number "))
#be careful to convert the input (= string) to integer to use comparison operators

if x < 2:
    print("small")
elif 10 < x < 20 :
    print(" medium")
else:
    print("large")

#elif can be added infinitely

