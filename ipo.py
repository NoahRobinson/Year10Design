x = input("enter a number(example 7: ")
if(x.isdigit() == True):
    x = int(x)
    result = str(x* x)
    print("Your result is" + result)
else:
    print("You did not enter a number")
