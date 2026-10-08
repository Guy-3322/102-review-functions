def isPythagoreanTriple(a,b,c):
    try:
     if(a**2)+(b**2) == (c**2) or (b**2)+(c**2) == (a**2) or (a**2)+(c**2) == (b**2):
          return True
     else:
         return False
    except:
        pass


print(isPythagoreanTriple(3,4,5))
print(isPythagoreanTriple(5,3,4))
print(isPythagoreanTriple(4,5,3))
print(isPythagoreanTriple(3,5,4))
print(isPythagoreanTriple(4,3,5))
print(isPythagoreanTriple(5,4,3))
print(isPythagoreanTriple(10,2,5))