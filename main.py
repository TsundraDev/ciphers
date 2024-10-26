def caesar_cipher(key, plaintext):
    for i, c in enumerate(plaintext):
        # Turn upper character to lower
        if ('A' <= c and c <= 'Z'):
            c = chr(ord(c) - ord('A') + ord('a'))
        # Modify if alphabetical
        if ('a' <= c and c <= 'z'):
            c_num = ord(c) + key
            if (c_num > ord('z')):
                c_num -= 26
            c = chr(c_num)
            plaintext = plaintext[:i] + c + plaintext[i+1:]
        # Modify if numerical
        elif ('0' <= c and c <= '9'):
            c_num = ord(c) + key
            if (c_num > ord('9')):
                c_num -= 10
            c = chr(c_num)
            plaintext = plaintext[:i] + c + plaintext[i+1:]
    return plaintext

# Prepare ciphertext
key = ord('E') - ord('A')
with open("text.plain", 'r') as f:
    plaintext  = f.read()
ciphertext = caesar_cipher(key, plaintext)


# Write text to file
with open("text.cipher", 'w') as f:
    f.write(ciphertext)
