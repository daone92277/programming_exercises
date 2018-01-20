import random
def guessing_game():
    secret_number = random.randint(1,20)
    print "I am thinking of a number between 1 and 10"
    print secret_number
    for guesses_taken in range(1,7):
        print "Take a guess"
        guess = int(input())

    if guess < secret_number:
        print "Your guess is too Low "
    
    elif guess > secret_number:
        print "Your guess is too high"
        break
    
    if guess == secret_number:
        print "Great Job Sir, You guessed the number", str(secret_number)
    else:
        print ("Nope. The number i was thinking of was:", str(secret_number)

guessing_game()