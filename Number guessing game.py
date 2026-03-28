print("-----Number guessing game-----")
num =56

while True:
    n=float(input("Enter the number:"))

    if num>n:
      print("your number is smaller then our's, please try again!!!")
    elif num<n:
        print("Your number is greater than our's, please try again!!")
    elif num==n:
        print("Good job!!! you did it!")
        break              
