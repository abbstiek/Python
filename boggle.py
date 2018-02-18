#--Abygail Stiekman--#
#-----boggle.py------#
#-----05/24/2017-----#
#------CIS 4930------#
#-------aes15d-------#

import random
import string
import enchant
import math

letters = [] #empty to be filled with random letts from the alphabet

# draws a 4x4 grid, uses randomLetters to fill 16 characters
def drawBoard (randomLetters):
    print " \n [%s] [%s] [%s] [%s]\n " %(randomLetters [0], randomLetters [1], randomLetters [2], randomLetters [3])
    print " [%s] [%s] [%s] [%s]\n " %(randomLetters [4], randomLetters [5], randomLetters [6], randomLetters [7])
    print " [%s] [%s] [%s] [%s]\n " %(randomLetters [8], randomLetters [9], randomLetters [10], randomLetters [11])
    print " [%s] [%s] [%s] [%s]\n " %(randomLetters [12], randomLetters [13], randomLetters [14], randomLetters [15])

def randomLetters ():
        alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Qu','R','S','T','U', 'V','W','X','Y','Z']
        for i in range (0,16,1): #fills grid with random letters
                letters.append(random.choice(alphabet))
        return letters #returns grid with random letters

def word_inp ():
        wordcount = 0 # iterates with each word added
        score = 0 #score per word
        d = enchant.Dict("en_US")  #sets for enchant dictionary
        score_total = 0 #keeps track of total score
        wordlist = [] # to be filled with user inputted words
        print("Start typing your words! (Press enter after each word and enter 'X' when done): \n")
        word_input = raw_input() #sets word that is inputted and adds it to list wordlist
        while not (word_input == "X" or word_input == "x"): #will stop when user enters X
                word_input = raw_input()
                wordlist.append(word_input)
                wordcount += 1 #used to keep track of how many times for loop is iterated
        for word_input in wordlist:
                del wordlist[-1]
                if len(word_input)<3: #doesn't score if word is too short
                        print ('the word %s it too short.'%(word_input))
                elif d.check(word_input) == True:
                        wordLength = len(word_input) #checks length of word to return score
                        if wordLength < 3:
                                score = 0
                        elif wordLength == 3:
                                score = 1
                        elif wordLength == 4:
                                score = 1
                        elif wordLength == 5:
                                score = 2
                        elif wordLength == 6:
                                        score = 3
                        elif wordLength == 7:
                                score = 5
                        else:
                                score = 11
                        print ('the word %s is worth %d points.'%(word_input, score))
                        score_total+=score #keeps count of score, updates with each word
                else:
                        print ('the word %s is ... not a word.'%(word_input)) #if word is not found in dictionary
             print("Your total score is %d points!" %(score_total)) #prints total score

def wordInBoardIter(let, word, x, y):
    n = int(len(letters)**0.5)
    if word == "": return True # empty - all letters are found
    if x<0 or y<0 or x>=n or y>= n: return False #outside of board
    if let[x+y*n] != word[0]: return False # we are looking at the wrong position
    #one step further:
    return any(wordInBoardIter(let, word[1:], x+dx,y+dy) for dx,dy in [(1,0), (0,1), (-1,0), (0,-1)])


def wordInBoard(let, word):
    n = int(len(let)**0.5)
    return any(any(wordInBoardIter(let, word, x,y) for x in range(n)) for y in range(n))


if __name__ == '__main__':
        drawBoard(randomLetters())
        word_inp()