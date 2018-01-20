#Write a program that prints all the prime numbers and all the perfect squares for all numbers between 100 and 100000.
#For all numbers between 100 and 100000 test that number for whether it is prime or a perfect square.

def foobar():
    number = str(input("Aman Please enter a number before I fuck you up: "))

    for number in range(100,100000):
        if number % 2 == 0:
                print "Foo" + number
                
        if (number**2) == 0:
                print "Bar" + number
        else:
            
                break
        
foobar()
  