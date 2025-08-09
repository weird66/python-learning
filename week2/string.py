import string

class StringManipulator:
    text: str = ''

    # __init__ is a better way to initialize attrs in the instance of class
    def set_init_value(self, word: str):
        self.text = word
    
    def find_character(self, char):
        return self.text.find(char)
    
    def length(self):
        return len(self.text)
    
    def upper_case(self):
        self.text = self.text.upper()
        return self
    
    def lower_case(self):
        self.text = self.text.lower()
        return self


def main():
    text = StringManipulator()
    text.set_init_value('Hello World')
    print(text.find_character('l'))
    print(text.find_character('B'))
    print(text.length())
    print(text.upper_case().text)
    print(text.lower_case().text)

if __name__ == '__main__':
    main()

