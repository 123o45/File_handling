import datetime


# files_generate = 4

# now = datetime.datetime.now()

# for f in range(2 ,files_generate + 1):
#     days_back = now -datetime.timedelta(days=f)
#     filename = days_back.strftime("%Y-%m-%d")
    # with open(f"{filename}.txt", "a") as file:
#       file.write("This is normal.... !")
      # print(filename)

nam = input("enter your name: ")
now = datetime.datetime.now()
filename = now.strftime("%Y-%m-%d-%h-%M")
with open(f"{nam} _ {filename} .txt","a")as file:
    file.write("this is just trials...........!")
    print(nam , filename)

