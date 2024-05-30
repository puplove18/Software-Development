```
In this exercise, we want to implement the columnar transposition encryption scheme, a (surprisingly
strong) manually computable cipher. The scheme works as follows.
We first fix a keyword, say EGGSSPAM. This gives two properties, namely the width 8 and an ordering, as
follows. We consider the alphabetical order of the letters, followed by the position within the keyword. So,
A corresponds to index 1, the E to index 2, the first G to 3, the second to 4, etc. Together, the keyword
translates to an index sequence 2 3 4 7 8 6 1 5 .
Now, we want to encrypt a given text, say HELLO FROM PYTHON HOW ARE YOU TODAY. We first remove
all spaces from it, obtaining HELLOFROMPYTHONHOWAREYOUTODAY. (You can also, e.g., replace spaces with
underscores, but keeping them in the cipher text reveals some information, in particular how many words
there are, making it more vulnerable to cryptanalysis.) Then, we arrange the text in rows which are as
wide as the key, i.e.

   E G G S S P A M 
   2 3 4 7 8 6 1 5 
   H E L L O F R O 
   M P Y T H O N H 
   O W A R E Y O U 
   T O D A Y 

Now, we read off the columns in the order given by the indices and concatenate the text. This produces
RNOHM OTEPW OLYAD OHUFO YLTRA OHEY (the text is grouped in words of length 5 for readability).
To decipher it, we again need the keyword and the encrypted text. From the length of text and the
keyword, we can derive the shape of the encryption table. Here, the keyword has length 8 and the
ciphertext has 29, meaning we have 3 full rows and 5 columns in the last row. Thus, we can derive the
“decryption template” as

   E G G S S P A M -- Code
   2 3 4 7 8 6 1 5 -- Indices
   * * * * * * * * 
   * * * * * * * * 
   * * * * * * * * 
   * * * * * 
  
Now, we just insert the cipher text column by column and then read it off row by row, obtaining back the
text HELLOFROMPYTHONHOWAREYOUTODAY.
Your task is to implement this process: Ask for a keyphrase and whether text should be encrypted or
decrypted. In both cases, ask for the text, print the table, and the resulting encrypted or decrypted text.
Observe how the decrypted text changes for slightly different keyphrases, especially if the length changes.
To strengthen the scheme further, observe that you can apply the encryption multiple times, i.e. take the
cipher text and again take it as input.
Also, observe that this encryption does not change the characters themselves, but only their order. We
could furthermore add a substitution cipher (Caesar cipher, Enigma, or something modern), fractionation,
etc. to further improve the encryption.

Below code only encrypts, but decryption follows the same idea.
import collections

phrase = input("Keyphrase: ")
text = input("Text to encrypt: ").replace(" ", "")

def sort_key(x):
  return x[1], x[0]

order = [i for i, _ in sorted(enumerate(phrase), key=sort_key)]

# Storing columns is not really needed, but easier to read
width = len(phrase)
columns = [list() for _ in range(width)]
for i, c in enumerate(text):
  columns[i % width].append(c)

print("Encrypted text: ", end="")
for i in order:
  print("".join(columns[i]), end="")
print()
