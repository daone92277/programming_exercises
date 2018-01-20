#import random
def gradeScale():
     
    for i in range(10): #run the loop ten (10) times
        score = input("Please enter your pitiful score sir:  ")
        # score = random.randint(60,100)
        #print score
        if score <=70:
            print "Your Score is : ", score,  " Your grade is a D"
           
        elif score <=80:
            print "Your Score is : ", score, " Your grade is a C"
            
        elif score <=90:
            print "Your Score is : ", score, " Your grade is a B"
           
        else:
            print "Your Score is : ", score, " Your grade is a A"
            


gradeScale()
print "You should be Proud!!!!"