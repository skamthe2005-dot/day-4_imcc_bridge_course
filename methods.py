text="welcome to imcc"
# to remove spaces form both ends
print(text.strip())

# to convert string to upper case
print(text.upper())

# to convert string to lower case
print(text.lower())

# to capitalize first letter
print(text.capitalize())

#count occurance of a substring
print("letter c occurs",text.count("c"),"times in text")

# find the position of substring (returns -1 if not found)
print("position of imcc in text is ",text.find("imcc"))

#replace substring
print(text.replace("imcc","IMCC"))

# check if string start or end with certain substring
print(text.startswith("wel"))
print(text.endswith("come"))



