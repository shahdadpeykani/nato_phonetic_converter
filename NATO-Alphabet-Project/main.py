import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dic = {row.letter: row.code for (index, row) in data.iterrows()}


def generate_phonetic():

    word = input("Enter a word: ").upper()

    try:
        output = [phonetic_dic[letter] for letter in word]

    except KeyError:
        print("Sorry, only letters in alphabet please.")
        generate_phonetic()
    else:
        print(output)


generate_phonetic()
