'''  # 1 demonstrates assigning an integer to a variable
x = 4
y = 5

print (y + x)

# 2 Assigning a string to a variable
x = 'Im a string!'

print x


# 3 assigning a float to a variable
x = 5.5

# 4 using print function with formatting 
print 'Hello {} people!'.format('party')

# 5 math functions
# +
print (y + x)
# -
print (y - x)
# *
print (y * x)
# /
print (x / y)
# +=
count = 0
while count < 20:
     print (count)
     count += 1

# if, elif, else
x = 5

if x == 10:
            print 'x = 10'

elif x == 9:
            print 'x = 9'

else:
            print 'x does not equal 9 or 10' 

#and, or, not
x = 5

if (x < 10) and (x > 1):
            print 'True'

if (x < 10) or (x > 1):
            print 'True'

not ('call' == 'car')

#while loop
password = ''
while password != 'cars':
    password = raw_input('\nPlease input password: ')
    if password == 'cars':
            print 'Thank you that is the correct password!'
    else:
        print 'Password incorrect try again' 

# for loop
for x in range(0, 100):
    print ('Dude went {}!').format(x) 

#iterating through list using a for loop
someList = ['a','b','c','d']
for x in lst:
    print x

#iterating through tuple using a for loop
someTuple = ('a','b','c','d')
for x in tup:
    print x   '''

#defining function that returns a string variable
a = 'Get Ready'
b = 'Get Set!'
c = 'GO!'
def racePrep ():
    print a
    print b
    print c
#calling the function
racePrep()


    
    


