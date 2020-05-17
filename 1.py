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

