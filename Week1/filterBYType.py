#Integer
#If the integer is greater than or equal to 100, 
# print "That's a big number!" If the integer is less than 100, print "That's a small number"

num = 4.3
print type(num)
if num >= 100:
    print "That's a Big Number!"
elif num < 100:
    print "That's a small number" 
print "The number is " + str(num)

#String
#If the string is greater than or equal to 50 characters 
#print "Long sentence." If the string is shorter than 50 characters print "Short sentence."

longstr = "this has to be greater than or equal to 50 freaking characters"

print "length of string:", len(longstr)

length = len(longstr)

if length >=50:
     print "Long Sentence!"
elif length < 100:
    print "That's a small number" 
print "The number is " + str(length)

#if the length of the list is greater than or equal to 10 print "Big list!" If the list has fewer than 10 values print "Short list."

#Test your program using these examples:
mL = [3,5,7,34,3,2,113,65,8,89]
items = len(mL)
print "The number # of items in the list is: ", items
if items >=10:
    print "This is a big god damn list!"
elif items <10:
    print "little ass list!"
