num = 4
if num==4:
    print('number is 4')
else:
    if num==5:
        print('number is 5')
    else:
        if num==3:
            print('number is 3')
        else:
            print('number is not 3, 4 or 5')


num = 5
if num==4:
    print('number is 4')
elif num==6:
    print('number is 6')
elif num==7:
    print('number is 7')
elif num==5:
    print('number is 5')
else:

    
 13 mei 20 00.39 start
'''
Range
The range function creates a sequential list of numbers.
the code below generates a list containing all of the integers up to 10
'''
number = list(range(10))
print(number)
'''
the call to list is necessary because range by itself creates a range object,
and this must be converted to a list if you want to use it as one

it is worthly to note that the range function takes three arguments:
the beginning value, the ending value and the step
'''
a = range(10,25, 3)
b = list(a)
print(b)
print(a)

num= list(range(5))
print(num[4])
'''
If range is called with one argument, it produces an object with values from 0 to that argument.
If it is called with two arguments, it produces values from the first to the second. '''
num = list(range(3, 8))
print(num)
print(range(20) == range(0, 20))
print(len(num))

jon = list(range(4, 40, 4))
print(jon)
print(jon[8])

# 13 mei 20 01.31 istirahat

# 10 mei 20 01.07 istirahat
# 10 mei 20 12.55 start

# list
# contoh 1
word = ['helo', 'world', '!']
print(word[0])
print(word[1])
print(word[2])

# ex 2
mylist = [0, 'tahu', 2.3, 3, 'kunyit']
i=0
while i<5:
    print(mylist[i])
    i+=1

# empty list 
# ex 1
blok = [1, 45, 3, 4, 5, 6, 7]
print(blok)

blok = []
print(blok)

# ex 2
empty_list = []
print(empty_list)
print(type(empty_list))
print(id(empty_list))

empty_list = '[]'
print(empty_list)
print(id(empty_list))
print(type(empty_list)) 

number = 3
thing = ['string', 2, [1, 2, number], 4.56]
print(thing[0])
print(thing[2])
print(thing[2][2])
print(thing)

# ex 3
uhu = 'kujang'
print(uhu[2])

# ex 4
yog = [1, 2, 'tahu', 3.4]
print(yog[0], yog[2])

# 10 mei 20 13.51 istirahat
# 10 mei 20 16.38 start

# list operations
# the item at a certain index in a list can be reassigned

# ex 1
num = [2, 2, 2, 2, 2]
num[2] = 4
print(num) 

# ex 2
a = ['x', 'y']
b = a
b[0]='z'
print(b)
print(a)

'''
# ex 3
a = ['x', 'y']
b = a.copy()
b[0]='z'
print(b)
print(a)
'''
num = [0, 1, 2, 3, 4, 5]
num[3] = num[1]
print(num[3])

# list can be added and multiplied  in the same way as strings
num = [1, 2, 3]
print(num + [4, 5, 6])
print(num*3)

'''
 to check if an item is in a list, the in operator can be used, it return True if the item occurs
 on or more in the list, and False if it does not '''

# ex 1
num = ['plata', 'plomo', 'uza','narcos']
print('plata' in num)
print('uza' in num)
print('tahu'in num)

# ex 2
num = [10, 4, 3, 2, 6]
num[0] = num[4] - 2
if 4 in num:
    print (num[2])
else:
    print (num[1])

'''
words = ["anto","ani","andi","tio"]
guess = input("what word do you guess?")
print(guess)

if (guess in words) == True :
    print('right')
else:
    print('wrong')
    '''
# 10 mei 20 17.37 istirahat
# 10 mei 20 21.24 start

#  to check if an item is not in a list, you can use the not operator in one of the following ways
x = [1, 2, 3,[4,5]]
print(4 not in x)
print(not 4 in x)
print(2 not in x)
print(not 2 in x)
print(4 in x)
print(4 in x[3])

# 10 mei 20 22.28 istirahat
# 12 mei 20 01.39 start

'''
List Functions
Another way of altering lists is using the append method. 
This adds an item to the end of an existing list.
'''
nums = [1, 2, 3]
nums.append (4)
print(nums)

# to get the number of items in a list , youo can use the len funcion
num = [1, 2, 3, 4, 5, 6]
x = len(num)
print(x)

word = ['a', 'b', 'c']
word.append ('d')
print(len(word))

# The insert method is similar to append, 
# except that it allows you to insert a new item at any position in the list, 
# as opposed to just at the end.

wr = ['python', 'fun']
wr.insert (1, 'is')
print(wr)

wr = [1,2,4,3,2]
wr.insert (-1, 7)
print(wr)

num = [2, 4, 1, 2]
num.append(3)
num.insert(2,8)
print(len(num))

# The index method finds the first occurrence of a list item and returns its index.
# If the item isn't in the list, it raises a ValueError.
d = ['q', 'e','e', 'q', 'd', 'd']
x = d.index('d')
print(x)

'''
There are a few more useful functions and methods for lists. 
max(list): Returns the list item with the maximum value
min(list): Returns the list item with minimum value
list.count(obj): Returns a count of how many times an item occurs in a list
list.remove(obj): Removes an object from a list
list.reverse(): Reverses objects in a list
'''

# 12 mei 20 02.44 istirahat
# 13 mei 20 00.39 start

x = [1, 2, 4, 42, 1, 2,  3, 1]
r = ['rusa', 'kusing','anjing', 'kerbau']
d = max(x)
s = min(x)
q = x.count(1)
print(d)
print(s)
print(q)
print(x.count(2))
r.remove('rusa')
print(r)
r.reverse()
print(r)


# while loop
i = 1
while i <= 2:
    print(i)
    i = i + 1
print('finished!')

i = 3
while i >= 0:
    print(i)
    i = i - 1
print('done bitch')

x = 0
while x <= 4:
    print(x)
    x+=2
print('dayum')

# 9 mei 20 23.30

# break
# contoh 1
i = 0
while 1==1:
    print(i)
    i = i + 1
    if i >= 5:
        print('break !')
        break
print("finished")

# contoh 2
i=0
while i<5:
    print(i)
    i+=1
print('breaking!')
print('finished')

# contoh 3
i = 5
while True:
    print(i)
    i=i-1
    if i <= 2:
        break

# continue
# contoh 1
i = 0
while True:
    i = i + 1
    if i == 2:
        print('skipping 2')
        continue
    if i == 5:
        print('break')
        break
    print(i)
print('Finished')


# contoh 2
aboi = 30
kujang = 1
gelut = True

while gelut:
    aboi=aboi - 1
    print ('maneh nyerang si aboi! Darah:')
    print(aboi)
    if aboi == 15:
        print('si aboi setengah deui darah na')
        continue
    elif aboi == 10:
        print('paehan si aboi!')
        continue
    elif aboi == 5:
        print('ayeuna kesempatan maneh')
        continue
    if aboi <= 0:
        print('aboi ges paeh')
        break
print('wilujeng')

# 15 mei 20 00.18 start
# For Loop
words = ['aku', 'ingin', 'mahir', 'python', 'dengan', 'masagi']
counter = 0
max_index = len(words) - 1
while counter <= max_index :
    word = words[counter]
    print(word + '!')
    counter = counter + 1

print('\n')
words = ['aku', 'ingin', 'mahir', 'python', 'dengan', 'masagi']
counter = 0
while counter < len(words):
    word = words[counter]
    print(word + '!')
    counter+=1

# 15 mei 20 01.33 istirahat
# 16 Mei 20 01.52 Start
'''
Iterating through a list using a while loop requires quite a lot of code
, so python provides the for loop as a shortcut that acconplishes the same thing.
the same code from the previrous example can be written with a for loop, as follow '''

worlds = ['aku', 'ingin', 'mahir', 'python', 'dengan', 'masagi']
for word in worlds :
    print(word + '!')

for i in range(4):
    print('good')

# 16 mei 20 02.15 istirahat
