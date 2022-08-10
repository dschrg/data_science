'''The game: Guess a number. Computer predict and guesses numbers'''
import numpy as np
def score_game(random_predict) -> int:
    """For how many attempts the algorithm will gueess the guessed number

    Args:
        random_predict (_type_): guessing function

    Returns:
        int: average quantity of tries
    """
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1,101, size = (1000))
    for number in random_array:
        count_ls.append(random_predict(number))
    score = int(np.mean(count_ls))
    
    print(f'Your algorithm guesses the number for {score} attempts in average')
    return(score)

    
def random_predict(number: int=1) -> int:
    """Guess a random number

    Args:
        number (int, optional): _description_. Defaults to 1.

    Returns:
        int: quantity of tries
    """
    count = 0
    while True:
        count += 1
        predict_number = np.random.randint(1,101) # a predict number
        if number == predict_number:
            break # exit from cycle
    return(count)

print(f'Quantity of tries: {random_predict()}')

if __name__ == '__main__':
    jscore_game(random_predict)

