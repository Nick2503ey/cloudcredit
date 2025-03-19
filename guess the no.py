### Program for Guessing the nunber


import random

def guess_no():
    no_to_guess = random.randint(1, 150)        # generate a random no between 1 to 150 

    attempt=8                                  # total no. of attemp 

    print ('Guess a number between 1 to 150, you have 8 attempts')

    while attempt > 0:
        try:
            guess =  int(input('Guess the no: '))
            if guess > no_to_guess:
                print('Sorry, try again, Too high')
            elif guess < no_to_guess:
                print ('Sorry, try again, Too Low')
            else :
                print (f'YAY!!! Congrats you have guess the right number {no_to_guess}')
                break
            attempt -= 1
            print(f"you have  {attempt} attempt remaining")

            
        except ValueError:
            print('Invalid input, Enter the number again')
    attempt == 0                        # when the attempt is finish its show the correct no
    print (f"Sorry You are out of attempt, the correct number was {no_to_guess}") 

guess_no()

        