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
#do not overlap condition like:
# if x < 2:
#elif x <20
#elif x < 10  : 6 is below 10 and below 20. second elif will never run
#be careful to the order of of conditional statement

