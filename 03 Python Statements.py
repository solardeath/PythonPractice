##--------------CONTROL FLOW---------------------------------
#1. -----------------IF/ELIF/ELSE
hungry = False

if hungry:
    print('FEED ME!!')
else:
    print('Im not hungry')    

loc = 'Bank'
if loc == 'Auto Shop':
    print('Cars are cool')
elif loc == "Bank":
    print('Money is cool')
elif loc == "Store":
    print('Welcome to the store')
else:
    print('I do not know much!')

#2.------------------------------ FOR LOOPS    
mylist = [1,2,3,4,5,6,7,8,9,10]
for i in mylist:
    print(i)

for num in mylist:
    #check for even
    if num%2 == 0:
        print(num) 
    else:
        print('Odd number: {}'.format(num))

#sum of list
list_sum =0
for num in mylist:
    list_sum+=num
print("The sum is {}".format(list_sum))

#string for loop
mystring = 'Hello World'
for letter in mystring:
    print(letter)

#list for loop
mylist =[(1,2),(3,4),(5,6),(7,8)]
print(len(mylist))
for i,j in mylist:
    print(i,j)

#for loop dictionary
d = {'k1':1, 'k2':2, "k3":3}
for key,value in d.items():
    print(key, value)

#3------------------------WHILE LOOPS--------------------------
x =0
while x<5:
    print(f"The current value of x is {x}")
    x+=1
else: 
    print('X is not less than 5')

#pass
x=[1,2,3]
for item in x:
    pass     #do nothing at all

#continue
mystring = 'Sammy' 
for letter in mystring:
    if letter == 'a':
        continue     #goes to top of loop
    print(letter)

#break
x = 0
while x<5:
    if x ==2:
        break       #break out of loop
    print(x)
    x+=1

#-----------------------USEFUL OPERATORS-------------------------
#RANGE
for num in range(0,11,2):
    print(num)

print(list(range(0,11,2)))

#Enumerate
index_count = 0
word = 'abcde'
for letter in word:
    print(word[index_count])
    index_count+=1

for item,letter in enumerate(word):
    print(item, letter )  

#ZIP
mylist = [1,2,3]
mylist2 = ['a','b','c']
mylist3 = [100,200,300]
for item in zip(mylist,mylist2,mylist3):
    print(item)

#min/max
mylist = [10,20,30,40]
print(min(mylist))
print(max(mylist))

#Random
from random import shuffle     #shuffles the list
mylist = [1,2,3,4,5,6,7,8,9,10]    
shuffle(mylist)   #inplace function
print(mylist)

from random import randint
print(randint(0,100))

#input
#result = input('Enter a name:')
# print(result)

#---------------------LIST COMPREHENSIONS------------------------
mystring = 'hello'
mylist = []
for letter in mystring:
    mylist.append(letter)
print(mylist)     

mylist =[letter for letter in mystring]
print(mylist)

mylist = [x for x in 'word']
print(mylist)

#-----------------------ASSESMENT TEST---------------------------------
#1
st = 'Print only the words that start with s in this sentence'
st_split = st.split()
print(st_split)

for letter in st_split:
    if letter[0] == 's':
        print(letter)

#2
list(range(0,11,2))
for i in range(1,11):
    if i%2 ==0:
        print(i)

#3
mylist = [num for num in range(1,51) if num%3==0]
print(mylist)

#4
st1 = 'Print every word in this sentence that has an even number of letters'
st1_split = st1.split()
print(st1_split)

for word in st1_split:
    if len(word)%2 ==0:
        print(word)

#5
l1 = list(range(1,101))
print(l1)
for i in l1:
    if i%3 ==0 and i%5 ==0:
        print("FIZZBUZZ")
    elif i %5 ==0:
        print('BUZZ')
    elif i%3 ==0:
        print("Fizz")
    else:
        print(i)