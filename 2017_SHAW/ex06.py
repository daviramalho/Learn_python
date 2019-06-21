types_of_people = 10
x = f"There are {types_of_people} types of people." #This is not a string.
#Previous one defines two variables with a numeric string, "types_of_people",
#inside another string, "x".The "f" before the string alows it to append the
#string inside the other.
binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."  #There are two strings
                                                        #inside an string [1, 2]
#Now the "x" & "y" are variables so it doesn't need to use quotation mark (" or ')
#to ask to print that.
print(x)
print(y)
#Remember here the reason why to use the "f" before the string. Without it
#it wouldn't be possible to append the "x" vairable. The curly brackets ({})
#allows that to specify where the before defined variable should be appent.
print(f"I said: {x}") #This is an string inside an string [3]
print(f"I also said '{y}'") #This is an string inside an string. [4]

hilarious = False #This is an boolean value.
joke_evaluation = "Isn't that joke so funny?! {}"   #This is not a string.
#Next line will add an sting inside a string, after that been write.
print(joke_evaluation.format(hilarious))
#Next will define two variables, "w" & "e".
w = "This is the left side of..."
e = "a string with right side."
#Than next one should append "w" & "e".
print(w + e)
