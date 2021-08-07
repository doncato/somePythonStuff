import os,random


def generate_word():
    # Variables
    # Maximum length of the generated word
    maximum_length = 12

    Consonants_combined = ['ch','st','sp','sch',]
    Consonants_single = ['b','c','d','f','g','h','j','k','l','m','n','p','qu','r','t','v','w','x','y','z']
    Consonants = Consonants_combined + Consonants_single
    Vowels = ['a','e','i','o','u','au','ei','ou','ui']
    all_letters = Consonants + Vowels

    word = []
    for i in range(maximum_length):
        if len(word) >= 1:
            if word[-1] in Consonants:
                letter = random.choice(Vowels)
            elif word[-1] in Vowels:
                letter = random.choice(Consonants)
        else:
            letter = random.choice(all_letters)
        word.append(letter)

    result = ''.join(word)
    word_length = random.randint(3,maximum_length)
    return result[:word_length].capitalize()

if __name__ == '__main__':
    count = 0
    while count == 0:
        inp = input("How many words? (1-100'000) >")
        try:
            inp = int(inp)
            if inp >= 1 and inp <= 100_000:
                count = inp
            else:
                raise ValueError
        except:
            print("Invalid input!")

    result = []
    for i in range(count):
        result.append(generate_word())
    with open(os.path.join(os.path.dirname(__file__), 'output.txt'), 'w') as f:
        f.write('\n'.join(result))
