# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string
import sys
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

# end of helper code

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
    guess = []
    for letter in list(secret_word):
        if letter in letters_guessed:
            guess.append(1)
    if len(list((secret_word))) == len(guess):
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
    hint = []
    list_word = list(secret_word)
    for letter in list_word:
        if letter not in letters_guessed:
            hint.append("_ ")
        else:
            hint.append(letter)
               
    return "".join(hint)


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    alpha = string.ascii_lowercase
    available = []
    for element in alpha:
        if element not in letters_guessed:
            available.append(element)
    return "".join(available)
            
    
    
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

    print("Welcome to the game Hangman!")
    print("I'm thinking of a word that is " + str(len(secret_word)) + " letters long.")
    print("You have 3 warnings left.")
    print("------------------------")
    
    letters_guessed = []
    guess_remaining = 6
    warning_remaining = 3
    unique_letters = len(set(secret_word)) # set this for calculate the score
    
    while is_word_guessed(secret_word,letters_guessed) is False:
        
        if guess_remaining >0:
            print("You have " + str(guess_remaining )+ " guesses left.")
            print("Available letters: " + get_available_letters(letters_guessed))
            
            guess = input("Please guess a letter: ")
            guess = guess.lower()
            if guess == "quit":
                print("Thank you for joining the game. The word was",secret_word)
                sys.exit()
                
            elif guess not in list(string.ascii_lowercase):
                warning_remaining -= 1
                print("You can only input an alphbet, not symbols or numbers. You have",str(warning_remaining), "warnings left: \n", str(get_guessed_word(secret_word,letters_guessed)) )
                
            

            elif guess in list(secret_word): 
                if guess not in letters_guessed:
                    letters_guessed.append(guess)
                    print("Good guess: " + str(get_guessed_word(secret_word,letters_guessed)))
                    print("------------------------")
                else:
                    warning_remaining -= 1
                    print("Oops! You have already guessed that letter. You have", str(warning_remaining), "warnings left: \n", str(get_guessed_word(secret_word,letters_guessed))) 

            else:       # i.e.  elif guess not in list(secret_word):
                if guess not in letters_guessed:
                    letters_guessed.append(guess)
                    print("Oops! That letter is not in my word: " + str(get_guessed_word(secret_word,letters_guessed)))
                    print("------------------------")
                    guess_remaining -= 1
                else:
                    warning_remaining -= 1
                    print("Oops! You have already guessed that letter. You have", str(warning_remaining), "warnings left: \n", str(get_guessed_word(secret_word,letters_guessed))) 
                    
        
        
        else:   
            print("Sorry, you ran out of guesses.The word was", secret_word)
            sys.exit()
        
    print("Congradulations, you won! \nYour total score for this game is:", str(guess_remaining * unique_letters))

    


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


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
    my_word = my_word.replace(" ", "")  # remove the spaces between underlines
    my_word = list(my_word)
    other_word_mutate = list(other_word)
    missed_letters = []
    if len(my_word) == len(other_word):
        for i in range(len(my_word)):
            if my_word[i] == "_":
                other_word_mutate[i] = "_"
                missed_letters.append(other_word[i])
        if my_word == other_word_mutate: 
            for element in missed_letters:
                if element not in other_word_mutate:
                    return True
                else:
                    return False
        else:
            return False
    else: 
        return False



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    possible = []
    for word in wordlist:
       if match_with_gaps(my_word, word) is True:
                possible.append(word)
    
    if len(possible) > 0:
        return ",".join(possible)
    else:
        return("No matches found")



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
    print("Welcome to the game Hangman!")
    print("I'm thinking of a word that is " + str(len(secret_word)) + " letters long.")
    print("------------------------")
    
    letters_guessed = []
    guess_remaining = 6
    warning_remaining = 3
    unique_letters = len(set(secret_word)) # set this for calculate the score
    
    while is_word_guessed(secret_word,letters_guessed) is False:
        
        if guess_remaining > 0:
            print("You have " + str(guess_remaining )+ " guesses left.")
            print("Available letters: " + get_available_letters(letters_guessed))
            
            guess = input("Please guess a letter: ")
            guess = guess.lower()
            if guess == "quit":
                print("Thank you for joining the game. The word was",secret_word)
                sys.exit()
            
            elif guess == "*":
                my_word = get_guessed_word(secret_word,letters_guessed)
                print("Possible word matches are: \n", show_possible_matches(my_word))
            
              
            elif guess not in list(string.ascii_lowercase):
                warning_remaining -= 1
                print("You can only input an alphbet, not symbols or numbers. You have",str(warning_remaining), "warnings left: \n", str(get_guessed_word(secret_word,letters_guessed)) )
                

            elif guess in list(secret_word): 
                if guess not in letters_guessed:
                    letters_guessed.append(guess)
                    print("Good guess: " + str(get_guessed_word(secret_word,letters_guessed)))
                    print("------------------------")
                else:
                    warning_remaining -= 1
                    print("Oops! You have already guessed that letter. You have", str(warning_remaining), "warnings left: \n", str(get_guessed_word(secret_word,letters_guessed))) 

            else:       # i.e.  elif guess not in list(secret_word):
                if guess not in letters_guessed:
                    letters_guessed.append(guess)
                    print("Oops! That letter is not in my word: " + str(get_guessed_word(secret_word,letters_guessed)))
                    print("------------------------")
                    guess_remaining -= 1
                else:
                    warning_remaining -= 1
                    print("Oops! You have already guessed that letter. You have", str(warning_remaining), "warnings left: \n", str(get_guessed_word(secret_word,letters_guessed))) 
                    
        
        
        else:   
            print("Sorry, you ran out of guesses.The word was", secret_word)
            sys.exit()
        
    print("Congradulations, you won! \nYour total score for this game is:", str(guess_remaining * unique_letters))

    




# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
   #secret_word = choose_word(wordlist)
   #hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
    

    #secret_word = 'apple'
    #hangman(secret_word)