#-------------------------FUNCTIONS----------------------------
def name_function():
    #help for function
    '''
    DOCSTRING: Information about the function
    INPUT: no input....
    OUTPUT: HELLO...... 
    '''
    print("HELLO")

help(name_function)

def say_hello(name = "NAME"):   #default string for parameter
    return 'Hello' +name
result = say_hello(" Pronnoy")
print(result)

def add (n1, n2):
    return n1+n2
result = add(10,20)
print(result)

#Find if word dog is in a string
def dog_check(mystring):
    return 'dog' in mystring.lower()
      
result = dog_check('My Dog ran away')
print(result)

#PIG LATIN
def pig_latin(word):
    first_letter = word[0]
    #check if vowel
    if first_letter in 'aeiou':
        pig_word = word + 'ay'
    else:
        pig_word = word[1:]+ first_letter+ 'ay'
    return pig_word

print(pig_latin('word'))

#*args and **kwargs
def myfunc(a,b):
    return sum((a,b)) * 0.05
print(myfunc(40,60))

#args to add in arbitrary number of arguments to a parameter list as a tuple 
def myfunc(*args):
    print(sum(args))
myfunc(2,3,4,51,2,4,5,1)

#**kwargs creates a dictionary of the arguments list#takes key value pairs
def myfunc(**kwargs):
    print(kwargs)
    if 'fruit' in kwargs:
        print('My fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print("I did not find any fruit here")
myfunc(fruit = 'apple', veggie ='lettuce')

def myfunc(*args, **kwargs):
    print(args)
    print(kwargs)
    print('I would like {} {}'.format(args[0], kwargs['food']))
print(myfunc(10,20,30, fruit='orange', food='eggs', animal = 'dog'))

#------------------PRACTICE PROBLEMS------------------------------
#level 0 
#1 
def lesser_of_two_evens(a,b):
    if a%2==0 and b%2==0:
        return min(a,b)
    else:
        return max(a,b)
print(lesser_of_two_evens(2,4))
print(lesser_of_two_evens(3,9))

#2
def animal_crackers(text):
    list = text.split()
    return list[0][0] == list[1][0]
print(animal_crackers('Levelheaded Llama'))
print(animal_crackers('Levelheaded Deer'))

#3
def makes_twenty(n1,n2):
    return (n1+n2)==20 or n1==20 or n2 ==20
print(makes_twenty(20,10))
print(makes_twenty(30,10))
print(makes_twenty(1,1))

#Level 1
#1
def old_macdonald(name):
    first_letters= name[:3]
    last_letters = name[3:]
    print(first_letters.capitalize() +last_letters.capitalize())
old_macdonald('macdonald')

#2
def master_yoda(text):
    l1 = text.split()
    print(' '.join(l1[::-1]) )
master_yoda('I am home')
master_yoda('We are ready')

#3
def almost_there(n):
    if abs(100-n)<=10 or abs(200-n)<=10:
        return True
    else:
        return False
print(almost_there(104))
print(almost_there(150))

#Level2
#1
def has_33(nums):
    for i in range(0,len(nums)-1):
        if nums[i]==3 and nums[i+1]==3:
            return True
    return False
print(has_33([3,3,4,4]))

#2
def paper_doll(text):
    result = ''
    for i in text:
        result+= i*3
    return result
    
print(paper_doll('HI'))
print(paper_doll('HELLO'))

#3
def blackjack(a,b,c):
    sum = a+b+c
    if sum<=21:
        return sum
    elif sum>21 and (a == 11 or b==11 or c==11):
        sum-= 10
        return sum
    elif sum>21:
        return "BUST"
    elif a>11 or b>11 or c>11:
        print("Enter valid numbers")
print(blackjack(9,9,9))

def spy_game(nums):

    code = [0,0,7,'x']
    
    for num in nums:
        if num == code[0]:
            code.pop(0)   # code.remove(num) also works
       
    return len(code) == 1
spy_game([1,2,4,0,0,7,5])    

##-------------------------Lambda Functions-------------------------------
#1. MAP
def square(num):
    return num**2

my_nums = [1,2,3,4,5]
for item in map(square,my_nums):
    print(item)

#2. Filter
def check_even(num):
    return num%2 ==0
my_nums = [1,2,3,4,5,6]
print(list(filter(check_even, my_nums)))

#3. Lambda Expressions
#also known as anonymous function -  no name
print(list(map(lambda num:num**2,my_nums)))

##-------------------NESTED STATEMENTS AND SCOPE-------------------
#lOCAL
#ENCLOSED LOCAL
#GLOBAL
#BUILT IN

#Global
name= 'I am a global string'

def greet():

    #enclosing local
    name = 'SAMMY'
    def hello():
        #LOCAL
        name = 'I\'m a local'
        print('HELLO '+name)
    hello()
greet()

## GLobal variable
x = 50
def func():
    global x
    print(f'x is {x}')

    #local reassignment on a global variable
    x = 'New Value'
    print(f'I just locally changed Global X to {x}')
func()
print(x)

##--------------------ASSIGNMENT-------------------------------
#1 Volume
def vol(rad):
    print((4/3)* 3.14* rad**3)
vol(2)

#2
def ran_check(num,low,high):
    if num in range(low, high+1):
        return True 
    else:
        return False
print(ran_check(9,2,7))

#3
def up_low(s):
    count_upp = 0
    count_low = 0
    s1 = s.split()
    print(s1)
    for i in s:
        if i.islower():
            count_low+=1
        elif i.isupper():
            count_upp+=1
    print(f'Number of lower case letters are {count_low}')
    print(f'Number of upper case letters are {count_upp}')
up_low('Hi my name is Pronnoy Dutta')

#4
def unique_list(lst):
    print(list(set(lst)))
unique_list([1,1,1,1,2,2,3,3,3,3,4,5])

#5
def multiply(numbers):  
    mul = 1
    for i in numbers:
        mul *= i
        print(mul)
multiply([1,2,3,5])

#6
def palindrome(s):
    for i in s:
        return s[0:] == s[::-1]
print(palindrome('malayalam'))

