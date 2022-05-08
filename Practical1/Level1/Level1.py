def returnArea(a, b):
    return a*b

print("Give first dimension of the room (in meters): ")
a = float(input())
print("Give second dimension of the room (in meters): ")
b = float(input())

print("The area of the room is " + str(returnArea(a,b)) + "m^2")



