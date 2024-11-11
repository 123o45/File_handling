import datetime

nam = input("enter your name: ")
now = datetime.datetime.now()
filename = now.strftime("%Y-%m-%d-%h-%M")
with open(f"files/{nam} _ {filename}.csv","w")as file:
    file.write("this not normal...........!")
    print(nam , filename)