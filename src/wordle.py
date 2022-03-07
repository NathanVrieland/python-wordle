import random
def main():
    printTitle()
    word = loadAnswer()
    valid_list = loadValidWords()
    guess = [""]
    # print("".join(word)) # cheat
    while guess != word and guess != []:
        guess_string = input()
        guess = list(guess_string)
        if len(guess) != 5:
            print("guess needs to be 5 letters")
            continue
        if guess_string not in valid_list:
            print("not a valid word!")
            continue
        for guess_index, guess_letter in enumerate(guess):
            in_word = False
            in_spot = False
            for word_index, word_letter in enumerate(word):
                if guess_letter == word_letter:
                    in_word = True
                    if guess_index == word_index:
                        in_spot = True
            if in_spot:
                printGreen(guess_letter)
            elif in_word:
                printYellow(guess_letter)
            else:
                print(guess_letter, end='')
        print()

def printGreen(character):
    print(f"\033[92m{character}\033[0m",end='')
        
def printYellow(character):
    print(f"\033[93m{character}\033[0m",end='')

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
        
if __name__ == "__main__":
    main()