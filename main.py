import numpy as np
from random import randint

def make_corpus(path):
    file = open(path, encoding='utf8').read()
    return file.split()


def make_pairs(corpus):
    for i in range(len(corpus)-1):
        yield (corpus[i], corpus[i+1])

def make_word_dict(pairs):
    word_dict = {}

    for word_1, word_2 in pairs:
        if word_1 in word_dict.keys():
            word_dict[word_1].append(word_2)
        else:
            word_dict[word_1] = [word_2]

    return word_dict
        
def generate(corpus, word_dict, amount=60):
    first_word = np.random.choice(corpus)

    while first_word.islower():
        first_word = np.random.choice(corpus)

    chain = [first_word]

    for i in range(amount):
        chain.append(np.random.choice(word_dict[chain[-1]]))

    return ' '.join(chain)

def generate_tyyp_ozlu():
    corpus    = make_corpus('tyyp_ozlu.txt')
    pairs     = make_pairs(corpus) 
    word_dict = make_word_dict(pairs)
    ozlu_soz  = generate(corpus, word_dict, 50)

    return ozlu_soz

def generate_tyyp_siir(line=30):
    corpus    = make_corpus('tyyp_siir.txt')
    pairs     = make_pairs(corpus) 
    word_dict = make_word_dict(pairs)

    siir = [generate(corpus, word_dict, randint(2, 7)) for _ in range(line)]

    return '\n'.join(siir)


print(generate_tyyp_ozlu())
print("\n\n-------------------\n\n")
print(generate_tyyp_siir(20))