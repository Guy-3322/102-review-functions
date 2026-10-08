import math
def isPerfectSquare(float):
 try:
   if (float) <0:
     return False
   root = math.isqrt(float)
   return root * root == float



 except:
   return False


print(isPerfectSquare(25))
print(isPerfectSquare(4))
print(isPerfectSquare(-3))
print(isPerfectSquare(2.2))
print(isPerfectSquare("wdasjngsg"))