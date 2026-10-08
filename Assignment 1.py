#Create a function called **isNegative(float)** that takes a float parameter.  
#Return a boolean value to indicate whether the result is True or False


def isNegative(float):
    if float < 0:
        return True
    if float > 0:
        return False
    if float == 0:
        return False

print(isNegative(4))
print(isNegative(-4))
print(isNegative(0))
print(isNegative(-20101020323804718241092312))
print(isNegative(-10))
