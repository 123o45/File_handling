
def book(phone_number,full_name):

  if (len(phone_number) > 10 or len(phone_number) < 10 ):
    print("invalid number")
  elif (phone_number[:3] != "020" and phone_number[:3] != "050"):
    print("your number is not a valid vodaphone number") 
  else:
    with open("phone.txt" ,"a") as file:
        file.write(f'{full_name}: {phone_number}\n')
        print("number is added succesfully")


name = input("enter yuor name: ")

phone_number = (input("enter your phone number: "))


with open("phone.txt" ,"r") as file:
    book = file.read()
    if ((phone_number in book) or (name in book)):
        print("it already exit") 
    else:
       book("name,phone_number")          

