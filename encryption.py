# This application allows users to be able to encrypt and decrypt messages.
# Users will only need to choose the option whether they want to encrypt or decrypt (using the same function)
# Only letters are encrypted. Numbers, symbols and spaces are not encrypted
# Users should have the option to choose the number of shifts by which they want to encrypt the characters in their message
# When a message is encrypted by a shift value, you can decode the encrypted message with the same shift value
# Users cannot use a shift value greater than 26 (the number of letters in the alphabet)
# Alternatively we could write the code such that if users enter a shift value over 26, the shift would be the remainder after 
# dividing the value entered by 26. Meaning a shift value of 45 would have the same effect as a shift value of 19 (45 % 26)
# After users encrypt or decrypt a message, the program should ask them whether they have another message to encrypt or decrypt.
# If yes, the program will re-run all over, asking them to enter the new message . . . and so onn. If no, then the program will exit


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e',
            'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


any_more_messages_to_cipher = True

def caesar_code():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    while shift > 26:
        if shift <= 26:
            pass
        else:
            print("The shift cannot be greater than 26")
        shift = int(input("Type the shift number:\n"))
    output = []

    for i in text:
        if i in alphabet:
            if direction == "encode":
                pos = alphabet.index(i) + shift
            else:
                pos = alphabet.index(i) - shift
            i = alphabet[pos]
        else:
            i = i
        output.append(i)
    if direction == "encode":
        print(f" Your encrypted message is {''.join(output)}")
    else:
        print(f" Your decrypted message is {''.join(output)}")

while any_more_messages_to_cipher == True:
    caesar_code()
    proceed = input("Have you any more messages to cipher? Please enter 'yes' or 'no': ").lower()
    if proceed == 'no':
        any_more_messages_to_cipher == False
        print("Thank you for using our cipher application")
        break
