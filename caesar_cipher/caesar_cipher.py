import nltk
nltk.download('words')
from nltk.corpus import words
word_list = words.words()
import random

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(words, key):
    encrypted_words = ''

    for char in words.lower():
        if char in alphabet:
            encrypted_letter = alphabet[(alphabet.index(char.lower()) + key) % len(alphabet)]
            encrypted_words += encrypted_letter
        else:
            encrypted_words += char
    return encrypted_words    

def decrypt(words):

    def english_words(list_of_words):
        number_correct = 0
        for word in list_of_words:
            if word in word_list:
                number_correct += 1
        if number_correct/len(list_of_words) >= 0.5:
            return True
        return False

    for key in range(len(alphabet)):    
        a = encrypt(words, (-1*(key)))
        b = english_words(a.split(' '))
        if b:
            return a

if __name__ == "__main__":
    # string_2 = "Relationships. Passion. Commitment. For Foushée, every client relationship is a long term commitment. We go beyond contractual obligations to help you succeed with your construction project. The difference since 1977: dedication and creative solutions. Our clients are many and diverse. Most of our volume is from repeat clients with needs from new construction to renovation. Taking care of your construction needs while you take care of your business."
    # string = "“I hope that in this year to come, you make mistakes. Because if you are making mistakes, then you are making new things, trying new things, learning, living, pushing yourself, changing yourself, changing your world. You’re doing things you’ve never done before, and more importantly, you’re doing something.”"
    # encrypted_string = encrypt(string, random.randint(1, len(alphabet)))
    # decrypted_string = decrypt(encrypted_string)
    # print('original string: ', string)
    print('')
    # print('encrypted: \n', encrypted_string)
    # print('decrypted: ', decrypted_string)