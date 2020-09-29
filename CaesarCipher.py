letterGoodness = [.0817, .0149, .0278, .0425, .1270, .0223, .0202, .0609, .0697, .0015, .0077,
                  .0402, .0241, .0675, .0751, .0193, .0009, .0599, .0633, .0906, .0276, .0098,
                  .0236, .0015, .0197, .0007]

# read input
ciphertext = str(input())
possibleMessages = {}


def decode(ciphertext, key):
    decoded = ''
    for char in ciphertext:
        if char == ' ':
            decoded += char
        else:
            pCode = (ord(char) - 65 + key) % 26
            pChar = chr(pCode + 65)
            decoded += pChar
    return decoded


def goodness(text):
    goodness = 0
    for char in text:
        if char == ' ':
            continue
        else:
            index = ord(char) - 65
            goodness += letterGoodness[index]
    return goodness


# decoding the message with all 26 possible values of the shift S
for i in range(0, 26):
    decoded = decode(ciphertext, i)
    possibleMessages[goodness(decoded)] = decoded

# out of these 26 possible original messages, print the one which has the highest goodness
key = max(possibleMessages, key=float)

print(possibleMessages[key])
