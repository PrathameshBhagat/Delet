
#1.capitalize()
txt = "ram is good boy."
x = txt.capitalize()
print (x)

#2.casefold()
txt = "Ram is Good boy than any other boy."
x = txt.casefold()
print (x)

#3.center()
txt = "Ram is Good boy than any other boy."
x = txt.center(60)
print (x)

#4.count()
txt = "Ram is Good boy than any other boy."
x = txt.count("boy")
print ("No of times boy present is : " ,x)

#5.encode()
txt = "Råm is Good boy than åny other boy."
x = txt.encode()
print ("Encoded version is : " ,x)

#6.endswith()
txt = "Ram is Good boy than any other boy."
x = txt.endswith(".")
print ("String Ends with : " ,x)

#7.expandtabs()
txt = "Ram \t is \t Good \t boy \t than \t any \t other \t boy."
x = txt.expandtabs(8)
print ("Tab size by 8 : " ,x)

#8.find()
txt = "Ram is Good boy than any other boy."
x = txt.find("boy")
print ("Find the boy in string : " ,x)

#9.format()
txt = "Ram is {boy: .2f} % Good boy than any other boy."
x = txt.format(boy = 100)
print ("No of times boy present is : " ,x)

#10.index()
txt = "Ram is Good boy than any other boy."
x = txt.index("boy")
print ("Index of  boy in string : " ,x)

#11.isalnum()
txt = "Ram"
x = txt.isalnum()
print ("Charecter in string is Alphanumeric : " ,x)

#12.isalpha()
txt = "Ram"
x = txt.isalpha()
print ("Charecter in string is Alphabet : " ,x)

#13.isascii()
txt = "Ram is Good boy than any other boy."
x = txt.isascii()
print ("Charecter in string is Ascii : " ,x)

#14.isdecimal()
txt = "Ram is Good boy than any other boy."
x = txt.isdecimal()
print ("Charecter in string is Decimal : " ,x)

#15.isdigit()
txt = "Ram is Good boy than any other boy."
x = txt.isdigit()
print ("Charecter in string is Digit : " ,x)

#16.isidentifier()
txt = "Ram is Good boy than any other boy."
x = txt.isidentifier()
print ("Charecter in string is Indentifier : " ,x)

#17.islower()
txt = "Ram is Good boy than any other boy."
x = txt.islower()
print ("Charecter in string is Loower Case : " ,x)

#18.isprintable()
txt = "Ram is Good boy than any other boy."
x = txt.isprintable()
print ("Charecter in string is Printable : " ,x)

#19.isspace()
txt = "Ram is Good boy than any other boy."
x = txt.isspace()
print ("Charecter in string is Whitespaces : " ,x)

#20.istitle()
txt = "Ram is Good boy than any other boy."
x = txt.istitle()
print ("Charecter in string is Follow Rule Title : " ,x)

#21.isupper()
txt = "Ram is Good boy than any other boy."
x = txt.isupper()
print ("Charecter in string is Upper Case: " ,x)

#22.join()
txt = ("Ram is Good " , " boy than " , " any other boy.")
x = "$".join(txt)
print ("Charecter in string is join Tuple : " ,x)

#23.ljust()
txt = "Ram is Good boy than any other boy."
x = txt.ljust(50)
print (x, " -:Charecter in string is Justified " )

#24.lower()
txt = "Ram is Good boy than any other boy."
x = txt.lower()
print ("Convert in Lowercase : " ,x)

#25.lstrip()
txt = "      Ram is Good boy than any other boy.       "
x = txt.lstrip()
print ("Convert in Trim Version : " ,x , " is")

#26.maketrans()
txt = "Ram is Good boy than any other boy."
x = txt.maketrans("b","d")
print ("Convert to Translate Table : " ,txt.translate(x))

#27.partition()
txt = "Ram is Good boy than any other boy."
x = txt.partition("boy")
print ("Convert in Parts : " ,x)
