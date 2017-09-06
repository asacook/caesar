import string
import sys

messageSpace = list(string.ascii_lowercase)


def getCharIndex(char):
  for i in range(0,len(messageSpace)):
    if char == messageSpace[i]:
      return i
  return "ERR!"



def encryptcaesar(plaintext, key):
  cipher = ""
  for char in plaintext:
    plaintextCharIndex = getCharIndex(char)
    if plaintextCharIndex == "ERR!":
      return "Error in plaintext: illegal character"
    else:
      if (len(messageSpace) - plaintextCharIndex) < key:
        cipher = cipher + messageSpace[(key - (len(messageSpace) - plaintextCharIndex))]
      else:
        cipher = cipher + messageSpace[plaintextCharIndex + key]
    
  return cipher



def decryptcaesar(cipher, key):
  plaintext = ""
  for char in cipher:
    plaintextCharIndex = getCharIndex(char)
    if plaintextCharIndex == "ERR!":
      return "Error in plaintext: illegal character"
    else:
      if plaintextCharIndex < key:
        plaintext = plaintext + messageSpace[len(messageSpace) - (key -plaintextCharIndex)]
      else:
        plaintext = plaintext + messageSpace[plaintextCharIndex - key]
    
  return plaintext



if (sys.argv[3] == "e"):
  print(encryptcaesar(sys.argv[1], int(sys.argv[2])))

if (sys.argv[3] == "d"):
  print(decryptcaesar(sys.argv[1], int(sys.argv[2])))

