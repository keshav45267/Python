# Create a program that asks for the user's favorite color and responds with a
# unique message for certain colors.
clr=input("enter color").lower()
if clr=="red":
    print("like the flames")
elif clr=="blue":
    print("like the sky")
elif clr=="green":
    print("like the grass")
elif clr=="yellow":
    print("like the sun")
else:
    print("this is your fav i guess")