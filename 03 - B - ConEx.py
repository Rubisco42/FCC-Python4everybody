#elif : multi way conditional

x = int(input("enter number "))# if user inputs is f up, crashes everything
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

#try/except structure alows to anticipate section of code that could lead to error (ex with user input
# if the try condition doesn t lead to error, except is skipped
#if try condition leads to errors, except section is run instead

rawster = input("Enter a number ")
try:
    ival = int(rawster)# this way anticipates user input induced errors
except:
    ival = -1#easy way to cope with wrong user inputs for this example. negative numbers are also convertible to int/floats

if ival > 0:
    print("Nice work")
else:
    print("Not a number")#
