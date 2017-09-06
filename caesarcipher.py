import string
import sys

messageSpace = list(string.ascii_lowercase)


def getCharIndex(char):
  for i in range(0,len(messageSpace)):
    if char == messageSpace[i]:
      return i
  return "ERR!"



def caesar(plaintext, key):
  cipher = ""
  for char in plaintext:
    plaintextCharIndex = getCharIndex(char)
    if plaintextCharIndex == "ERR!":
      return "Error in plaintext: illegal character"
    else:
      if (sys.argv[3] == "e"):

        if ((len(messageSpace)-1) - plaintextCharIndex) < key:
          cipher = cipher + messageSpace[(key - (len(messageSpace) - plaintextCharIndex))]
        else:
          cipher = cipher + messageSpace[plaintextCharIndex + key]
    
      if (sys.argv[3] == "d"):
        if plaintextCharIndex < key:
          cipher = cipher + messageSpace[len(messageSpace) - (key -plaintextCharIndex)]
        else:
          cipher = cipher + messageSpace[plaintextCharIndex - key]

  return cipher

print(caesar(sys.argv[1], int(sys.argv[2])))


