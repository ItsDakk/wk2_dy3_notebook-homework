#Given a string after every y add an ! and after every s add a period and make every w and g capital
#Make a Function that takes a string as input and returns the adjusted string.
s="Hey welcome to doing whiteboard problems get prepared to figure our a problem on the fly"
#output= Hey! Welcome to doinG Whiteboard problems. Get prepared to fiGure our a problem on the fly!
def make_string(s):
    s1 = ""
    for letter in s:
        #after every y I need an !
        if letter.lower() == "y":
            s1 += "y!"
        #after every s I need a .
        elif letter.lower() == "s":
            s1 += "s."
        #Every g needs to be capitalized
        elif letter.lower() == "g":
            s1 += "G"
        #every w needs to be capitalized
        elif letter.lower() == "w":
            s1 += "W"
        else:
            s1 += letter
    return s1
print(make_string(s))









