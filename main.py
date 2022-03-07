#Basic - Print all integers from 0 to 150.

for i in range(0, 151):
    print(i)

#Multiples of Five - Print all the multiples of 5 from 5 to 1,000

#(start, end, increment)
for i in range(5, 1001, 5): 
    print(i)


# Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
#use modulus operator - denoted by % producing the remainder of an integer division
for i in range(0, 101):
    if i % 10 == 0:
        print('coding dojo')
    elif i % 5 == 0:
        print('coding')
    else:
        print(i)



# Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.

x = 0
for i in range(1, 500001, 2):
    x += i

print(x)



# Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.

for i in range(2018,0,-4):
    print(i)


"""
Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, 
print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, 
the loop should print 3, 6, 9 (on successive lines)
"""

low = 2
high = 9
mult = 3

for i in range(low, high +1):
    if i % mult == 0:
        print(i)


list = ['subscribe', 'to', 'mav', 'red']
for i in list: 
        print(i)


