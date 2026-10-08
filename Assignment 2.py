#Create a function called "**isHappy(float)**.  
#This will return a boolean value that meets the following criteria:
#* it is a number
#* is an integer
#* it is positive


def isHappy(x):

 try:
  float(x)
  if x>-1:
         if isinstance(x, int):
          return True
         else:
           return False
         
  else:
    return False
 except:
  return False
        



print(isHappy(4))
print(isHappy(4.9))
print(isHappy(-4))
print(isHappy("four"))
print(isHappy(5))