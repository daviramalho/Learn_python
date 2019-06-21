#Exercise 9 -printing, printing, printing   #Use the comments here to print out
                                            #the markdown comments on the
                                            #Jupyter notebooks.
#------
#- Write down the code to apply more about the codes learnt;
#```python
#```code
#```
#------
#**SHAW, Z. \"Learn python 3 the hard way...\", 2017.

#Here's some new strange stuff, remember type it exactly.

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"
#With only the space the strings are printed into the same line.
print("Here are the days", days)
#Seems like the "\n" teels python to jump the string to the next line.
print("Here are the months", months)
#The more interesting here is that the the three double-quotes are used to
#write down any size of text inside of it. Seems like in this case the dot (".")
#should tell python to jump to the next line. You can check that by breaking the code.
#No. Try to understand why then the python jump the line...
print("""
There is something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
""")
