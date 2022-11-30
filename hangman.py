# Problem Set 2, hangman.py
# Name: Dariia Belovol
# Collaborators:
# Time spent: 2 days

# Hangman Game
# -----------------------------------
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    letters = set(secret_word)
    letters_g = set(letters_guessed)
    secret_w = set(secret_word)
    if ((letters_g.intersection(letters)) == secret_w): 
      return True
    else: 
      return False 



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    letters = set(secret_word)
    letters_g = set(letters_guessed)
    list = letters.difference(letters_g)
    unknown = secret_word
    for i in list:
      unknown = unknown.replace(i, '_ ')
    return unknown

global letters_guessed
letters_guessed = set()
def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    lst = string.ascii_lowercase
    left = lst
    for letter_guess in letters_guessed:
        left = left.replace(letter_guess, '')
    return left



def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    letters_guessed = set()
    guesses = 6
    warning = 3
    print('Welcome to the game Hangman!\nI am thinking of a word that is ', len(secret_word), ' letters long.')
    print('-'*25)
    while guesses > 0:
        
        print('You have', guesses, 'guesses left. \nAvailable letters: ', get_available_letters(letters_guessed = letters_guessed))
        letter_guess = input('Please guess a letter:')
        letter_guess.lower()
        trying = get_guessed_word(secret_word, letters_guessed)
        attempts = False

        vowels = ['a', 'e', 'i', 'o', 'u', 'y', 'w']
        if letter_guess.isalpha() and len(letter_guess) == 1:
          if letter_guess in secret_word and letter_guess not in letters_guessed:
            
            letters_guessed.add(letter_guess)
            print(f'Good guess: {get_guessed_word(secret_word, letters_guessed)}') 
            print('-'*25)
          elif letter_guess not in secret_word:
            print(f"Oops! That letter in not in my word: {get_guessed_word(secret_word, letters_guessed)}")
            print('You have', guesses , 'guesses left.')
            print('-'*25)
            if letter_guess in vowels:
                warnings_1 = 2
            else:
                warnings_1 = 1
            guesses -= warnings_1
          elif letter_guess in letters_guessed:
            if warning > 0:
              warning -=1
            else:
              goal -=1
              warning +=3
            print(f'Oops! You have already guessed that letter: {get_guessed_word(secret_word, letters_guessed)}')
            print('-'*25)
        elif letter_guess.isalpha() is False or len(letter_guess) != 1:
            if warning > 0:
              warning -=1
            else:
              goal -=1
              warning +=3
            print(f'Oops!\nThat is not a valid letter : {get_guessed_word(secret_word, letters_guessed)} You have ', warning, ' warnings left.')
            print('You can only enter a letter')
            print('-'*25)
        if is_word_guessed(secret_word, letters_guessed):
            set_goals = set(secret_word)
            goal = 0
            for i in set_goals:
                goal += 1
            print("Congratulations, you won!!! Your total score for this game is:", goal*guesses)
            print('-'*25)
            break
    else:
        print('Sorry, you lose:( \nThe word was: ', secret_word)
        print('-'*25)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    list_my_word = str.strip(my_word)
    lst_my_word =  set(list_my_word.replace('_', ''))
    other_word_list = list(other_word)
    if len(my_word) != len(other_word) or lst_my_word != other_word_list:
        return False
    else:
        return True

    
      


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    my_word_list = list(my_word)
    word_resault = ''
    list = 0
    for i in my_word_list:
      if match_with_gaps(word_resault, i):
            list += 1
            print(i, end=" ")
    
    if len(list)>0:
      print(i, end=" ")
    else:
      print('No matches found')
    



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    letters_guessed = set()
    guesses = 6
    warning = 3
    print('Welcome to the game Hangman!\nI am thinking of a word that is ', len(secret_word), ' letters long.')
    print('-'*25)
    while guesses > 0:
        
        print('You have', guesses, 'guesses left. \nAvailable letters: ', get_available_letters(letters_guessed = letters_guessed))
        letter_guess = input('Please guess a letter:')
        letter_guess.lower()
        trying = get_guessed_word(secret_word, letters_guessed)
        attempts = False

        vowels = ['a', 'e', 'i', 'o', 'u', 'y', 'w']
        if letter_guess.isalpha() and len(letter_guess) == 1:
          if letter_guess in secret_word and letter_guess not in letters_guessed:
            
            letters_guessed.add(letter_guess)
            print(f'Good guess: {get_guessed_word(secret_word, letters_guessed)}') 
            print('-'*25)
          elif letter_guess not in secret_word:
            print(f"Oops! That letter in not in my word: {get_guessed_word(secret_word, letters_guessed)}")
            print('You have', guesses , 'guesses left.')
            print('-'*25)
            if letter_guess in vowels:
                warnings_1 = 2
            else:
                warnings_1 = 1
            guesses -= warnings_1
          elif letter_guess in letters_guessed:
            if warning > 0:
              warning -=1
            else:
              goal -=1
              warning +=3
            print(f'Oops! You have already guessed that letter: {get_guessed_word(secret_word, letters_guessed)}')
            print('-'*25)
        elif letter_guess.isalpha() is False or len(letter_guess) != 1:
            if warning > 0:
              warning -=1
            else:
              goal -=1
              warning +=3
            print(f'Oops!\nThat is not a valid letter : {get_guessed_word(secret_word, letters_guessed)} You have ', warning, ' warnings left.')
            print('You can only enter a letter')
            print('-'*25)
        if is_word_guessed(secret_word, letters_guessed):
            set_goals = set(secret_word)
            goal = 0
            for i in set_goals:
                goal += 1
            print("Congratulations, you won!!! Your total score for this game is:", goal*guesses)
            print('-'*25)
            break
    else:
        print('Sorry, you lose:( \nThe word was: ', secret_word)
        print('-'*25)





if __name__ == "__main__":
   
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
