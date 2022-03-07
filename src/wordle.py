"""
wordle.py: text based wordle clone written in python
@author: nathan vrieland
"""
import random

def main():
    answer = loadAnswer()
    valid_list = loadValidWords()
    guess = ""
    guess_list = [""]
    guess_log = []
    # print("".join(word)) # cheat
    while guess != answer and guess_list != []:
        print(chr(27)+'[2j\n\033c\n\x1bc') # ANSI escape sequence to clear console
        printTitle()
        for i in guess_log:
            print(i)
        guess = input()
        guess_list = list(guess)
        if not correctLength(guess):
            continue
        if not valid(guess, valid_list):
            continue
        guess_log.append(colorWord(guess, answer))
        
        


        

def getGreen(character) -> str:
    return f"\033[92m{character}\033[0m"
        
def getYellow(character) -> str:
    return f"\033[93m{character}\033[0m"

def printTitle():
    with open("title.txt", "r") as title_file:
        title_string = title_file.read()
        print(title_string)

def loadAnswer() -> str:
    with open("possible_answers.txt", "r") as list_file:
        word_list = list_file.read().split(",")
        word = list(random.choice(word_list))
        return word

def loadValidWords() -> list:
    with open("5_letter_english_words.txt", "r") as words:
        words_string = words.read().lower()
        return words_string.split("\n")

def colorWord(guess, answer) -> str:
    ret = ""
    for guess_index, guess_letter in enumerate(guess):
            in_word = False
            in_spot = False
            for word_index, word_letter in enumerate(answer):
                if guess_letter == word_letter:
                    in_word = True
                    if guess_index == word_index:
                        in_spot = True
            if in_spot:
                ret += getGreen(guess_letter)
            elif in_word:
                ret += getYellow(guess_letter)
            else:
                ret += guess_letter
    return ret

def correctLength(guess) -> bool:
    return len(guess) == 5

def valid(guess, valid_words) -> bool:
    return guess in valid_words
        
if __name__ == "__main__":
    main()