import answers
import random

print('\n-----------------CHAT BOT-----------------')

while True:
    userInput = input('User: ').lower()

    # Check if the user asked an empty question
    if not userInput.strip():
        print('Bot: Goodbye!')
        break

    found_word = False

    # Check for hello words
    for hello_word in answers.helloWords:
        if hello_word in userInput:
            response = random.choice(answers.helloWordsAnswers)
            print(f'Bot: {response}')
            found_word = True
            break

    # Check for time words only if a hello word is not found
    if not found_word:
        for time_word in answers.timeQuestions:
            if time_word in userInput:
                response = random.choice(answers.timeAnswers)
                print(f'Bot: {response}')
                found_word = True
                break

    # Check for date
    if not found_word:
        for date_word in answers.dateQuestions:
            if date_word in userInput:
                response = random.choice(answers.dateAnswers)
                print(f'Bot: {response}')
                found_word = True
                break

    # Check for tech
    if not found_word:
        for tech_word in answers.techQuestions:
            if tech_word in userInput:
                response = random.choice(answers.techAnswers)
                print(f'Bot: {response}')
                found_word = True
                break

    # Check for programming
    if not found_word:
        for code_word in answers.programmingQuestions:
            if code_word in userInput:
                response = random.choice(answers.programmingAnswers)
                print(f'Bot: {response}')
                found_word = True
                break

    # Check for jokes
    if not found_word:
        for joke_word in answers.jokesQuestions:
            if joke_word in userInput:
                response = random.choice(answers.jokesAnswers)
                print(f'Bot: {response}')
                found_word = True
                break

    # Check for origin
    if not found_word:
        for origin_word in answers.originQuestions:
            if origin_word in userInput:
                response = random.choice(answers.originAnswers)
                print(f'Bot: {response}')
                found_word = True
                break

    # Check for origin
    if not found_word:
        for fun_word in answers.funFactQuestions:
            if fun_word in userInput:
                response = random.choice(answers.funFactAnswers)
                print(f'Bot: {response}')
                found_word = True
                break

    # If neither hello word nor time word is found, print "Did not understand"
    if not found_word:
        print('Bot: Did not understand')
