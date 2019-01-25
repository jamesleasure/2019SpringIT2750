## IT 2750 - Lab 3

*Use Chapter 3 to complete this lab.*

1. Create a folder in your repository called Lab3.
2. In the Lab 3 folder add a file called README.md. Note: create all of the following files in the lab 3 folder.
3. In your README.md file, describe - in a few sentences - what we've covered in lesson 3. 
4. Again, in README.md, answer the following questions:
  1. List and describe 3 basic string methods.
  2. Describe the 3 simple algorithms for encryption that we covered in this lesson (it can be in 2 or 3 sentences.
  3. Identify the type of encryption the following algorithm is implementing:
  ```
def encrypt(plainText ,key):  
    alphabet = "abcdefghijklmnopqrstuvwxyz"  
    plainText = plainText.lower ()  
    cipherText = ""  
  
    for ch in plainText:  
        idx = alphabet.find(ch)  
        cipherText = cipherText + key[idx]  
    return cipherText  
  ```
  4. Identify the type of encryption the following algorith is implementing:
  ```
  def scramble2Encrypt(plainText):  
    evenChars = ""  
    oddChars = ""  
    charCount = 0  
  
    for ch in plainText:  
        if charCount % 2 == 0:  
            evenChars = evenChars + ch  
        else:  
            oddChars = oddChars + ch  
      charCount = charCount + 1  
    cipherText = oddChars + evenChars  
    return cipherText  
  ```
  5. Create a file called myCrypto.py. Implement one of the encryption algorithms using these files. Make sure you add comments indicating the type of encryption algorithm used. You should have a method called encrypt and a method called decrypt at the minimum in this file. 
  6. Create a file called testCrypto.py. In testCrypto.py, test (and output the results) of both encrypt and decrypt 3 times.
