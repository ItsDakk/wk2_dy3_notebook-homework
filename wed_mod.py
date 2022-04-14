def square_footage():
    user_length = int(input("Please enter length: "))
    user_width = int(input("Please enter width: "))
    Area = user_length * user_width
    return Area
    
print("Your square-footage is "+ str(square_footage()) + "ft")

def circumference():
    user_radius= int(input("Please enter radius: "))
    circumference =  3.14159265359 * user_radius
    return circumference
    
print("The circumference is "+ str(circumference()))
