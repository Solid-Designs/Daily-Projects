# sentence = 'This is a common interview question'

# # Find the most repeated character in this text
# # Create a count variable
# # Loop through the string and grab the value
# # See how many times the character shows up
# # Compare it to the highest amount previously
# # if it is higher then change the character


# def most_repeated(string):
#     repeat_count = 0
#     highest_character = ''
#     for character in string:
#         if string.count(character) > repeat_count:
#             highest_character = character
#             repeat_count = string.count(character)

#     print(f'The most repeated character in this text is: {highest_character}')


# most_repeated(sentence)

# ----------------------------------------------------
# Exceptions
try:
    with open('app.py') as file:
        print('File opened')

    age = int(input('Age: '))
    xfactor = 10/age
except (ValueError, ZeroDivisionError):
    print('You didn\'t enter a valid age')
else:
    print('No exceptions here')
