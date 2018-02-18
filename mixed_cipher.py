###Abygail Stiekman###
########aes15d########


from __future__ import print_function
import sys
import string

def test(kw):
    return [x for i, x in enumerate(kw) if i is kw.index(x)]

#if letter is lowercase
low_alph = [x for x in string.ascii_lowercase]

#opens first command line arg
with open( sys.argv[1], 'r' ) as file:
    chars = [char for line in file for char in line]

#takes user input and sets it to ciphertext list
kw = test([x for x in raw_input('Please enter a keyword for the mixed cipher: ')])

# takes input from command line file, prints depending on if word in file is
#uppercase or lowercase
cipher_alpha = test( kw + low_alph )
ciphered_file = []
for char in chars:
    if char.islower():
        ciphered_file.append( cipher_alpha[ low_alph.index(char) ] )
    elif char.isupper():
        ciphered_file.append( cipher_alpha[ low_alph.index( char.lower() ) ].upper() )
    else:
        ciphered_file.append(char)


#prints plaintext
print('Plaintext:   ', end='') #stops when you reach the end of the list
print(('').join(low_alph))
print('Ciphertext:  ', end='') #prints ciphered text
print(('').join(cipher_alpha))
print(('').join(ciphered_file)) #prints ciphered words in file
