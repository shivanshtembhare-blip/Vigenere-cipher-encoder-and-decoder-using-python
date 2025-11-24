# Function to Encrypt using the Vigenere cipher.
def vigenere_encrypt(plain_text,key):
   encrypted_text = ''
   # Repeat the key to match the length of the plaintext.
   key_repeated = (key * (len(plain_text) // len(key))) + key[:len(plain_text) % len(key)]
   # Iterate through each character in the plaintext.
   for i in range(len(plain_text)):
       # Check if the character is an alphabet letter.
       if plain_text[i].isalpha():
           # Calculate the shift based on the corresponding key letter.
           shift = ord(key_repeated[i].upper()) - ord('A')
           # Encrypt uppercase and lowercase letters separately.
           if plain_text[i].isupper():
               encrypted_text += chr((ord(plain_text[i]) + shift - ord('A')) % 26 + ord('A'))
           else:
               encrypted_text += chr((ord(plain_text[i]) + shift - ord('a')) % 26 + ord('a'))
       else:
           # If the character is not an alphabet letter, keep it unchanged.
           encrypted_text += plain_text[i]
   # Return the final encrypted text
   return encrypted_text
def vigenere_decrypt(cipher_text,key):
    decrypted_text = ''
    # Repeat the key to match the length of the ciphertext
    key_repeated = (key * (len(cipher_text) // len(key))) + key[:len(cipher_text) % len(key)]
    # Iterate through each character in the ciphertext
    for i in range(len(cipher_text)):
        # Check if the character is an alphabet letter
        if cipher_text[i].isalpha():
            # Calculate the shift based on the corresponding key letter
            shift = ord(key_repeated[i].upper()) - ord('A')
            # Decrypt uppercase and lowercase letters separately
            if cipher_text[i].isupper():
                decrypted_text += chr((ord(cipher_text[i]) - shift - ord('A')) % 26 + ord('A'))
            else:
                decrypted_text += chr((ord(cipher_text[i]) - shift - ord('a')) % 26 + ord('a'))
        else:
            # If the character is not an alphabet letter, keep it unchanged
            decrypted_text += cipher_text[i]
    # Return the final decrypted text
    return decrypted_text
i='y'
while i=='y':
    z=input('do you want to encrypt or decrypt?(e/d):')
    if z=='e' or z=="E":
        x=input("Enter text to encrypt:")
        t=input("Enter key:")
        L=x.split(" ")
        L1=[]
        #print(L)
        for j in L:
            L1.append(vigenere_encrypt(j,t))
        print("Encrypted text:")
        for i in L1:
            print(i,end=" ")
    else:
        c=input("Enter text to decrypt:")
        v=input("Enter key:")
        L=c.split(" ")
        L1=[]
        #print(L)
        for j in L:
            L1.append(vigenere_decrypt(j,v))
        print("Decrypted text:")
        for i in L1:
            print(i,end=" ")
    i=input("\ndo you want to continue(y/n):")
exit()
