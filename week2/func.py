import random
import string

def randomWord():
    letter = '' 
    for i in range(random.randint(5, 10)):
        letter += random.choice(string.ascii_lowercase)
    
    return letter


def main():
    # 这里写主要的程序逻辑
    word = randomWord()
    blanks = blanks = word.__len__() * '_'

    while True:
        print('please guess the word, one letter each time: ', blanks)
        letter = input()
        if letter.__len__() != 1 or letter == '':
            continue
        if letter in word:
            for i in range(word.__len__()):
                if word[i] == letter:
                    blanks = blanks[:i] + letter + blanks[i+1:]
        
        if blanks == word:
            print('you win, word is:',  word)
            break



if __name__ == "__main__":
    main()