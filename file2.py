

def phone_book(phone_number, name):

    
  if (len(phone_number) > 10 or len(phone_number) < 10):

    print("Invalid number") 
  elif(phone_number[:3] != '024' and phone_number[:3] != '054' and phone_number[:3] != '055'):
    print("your number is not an MTN number")

  else:
    with open("phoneBook.txt","a") as number:
        number.write(f"{name}: {phone_number} \n")
    print("Number added successfully!")

nan = input("enter your full name: ")    
phone_number = input("entre your mobile number: ")

with open("phoneBook.txt","r") as file:
   content = file.read()
   if((phone_number in content) or (nan in content)):
      print("It already exists")
   else:
      phone_book(phone_number,nan)
      

#phone_book(phone_number,nan)

   
