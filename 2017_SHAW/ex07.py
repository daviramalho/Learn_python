print("Mary had a little lamb.")
#The ".format('snow')" command should add a string named "snow" inside the
#curly brackets inside the phrase.
print("Its fleece was white as {}.".format('snow')) #I just didn't understand
                                                    #how does it know to do that
                                                    #because there is any
                                                    #indication os variables
                                                    #inside that brackets

#If you print next code line instead of last one, will will receive an error
#reporting some tupla problem
#print("Its fleece was {} {} {} white as {}.".format('snow'))

#Maybe next strategy solve this tupla problem:
print("Its fleece was {} {} {} white as {}.".format('sweet','soft','and','snow'))
#So the string after ".format('')" should have the same quantity of data than
#The curly bracket inside the print string.

print("And everywhere that Mary went.")
print("."*10)   #What'd that do? Repeat "." ten times.

end1="C"
end2="h"
end3="e"
end4="e"
end5="s"
end6="e"
end7="B"
end8="u"
end9="r"
end10="g"
end11="e"
end12="r"

#Watch that comma at the end. Try removing it to see what happens.
print(end1 + end2 + end3 + end4 + end5 + end6,end=' ')  #I don't know what that
                                                        #",end=''"means. seems
                                                        #it's made to append
                                                        #multiple functions.
print(end7 + end8 + end9 + end10 + end11 + end12)
