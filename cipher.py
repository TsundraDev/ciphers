import sys

def caesar_cipher(key, plaintext):
    for i, c in enumerate(plaintext):
        # Turn upper character to lower
        if ('A' <= c and c <= 'Z'):
            c = chr(ord(c) - ord('A') + ord('a'))
        # Modify if alphabetical
        if ('a' <= c and c <= 'z'):
            c_num = ord(c) + key
            while (c_num > ord('z')):
                c_num -= 26
            c = chr(c_num)
            plaintext = plaintext[:i] + c + plaintext[i+1:]
        # Modify if numerical
        elif ('0' <= c and c <= '9'):
            c_num = ord(c) + key
            while (c_num > ord('9')):
                c_num -= 10
            c = chr(c_num)
            plaintext = plaintext[:i] + c + plaintext[i+1:]
    return plaintext

# Check cmd-line arguments
if (len(sys.argv) != 4):
    print("Usage: python3 cipher.py [key] [plaintext-file] [ciphertext-file]")
key = ord(sys.argv[1]) - ord('A')
plaintext_filename  = sys.argv[2]
ciphertext_filename = sys.argv[3]

# Prepare ciphertext
with open(plaintext_filename, 'r') as f:
    plaintext  = f.read()
ciphertext = caesar_cipher(key, plaintext)

# Write text to file
with open(ciphertext_filename, 'w') as f:
    f.write(ciphertext)
