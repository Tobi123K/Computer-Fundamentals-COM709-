import math
#Ask user for radius of cylinder or cone
print("Please enter shape (cylinder or cone)")
shape = input()

print ("Enter a radius ")
radius = float(input())
#Ask user for height of cylinder

print ("Enter a height")
height = float(input())

# Decision yes or now answer is it a cylinder
if (shape == "cylinder"):
    volume = math.pi * (radius**2) * height
    print ("The volume of cylinder with",round(radius,2) , "and", round(height,2), "is", round(volume,2 ))
elif (shape == "cone"):
    volume = (math.pi * (radius**2) * height) /3
    print ("The volume of cylinder with",round(radius,2) , "and", round(height,2), "is", round(volume,2 ))
else:
   print("What the...?!")
