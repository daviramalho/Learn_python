name = 'Zed A. Shaw'
age = 35 # Not a lie
height = 74 # inches
height_cm = height*2.54 #Centimenters. This is my first ever Function.
weight = 180 #lbs
weight_kg = weight*0.453592 #Kilograms. This is my second ever Function.
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"In centimenters that means {height_cm}cm.") #This is my first time
                                                    #appending an function
                                                    #into a string.
print(f"He's {weight} pounds heavy.")
print(f"In kilograms that means {weight_kg}Kg.")

print(f"Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

#This line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")
