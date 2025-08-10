class SentenceBuilder:
    def __init__(self, sentence):
        self.sentence = sentence
        words = sentence.split(' ')
        self.words = [word for word in words if word.strip() != '']
        self.num_words = len(self.words)
    
    def len(self):
        return self.words.__len__()
    

def main():
    sentence = input('Please input an sentence: ')
    sentenceBuilder = SentenceBuilder(sentence)

    print('The words number is: ', sentenceBuilder.len())

if __name__ == "__main__":
    main()