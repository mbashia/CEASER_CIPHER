# The Caesar cipher is an ancient encryption algorithm used by Julius Caesar. It
# encrypts letters by shifting them over by a
# certain number of places in the alphabet. We
# call the length of shift the key. For example, if the
# key is 3, then A becomes D, B becomes E, C becomes
# F, and so on. To decrypt the message, you must shift
# the encrypted letters in the opposite direction. This
# program lets the user encrypt and decrypt messages
# according to this algorithm


SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
while True:
    print("do you want to (e)ncrypt or d(ecrypt)")
    move = input("enter 'e' or 'd':").lower()
    if move.startswith("e"):
        mode = "encrypt"
        break
    if move.startswith("d"):
        mode = "decrypt"
        break
while True:
    maxKey = len(SYMBOLS) - 1
    print("ENTER KEY TO SHIFT....MAXKEY IS ", maxKey)
    key = input(">")
    if not key:
        continue
    elif 0 <= int(key) <= maxKey:
        key = int(key)
        break
print(f"enter message you to {mode}")
message = input(">")
message = message.upper()
translated = ""
for symbol in message:
    if symbol in SYMBOLS:
        num = SYMBOLS.find(symbol)
        if mode == "encrypt":
            k = (num + key) % 26
        elif mode == "decrypt":
            k = (num - key) % 26
        # Handle the wrap-around if num is larger than the length of
        # SYMBOLS or less than 0:
        # if num > maxKey:
        #     num -= maxKey
        # elif num<0:
        #     num +=maxKey

        translated += SYMBOLS[k]
    else:
        translated += symbol

print(translated)
