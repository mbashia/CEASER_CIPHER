# This program can hack messages encrypted
# with the Caesar cipher from Project 6, even
# if you don’t know the key. There are only 26
# possible keys for the Caesar cipher, so a computer
# can easily try all possible decryptions and display the results to the user
# this is a brute force attack
SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print("enter the message you want to decrypt")
message = input(">")
message = message.upper()

for key in range(len(SYMBOLS)):
    translated = ""
    for symbol in message:
        if symbol in SYMBOLS:
            num = SYMBOLS.find(symbol)
            k = (num - key) % 26
            translated += SYMBOLS[k]
        else:
            translated += symbol
    print(f'({key}) {translated}')
