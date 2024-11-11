import datetime

filename = datetime.datetime.now()

with open(f"{filename}.txt", "w") as file:
    file.write("How are you doing......!")

# with open(filename.strftime("%Y-%m-%d-%H-%M")+".txt","w") as file:
#     file.write("This is a test")

    