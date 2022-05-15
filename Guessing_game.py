import random

def askforcode():
    while True:
        code = input('Guess: ') # Enter the guess.
        if code.isdecimal():
            return int(code) # Convert string guess to an integer.
        print('Please enter a number between 1 and 10.')


print('''let's play a game: guess the code''')
print()
guess = random.randint(1, 10) # Select a random number.
print('Guess should be in between 1 to 10.')

for i in range(3): # Give the player 10 guesses.
    print('You have {} guesses left....'.format(3 - i))

    code = askforcode()
    if code == guess:
        break
    # Break out of the for loop if the guess is correct.
    if code > 10:
        print("Enter a number between 1 to 10")

    # Offer a hint:
    if code < guess:
        print('guess was low.')
    if code > guess:
        print('guess was high.')

# Reveal the results:
if code == guess:
        print('Yay! You guessed my number!')
else:
        print('Your Game is over. \nThe number was', guess)
