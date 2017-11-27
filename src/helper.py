import numpy as np
import nltk.tokenize

def word(sentence):
    sentence = input("Enter text")
    words = nltk.word_tokenize(sentence)
    print(words)
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
    words[] = text.split(' ')
    for each in words:
        if each not in uniques:
            uniques.append(each)
    print(uniques)
    
    frequency = []
    for i in uniques:
        frequency.append(uniques.count(i))
    print(str(zip(uniques, frequency)))
        
def pairs():
    
    
def dicts():
    uniques = []
    text = input("Enter text")
    words[] = text.split(' ')
    for each in words:
        if each not in uniques:
            uniques.append(each)
    print(uniques)
    dict_key = []
    dict_word = []
    for i in uniques:
        dict_key = [i, uniques[i]]
        dict_word = [uniques[i], i]
        
        print(dict_key)
        print(dict_word)
