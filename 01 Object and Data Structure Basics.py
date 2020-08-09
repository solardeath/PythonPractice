##slicing

a = 'abcdefg'


print(a[3:6:1]) 


print('hello')

b = 'abcdefghijk'

print(b[2::2])    

##-----STRING FUNCTIONS--------------------------------------------------

##split

c = 'Hello world this is a string'
print(c.split())
print(c.split('i'))  #split where letter 'i'
print(c.upper())  #string to upper case
print(c.lower())    #string to lower case


##---------STRING FORMATTING-----------------------------------------

#.format()

print('Hi my name is {} {}'.format('Pronnoy','Dutta'))
print('The {1} {0} {2}'.format('brown', 'quick', 'fox'))
print('The {q} {b} {f}'.format(b='brown', q= 'quick', f='fox'))
result = 100/777
print(result)
print('The result was {r:1.2f}'.format(r = result))

#f-string
name = 'Neil'
print(f'My name is {name}')

## ---------------LISTS-------------------------------------------
my_list = [1,2,3]
my_list = ['String',100, 23.2]
print(len(my_list))
my_list = ['one', 'two', 'three']
my_list[0]
print(my_list[1:])
another_list = ['four', 'five']
new_list = my_list + another_list
print(new_list)
new_list[0]= 'ONE ALL CAPS'
print(new_list)

new_list.append('six')   #add to last index
print(new_list)

new_list.pop()          #delete from last index
print(new_list)

new_list = ['a','e','x','b','c']
num_list = [4,1,2,3]
new_list.sort()         #SORT ASCENDING ORDER in place
print(new_list)

num_list.sort()
print(num_list)

num_list.reverse()      #Sort Descending order

##--------------------DICTIONARIES-----------------------------

my_dict = {'key1' : 'value', 'key2' : 'value2'}
print(my_dict['key1'])
prices_lookup = {'apple':2.99, 'banana':3.44}
print(prices_lookup['apple'])
d = {'key1':['a','b','c']}
my_list= d['key1']
print(my_list)
letter = my_list[2]
print(letter.upper())
d['k3'] = 300
print(d)
print(d.keys())         #get all keys
print(d.values())       #get all values 
print(d.items())        #get all items

##-------------------TUPLES-------------------------------------
t = (1,2,3)
my_list = [1,2,3]
print(type(t))
print(type(my_list))
t = ('a','a','b')
print(t.count('a'))           #occurences of a
print(t.index('a'))           #index of a
# t[0] = 'NEW'                #Cannot reassign 

##--------------------SETS----------------------------------------
myset = set()
myset.add(1)
myset.add(2)
myset.add(2)                #only 1 unique element
print(myset)
mylist = [1,1,1,1,2,2,2,2,2,3,3,3]
print(set(mylist))

##------------------BOOLEANS-----------------------------------
print(type(False))
print(1>3)
print(1==3)

##-----------------I/O With Basic Files-------------------------
myfile = open('myfile.txt')
print(myfile.read())        #read file
myfile.seek(0)             #reset pointer to 0
print(myfile.readlines())   #make list of the lines
myfile.close()

#other way to open file
with open('myfile.txt') as my_new_file:
    contents = my_new_file.read()
    print(contents)

with open('my_new_file.txt', mode='r') as f:
    print(f.read())
with open('my_new_file.txt', mode='a') as f:
    f.write('\nFOUR ON FOURTH')  
# with open('asd.txt', mode='w') as f:
#     f.write('I CREATED THIS FILE')

##--------------------ASSIGNMENT-----------------------------------------------
s = 'hello'
print(s[1])
print(s[::-1])
print(s[-1])
print(s[4])

list1 = [0,0,0]
list2 = [0]*3
print(list1, list2)
list3 = [1,2,[3,4,'hello']]
list3[2][2] = 'goodbye'
print(list3)
list4 = [5,3,4,6,1]
list4.sort()
print(list4)

d = {'simple_key':'hello'}           #grab hello in all
print(d['simple_key'])
d = {'k1':{'k2':'hello'}}
d1 = d['k1']
print(d1['k2'])
d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
d1 = d['k1']
d2 = d1[0]['nest_key'][1][0]
print(d2)
d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
d1 = d['k1']
print(d1[2]['k2'][1]['tough'][2][0])

list5 = [1,2,2,33,4,4,11,22,3,3,2]
print(set(list5))

print(3.0 == 3)
print(4**0.5 != 2)