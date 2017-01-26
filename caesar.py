def alphabet_position(letter):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    if letter.isupper():
        position = alphabet2.index(letter)
    else:
        position = alphabet.index(letter)
    return(position)

def rotate_char(char, rot):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    if char.isalpha() == False:
        return char
    elif char in alphabet:
        rotated_index = alphabet_position(char) + rot
        if rotated_index < 26:
             return alphabet[rotated_index]
        else:
            return alphabet[rotated_index % 26]
    elif char in alphabet2:
        rotated_index = alphabet_position(char) + rot
        if rotated_index < 26:
             return alphabet2[rotated_index]
        else:
            return alphabet2[rotated_index % 26]

def encrypt(message, rot):

    encrypted = ''
    for i in message:
        encrypted = encrypted + rotate_char(i, rot)

    return encrypted
