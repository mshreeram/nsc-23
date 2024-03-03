def encrypt(text,s):
  result = ""
  for i in range(len(text)):
    char = text[i]
    if (char.isupper()):
      result += chr((ord(char) + s-65) % 26 + 65)
    else:
      result += chr((ord(char) + s - 97) % 26 + 97)
  return result

text = "shreeram"
s = 4
print("plain text: " + text)
print("Shift pattern: " + str(s))
print("Cipher text: " + encrypt(text, s))

message = encrypt(text, s)
message=message.upper()
LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


for key in range(len(LETTERS)):
    translated = ""
    for symbol in message:
        if symbol in LETTERS:
            num = LETTERS.find(symbol) 
            num = num - key
            if num < 0:
                num = num + len(LETTERS)
            
            translated = translated + LETTERS[num]
        else:
            translated = translated + symbol
    print("Key #%s: %s" % (key, translated))