'''this programm guesses a number'''
import numpy as np
number = np.random.randint(1,101) # we've picked a number
count = 0
while True:
    count += 1
    predict_number = int(input('Guess a number from 1 till 100: '))
    
    if predict_number > number:
        print('Your number is more than predict_number!')
    elif predict_number < number:
        print('Your number is less than predict_number!')
    else:
        print(f'You have guessed the number! This number is {number}, for {count} tries')
        break

