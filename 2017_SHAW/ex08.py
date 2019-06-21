#Exercise 8 - Printing, Printing    #Use the comments here to write markdonw
                                    #comments into Jupyter Notebooks
#------
#- Here you'll learn how to print more complex string using ".format()"
#```python
#var="{} {} {} {}"
#print(var.format(x, y, z, w))
#```
#------
#**SHAW, Z., \"Learn Python 3 the hard way...\", 2017.

formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
#The strings, numbers or booleans should appear in the same order inside the
#previous defined variable.
print(formatter.format(True, False, False, True))
#Even the variable should show itself, if defined so.
print(formatter.format(formatter, formatter, formatter, formatter))
#The interesting here is the way the author uses the indentation (I think this
#is the name but I'm not sure). This is very useful and important.
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))
