# Exp 1
## Title: 
Design and Implementation of a product cipher using Substitution and Transposition Ciphers.
### Lab Objective :
This lab provides insight into:
- How different types of Substitution Ciphers and Transposition Ciphers like Hill cipher, Verman cipher, Playfair cipher, Vigenere cipher works and their advantages and disadvantages.

### Reference : 
- "Cryptography and Network Security" Atul Kahate
### Pre-requisite : 
- Any Programming language and Knowledge of Ciphering .

## Solution:
we will use 
- Playfair Cipher
- Double Columnar Transposition
and make a product cipher using the above two.

### Playfair Cipher
Playfair substitution cipher **Rules**
The scheme was invented in 1854 by Charles Wheatstone, but bears the name of Lord Playfair for promoting its use.
In this algorithm, pairs of letters are encrypted, instead of single letters as in the case of simple substitution cipher.
In playfair cipher, initially a key table is created.
The key table is a 5×5 grid of alphabets that acts as the key for encrypting the plaintext.
1. If both letters are the same (or only one letter is left), add an "X" after the first letter. Encrypt the new pair and continue. Some variants of Playfair use "Q" instead of "X", but any uncommon monograph will do.
2. If the letters appear on the same row of your table, replace them with the letters to their immediate right respectively (wrapping around to the left side of the row if a letter in the original pair was on the right side of the row).
3. If the letters appear on the same column of your table, replace them with the letters immediately below respectively (wrapping around to the top side of the column if a letter in the original pair was on the bottom side of the column).
4. If the letters are not on the same row or column, replace them with the letters on the same row respectively but at the other pair of corners of the rectangle defined by the original pair. The order is important – the first letter of the encrypted pair is the one that lies on the same row as the first letter of the plaintext pair.

Example:
https://en.wikipedia.org/w/index.php?title=Playfair_cipher&oldid=675560537

### Double Columnar transposition: 
A single columnar transposition could be attacked by
guessing possible column lengths, writing the message out in its columns (but in the wrong
order, as the key is not yet known), and then looking for possible anagrams. Thus to make it

stronger, a double transposition was often used. This is simply a columnar transposition applied
twice. The same key can be used for both transpositions, or two different keys can be used.
As an example, we can take the result of the irregular columnar transposition in the previous
section, and perform a second encryption with a different keyword, STRIPE, which gives the
permutation "564231"

Example:

5 6 4 2 3 1

E V L N A C

D T E S E A

R O F O D E

E C W I R E

E

This is read off column wise to give the cipher text.
CAEEN SOIAE DRLEF WEDRE EVTOC


So now lets make a menu driven code
