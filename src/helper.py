import numpy as np
import nltk.tokenize

def word(sentence):
    sentence = input("Enter text")
    words = nltk.word_tokenize(sentence)
    print(words)
<<<<<<< Updated upstream
#return words

word(" ")


import nltk.tokenize

def sentence(para):
    para = input("Enter text")
    sentences = nltk.sent_tokenize(para)
    print(sentences)
#return words


def vocab():
    uniques = []
    text = input("Enter text")
    words[] = text.split(' ')
    for each in words:
        if each not in uniques:
            uniques.append(each)
    print(uniques)
    
def pairs():
    uniques = []
    text = input("Enter text")
    words = text.split(' ')
    for each in words:
        if each not in uniques:
            uniques.append(each)
    print(uniques)

    frequency = []
    for i in words:
        frequency.append(words.count(i))
    print(list(zip(words, frequency)))


uniques = []
text = input("Enter text")
words = text.split(' ')
for each in words:
    if each not in uniques:
        uniques.append(each)
print("Text: ", uniques)

sorted_uniques = sorted(list(set(uniques)))
print("Sorted text: ", sorted_uniques)

char_to_int = dict((c, i) for i, c in enumerate(uniques))
print("Words to Integer Mapping: ", char_to_int)

int_to_char = dict((i, c) for i, c in enumerate(uniques))
print("Integer to Words Mapping:", int_to_char)
