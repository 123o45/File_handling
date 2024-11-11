def fizzBuzz(n):
    for i in range(1, n + 1):
        if(i % 3 == 0)and (i % 5 == 0):
            print(f"{i} is a multiple of 3 and 5")
            print("FizzBuzz")
        elif(i % 3 == 0) and (i % 5!=0):
            print(f"{i} is a multiple of 3 but not 5")
            print("Fizz")
        elif (i % 5 == 0) and (i % 3!= 0):
            print(f"{i} is a multiple of 5 but not 3")
            print("Buzz")
        else:
            print(i)

fizzBuzz(15)