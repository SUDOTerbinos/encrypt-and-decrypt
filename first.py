import random
import string

chars = string.punctuation + string.digits + string.ascii_letters 

chars = list(chars)
key = chars.copy()

random.shuffle(key)

#print(f"chars: {chars}")
#print(f"key  : {key}")

#ENCRYPT
plain_text = input ("Enter your name :")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]


print(f"original name : {plain_text}")
print(f"encrypted message : {cipher_text}")

#DECRYPT
cipher_text = input ("Enter your name :")
plain_text = ""

for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]

print(f"decrypted message : {cipher_text}")
print(f"original name : {plain_text}")
