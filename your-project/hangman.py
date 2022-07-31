import random
import re

print("Welcome to Hangman world edition!")
print("""\nThere are multiple difficulties.
\n• 1 Easy (Limited to 40 very popular countries and you have 7 lives.)
\n• 2 Intermediate (Limited to 80 popular countries and you have 6 lives.)
\n• 3 Hard (Every single country is included and you only have 5 lives!)""")

play = True
while play == True:
    number_of_lives = ()
    country_list = []

    def settings():
        while True:
            valid_answers = ('1', '2', '3')
            difficulty = (
                input("\nPlease enter a difficulty by typing its number (1 = Easy, 2 = Intermediate, 3 = Hard): "))
            while difficulty not in valid_answers:
                difficulty = (input(
                    "Not a valid difficulty.\nPlease enter a difficulty by typing its number (1 = Easy, 2 = Intermediate, 3 = Hard): "))
            if difficulty == '1':
                print("\nYou have chosen Easy and you have 7 lives!")
                break
            elif difficulty == '2':
                print("\nYou have chosen Intermediate and you have 6 lives!")
                break
            elif difficulty == '3':
                print("\nYou have chosen Hard and you have 5 lives! Good luck!")
                break
            else:
                break
        return difficulty

    difficulty = ()
    difficulty = settings()

    def lives():
        if difficulty == '1':
            number_of_lives = 7
            return number_of_lives
        if difficulty == '2':
            number_of_lives = 6
            return number_of_lives
        else:
            number_of_lives = 5
            return number_of_lives

    number_of_lives = lives()

    def read_file(difficulty):
        if difficulty == '1':
            with open("easy.txt") as f:
                country_list = f.read().splitlines()
                return country_list
        elif difficulty == '2':
            with open("intermediate.txt") as f:
                country_list = f.read().splitlines()
                return country_list
        else:
            with open("all_countries.txt") as f:
                country_list = f.read().splitlines()
                return country_list


    country_list = read_file(difficulty)

    def randomize():
        random_country = random.randint(0, len(country_list))
        chosen_country = country_list[random_country]
        return chosen_country

    chosen_country = randomize()

    def encode_country(chosen_country):
        encoded_country = re.sub('[a-zA-Z]', '?', chosen_country)
        return encoded_country


    encoded_country = encode_country(chosen_country)

    print("\nLet's start!"
                                                       """  
        +---+
        |   |
            |
            |
            |
            |
        =========""")

    def guess(letter, word, encoded):
        found = False
        if letter in word:
            found = True
            for i in range(0, len(word)):
                if word[i] == letter:
                    encoded = encoded[0:i] + letter + encoded[i+1:len(encoded)]
        return (found, encoded)

    letter_found = ''

    while(number_of_lives > 0):
        guessed_letter = input(str("\nGuess a letter: "))[:1]
        if not guessed_letter.isalpha():
            print("\nOnly letters are allowed!")
            guessed_letter = input(str("\nGuess a letter: "))[:1]

        letter_found, encoded_country = guess(guessed_letter, chosen_country, encoded_country)

        if not letter_found:
            number_of_lives -= 1
            if number_of_lives == 0:
                print("\nGame over! You lost!" 
                      '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    ========='''
                      "\nThe country was: ", chosen_country)
                break
            else:
                print("\nThat letter was not found. You now have", number_of_lives, "lives left.\n")
                print(encoded_country)
        else:
            if "?" not in encoded_country:
                print("\nCongratulations! You won with", number_of_lives, "lives remaining. The country was: ", chosen_country)
                break
            else:
                print("\nGood job! That letter was found. You still have", number_of_lives, "lives left!\n")
                print(encoded_country)

    again = input("\nWould you like to play again? ")

    if again not in ['yes', 'no', 'Yes', 'No', 'Y', 'y', 'n', 'N', 'yep', 'Yep', 'nope', 'Nope', 'nel', 'yes en ingles']:
        print(("\nInvalid answer. Please type yes or no."))
        again = input("\nWould you like to play again? ")

    if again in ['yes', 'Yes', 'y', 'Y', 'yep', 'Yep', 'yes en ingles']:
        play = True
    if again in ['no', 'No', 'n', 'N', 'nope', 'Nope', 'nel']:
        play = False