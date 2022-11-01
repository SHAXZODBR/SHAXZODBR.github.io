from cgitb import text

w = input("Enter the text: ")
index = 0
search_char = input("Enter the letter: ")

while (index != len(w)) and (w[index] != search_char):
    index += 1

if index == len(w):
    print("Character not in string")
else:
    print("Character is at position: ", index)