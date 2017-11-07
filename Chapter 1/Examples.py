#Exception
def division(x,y):
    try:
        z = x/y
        return z

    except ZeroDivisionError:
        print("Divider cannot be zero")




x = input("Input a dividable: \n")
y = input("Enter a divider: \n")

result = division(float(x),float(y))
print("result is: " + str(result))
