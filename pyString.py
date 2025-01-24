# Concat in String

'''Message = "Good Morning ,"
Name = "Phalgun"

concat = (Message+Name)

print(concat)'''

# String Slicing

'''1.  NAME = "Phalgun"
print(NAME[0])

2.  Name = "Phalgun"
print(Name[4:7])

3.  Name = "Phalgun"
print(Name[ :7]) # is same as Name [0:7]

print(Name[0: ]) # is same as Name[0:5]'''

# Negative Indices

''' Name = "Phalgun"
print(Name[-5:-2])'''

# Slicing with skip value
'''Name = "Phalgun"

print(len(Name)) #Lenth of String = 7

print(Name[:-3]) # 7-3 = 4 (It will (print) 4 Words (Phal)))

print(Name[-3:]) # 7-3 = 4 (It will (Remove) 4 Word (gun)))

# Example 

print(Name[-5:-2]) # In this Case (First Word(Ph)) Remove Because (7-5 = 2) It {Remove} (Ph) 
                   #              (Second Word(un)) Remove Because (7-2 = 5) It Print (Phalg) BUT (Ph is Remove From First side) and [alg] is {Print} and it Remove (un) From Second side '''
                   
                   
# String Methods in Python

# String are Immutable

''' Name = "Phalgun"

print(len(Name)) # This Method Help To Find Length of a String

print(Name.upper()) # This Method Help To Capital a String

print(Name.lower()) # This Method Help To Smaller a String

Name1 = "Phalgun!!!!!!!!!"
print(Name1.rstrip("!"))  # This Method Remove all The Sign Character From a String

Name2 = "Hi' Yatharth"
print(Name2.replace("Yatharth", "Phalgun")) # This Method Help To Replace in String 

Name3 = "Name-Phalgun Gender-Male Age-16"
print(Name3.split(" ")) # This Method Help To Convert String in Form of a List

Name4 = "phalGUN"
print(Name4.capitalize())# This Method Help To Convert First Character of a String to uppercase and Rest of Character of a String become lowercase

print(Name.center(50))# This Method Help To Move String at Center
print(Name2.center(50 ,","))

Name5 = "Phalgun is Phalgun"
print(Name5.count("Phalgun")) # This Method Help To Return the Number of Times The Given Value has Occured within the Given String

Name6 = "Phalgun is a Good Boy"
print(Name6.endswith("Boy")) # This Method Help to Find That Given String is Ending ending With in Given Value in String
print(Name3.endswith("16")) 

print(Name5.find("is")) # This Method Help to Find for a First Occurence of Given Value and Return The Index Where It Present

Name7 = "Phalgun is a Boy"
print(Name7.index("isu")) # This Method Help to Find for The First Occurrence of Given Value and Return The index Where it is present if given value is absent from the String Then Raise an Exception

Name8 = "Phalgun1099"
print(Name8.isalnum()) # This Method Help to Find True if entire String consists of A-Z,a-z,0-9 if any Punctuations or a Character is Present it Will Return False

print(Name.isalpha()) # This Method Help To Find True if Entire String Consists of A-Z,a-z

Name9 = "phalgun"
print(Name9.islower())# This Method Help To find True if all character in a String is Lower
print(Name.islower())

print(Name8.isprintable()) # This Method Help To Find out That a Value Given in a String is Printable or Not
Name10 = "Phalgun\n"
print(Name10.isprintable()) # False

Name11 = "               "
print(Name11.isspace())# This Method Help to Find String Contains White Space it #True

Name12 = "Phalgun Is A Boy"
print(Name12.istitle()) # This Method Help To Find That First Letter of Each Word of String is Capitalize #True
print(Name6.istitle()) # False

print(Name.startswith("P")) # This Method Help To Find That String Starts With Given Value #True

Name13 = "pHALGUN IS A pROGRAMMER"
print(Name13.swapcase()) #This Method Help in Converting the Character in (Uppercase to Lowercase) and (Lowercase to Uppercase)

Name14 = "phalgun is a programmer"
print(Name14.title()) #This Method Help To Capitalize Each Letter of the word Within a String '''

# Escape Sequence Character

''''Name = "Phalgun is Good"

# 1. \n For Adding New Line
print("Phalgun\nis a Good")

# 2. \t For Adding Tab Between Letter
print("Phalgun\tis Good")

# 3. \' For Adding Single Quotes Between Letter
print("Phalgun\'is Good")

# 4. \\ For Adding Single BackSlash Between Letter
print("Phalgun\\is Good")'''