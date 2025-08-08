import random
import string

def randomWord():
    letter = '' 
    for i in range(random.randint(5, 10)):
        letter += random.choice(string.ascii_lowercase)
    
    return letter

def guessGame():
    word = randomWord()
    blanks = blanks = word.__len__() * '_'
    lives = 5

    while True:
        print('please guess the word, one letter each time: ', blanks)
        letter = input()
        if letter.__len__() != 1 or letter == '':
            print('invalid input')
            continue
        if letter in word:
            for i in range(word.__len__()):
                if word[i] == letter:
                    blanks = blanks[:i] + letter + blanks[i+1:]
            print('remain lives:', lives)
        else:
            lives -= 1
            print('remain lives', lives)
        if blanks == word:
            print('you win, word is:',  word)
            break
        if lives <= 0:
            print('you lose, word is:', word)
            break
def main():
    # 这里写主要的程序逻辑
    guessGame()

if __name__ == "__main__":
    main()