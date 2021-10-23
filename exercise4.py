import string
class Alphabet:
    def __init__(self, lang, letters):
        self.lang = lang
        self.letters = letters
    
    def prinnt(self):
        print(self.letters)

    @property
    def letters_num(self):
        return len(self.letters)

class EngALphabet(Alphabet):
    __letters_num = 26

    def __init__(self):
        super().__init__('En', list(string.ascii_uppercase))
    
    @property
    def _letters_num(self):
        return EngALphabet.__letters_num

    def is_en_letters(self, let):
        return let in self.letters

    @staticmethod
    def example():
        return 'Have a good lunch'

def main():
    word = EngALphabet()
    word.prinnt()
    word.letters_num
    word.is_en_letters("G")
    word.is_en_letters("П")
    print("English Example:")
    EngALphabet.example()
    
if __name__ == "__main__":
    main()