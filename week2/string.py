import string

class StringManipulator:
    def __init__(self, text):
        self.text = text

    def find_character(self, char):
        return self.text.find(char)
    
    def length(self):
        return len(self.text)
    
    def upper_case(self):
        return StringManipulator(self.text.upper())
    
    def lower_case(self):
        return StringManipulator(self.text.lower())


def main():
    text = StringManipulator('aBc')
    print(text.find_character('b'))
    print(text.find_character('B'))
    print(text.length())
    print(text.upper_case().text)
    print(text.lower_case().text)

if __name__ == '__main__':
    main()

