number = 20
guess = int(input('Enter an integer : '))

if guess < number:
    print('No, it is a little higher than that.')
elif guess > number:
    print('No, it is a little lower than that.')
else guess == number:
    print('Congratulations, you guessed it.')