# 6.00 Problem Set 3
#
# Hangman
#


# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
import string

WORDLIST_FILENAME = "/Users/janko/Dropbox/_active/dev/MIT600/ps2/words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# actually load the dictionary of words and point to it with
# the wordlist variable so that it can be accessed from anywhere
# in the program
wordToGuess = list(choose_word(load_words()))
numOfGuesses = 0
printed = ""
for i in range(len(wordToGuess)):
    printed += "_"
printed = list(printed)

def guessing(userInput):
    global numOfGuesses
    global wordToGuess
    global printed
    i = 0
    for letter in wordToGuess:
        if userInput == letter:
            printed[i] = letter
        i += 1
    numOfGuesses += 1
    return ''.join(printed)

def stringChecker(userInput):
    global numOfGuesses
    global wordToGuess
    global printed
    userInput = userInput.lower()
    alphabeth = "abcdefghijklmnopqrstuvwxyz"
    for letter in userInput:
        for alphabethLetter in alphabeth:
            if letter != alphabethLetter:
                check = False
            else:
                check = True
                break
        if check == False:
            return "Try letters!"
        elif check == True:
            trial = guessing(letter)
            return trial
        else:
            return "unknown error!"





print "\n##############\n#HANGMAN GAME#\n##############\n\nHello, welcome to hangman game, \nyou're playing with computer \nthe word to guess is: " + ''.join(printed) + "\nit's " + str(len(printed)) + " letters long!"

while numOfGuesses < 20:
    print "\nTURN " + str(numOfGuesses) + " : : : : : : : : :" + "\nYou have " + str(20 - numOfGuesses) + " tries left!\nNow take the guess!"
    userText = raw_input()
    print "\n" + stringChecker(userText)
    if printed == wordToGuess:
        print "Congratulations! You won!"
        break

if printed != wordToGuess:
    print "Failure! The correct awnser was: " + ''.join(wordToGuess)

# your code begins here!
