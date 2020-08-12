def add(n1, n2):
    print(n1+n2)

add(10,20)

number1 = 10
number2 = input("Enter a number: ")   #if we call add() and give input it will give error as input is always a string

# print(add(number1, number2))

try:
    #Want to try this code, may have error
    result = 10+10
except:
    print("Hey it looks like you arent adding correctly")
else:
    print("Add went well!!")
    print(result)
finally:
    print("I always run!!")


##
def ask_for_int():
    while True:
        try:
            result = int(input("Please provide number "))
        except:
            print("Whoops! That is not a number")
            continue
        else:
            print("Yes thank you !!")
            break
        finally:
            print("End of try/except/finally")
            print("I always run at the end!!!")

ask_for_int()


#3 Homework
#1
for i in ['a','b','c']:
    try:
        print(i**2)
    except:
        print("Please try to enter numbers")
        break

#2
x = 5
y = 0
try:
    z = x/y
except:
    print("Divide by 0 error")
finally:
    print("All Done")


#3
def ask():
    while True:
        try:
            integer = int(input("Please enter an integer "))
        except:
            print("You didnt input an integer!! Please try again!")
            continue
        else:
            print(f"Thank you, your number squared is {integer**2}")
            break

ask()
