import random

print('Welcome to the Number Guessing Game!')
print("I'm thinking of a number between 1 and 100")

level = input("Choose a difficulty. Type 'easy' or 'hard' : ")

number = [i for i in range(1, 101)]

easy = [i for i in range(0, 11)]
hard = [i for i in range(0, 6)]

if level == 'easy':

    result_num = random.choice(number)

    for attempt in easy[::-1]:
        if attempt == 0:
            print("You've run out of guesses. Refresh the page to run again.")
            break

        print(f"You have {attempt} attempts remaining to guess the number.")
        guess = int(input('Make a guess: '))

        if guess < result_num:
            print("Too low")
        elif guess > result_num:
            print('Too high')
        else:
            print("That's right !!")
            break



if level == 'hard':

    result_num = random.choice(number)

    for attempt in hard[::-1]:
        if attempt == 0:
            print("You've run out of guesses. Refresh the page to run again.")
            break

        print(f"You have {attempt} attempts remaining to guess the number.")
        guess = int(input('Make a guess: '))

        if guess < result_num:
            print("Too low")
        elif guess > result_num:
            print('Too high')
        else:
            print("That's right !!")
            break

