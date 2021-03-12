import random #Imports the random module


print()
print('Magic 8 ball says... ') #First line (text string)
def get_answer(answer_number): #get_answer function is defined
    if answer_number == 1:
        return 'It is certain.'
    elif answer_number == 2:
        return 'It is decidedly so.'
    elif answer_number == 3:
        return 'Yes.'
    elif answer_number == 4:
        return 'Reply hazy try again.'
    elif answer_number == 5:
        return 'Ask again later.'
    elif answer_number == 6:
        return 'Concentrate and ask again.'
    elif answer_number == 7:
        return 'My reply is no.'
    elif answer_number == 8:
        return 'Outlook not so good.'
    elif answer_number == 9:
        return 'Very doubtful.'

r = random.randint(1, 9) #random integer between 1 & 9 is called and stored in a variable called r
get_answer(r) #get_answer function is called with r as the argument
print(get_answer(r))




