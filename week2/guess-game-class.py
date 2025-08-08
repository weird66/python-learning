import random
import string

def randomWord():
    letter = '' 
    for i in range(random.randint(5, 5)):
        letter += random.choice(string.ascii_lowercase)
    return letter

class Gamer():
    def __init__(self, word):
        self.word = word
        self.userInput = []
        self.blanks = '_' * word.__len__()
        self.lives = 5
    
    def isInputed(self, letter):
        if letter in self.userInput:
            return True
    
    def handleInput(self, letter):
        if letter.__len__() != 1 or letter == '':
            print('invalid input')
            return
        if self.isInputed(letter):
            print('You have already input this letter before!')
            return
        if letter in self.word:
            for i in range(self.word.__len__()):
                if self.word[i] == letter:
                    self.blanks = self.blanks[:i] + letter + self.blanks[i+1:]
            print('remain lives:', self.lives)
        else:
            self.lives -= 1
            print('remain lives', self.lives)
        self.userInput.append(letter)

    def start(self):
        while True:
            print('please guess the word, one letter each time: ', self.blanks)
            letter = input()
            self.handleInput(letter)

            if self.blanks == self.word:
                print('you win, word is:',  self.word)
                break
            if self.lives <= 0:
                print('you lose, word is:', self.word)
                break

def main():
    gamer = Gamer(randomWord())
    gamer.start()

if __name__ == "__main__":
   
    # main()
    main()