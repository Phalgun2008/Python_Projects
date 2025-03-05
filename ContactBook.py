# Contact Store
Contacts = {}

while True:

# Features
 print("1.Create Contact")
 print("2.Search Contact")
 print("3.Edit Contact")
 print("4.Delete Contact")
 print("5.Total Contact")
 print("6.View Contact")
 print("7.Exit")
 
# Choice 
 Choice=input("Enter your Choice ")
 
#1. Create Contact
 if Choice == '1':
      Name=input("Enter Name ")
      if Name in Contacts:
           print(f"Name {Name} already exist ",exit())
           
      else:
          Number=(input("Enter Number "))
          Contacts[Name]={Number}
          print(f"Name {Name} has created")
          #print(list(Contacts.items()))

#2. Search Contact
 elif Choice == '2':
    Name=input("Enter your Name to View ")
    if Name in Contacts:
      Contact=Contacts[Name]
      print(f"Name {Name}, Number:{Number}")
      
    else:
         print("Contact Not Found")
         
#3. Edit Contact
 elif Choice == '3':
      Name=input("Enter your Contact ")
      if Name in Contacts:
           Contact=Contacts[Name]
           print(f"Name {Name}, Number:{Number}")
           Name=input("Enter Name for update ")
           Number=input("Enter your Number for update ")
           Contacts[Name]={'Number ':Number}
           print(f"Name:{Name}, Number:{Number} has updated ")
      else:
           print("Not Found")
           
#4. Delete Contact     
 elif Choice == '4':
      Name=input("Enter Name to Delete ")
      if Name in Contacts:
           del Contacts[Name]
           print(f"Name {Name}, has Deleted ")
           
      else:
           print("Contact not found")
                     
#5. Total Contact
 elif Choice == '5':
      print("Total Contact = ",len(Contacts))
      
#6. View Contact
 elif Choice == '6':
      Contacts.keys()
      print(list(Contacts))

#7. Exit Program
 elif Choice == '7':
      print("Program Closed")
      
      break

 else:
      print('Invalid')
      break
