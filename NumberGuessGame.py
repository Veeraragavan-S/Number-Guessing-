import random

top_of_range=input("Type a number:) ")

if top_of_range.isdigit():
    top_of_range=int(top_of_range)
    if top_of_range>0:
        print("Okay..Lets play")
    else:
        print("Type a number greater than 0!")
        quit()
else:
    print("Type only a number greater than 0!")
    quit()
    
guesses=0

random_number=random.randint(0,top_of_range)

while True:
    guesses+=1
    
    user_guess=input(f"Make a guess between 0 to {top_of_range} ")

    if user_guess.isdigit():
        user_guess=int(user_guess)
        if user_guess==random_number:
            print("You got it..That's correct")
            break
        elif user_guess>random_number:
            print("You guessed above the number")
        else:
            print("You guessed below the number")
            
    else:
        print("Type only a number!")
        
        
print(f"you guessed the number in {guesses} guesses")
        