print("Please enter one of the following")
print("Please press w to go upward")
print("Please press s to go backward")
print("Please press a to go left")
print("Please press d to go right")

direction = input()

if (direction == "w"):
    print("Your are going up")
elif (direction =="s"):
    print("Your are going down")
elif (direction =="a"):
    print("Your are going left")
elif (direction =="d"):
    print("Your are going right")
else:
    print("error!!!")
