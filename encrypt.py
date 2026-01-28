from sys import argv
from Split import Split_para
import random

random.seed()   # Seeds the rng with the system clock

txt_path = "Texts\\" + argv[1] + ".txt"
label_path = "Testing_labels\\" + argv[1] + "_label.txt"
encrypted_path = "Testing_data\\" + argv[1] + "_encrypted.txt"

Split_para(txt_path)    # Splits paragraphs into sentences

label = open(label_path, 'w')   # File containing the correct "answer" for each encrypted sentence
encrypted = open(encrypted_path, 'w')   # File containing encrypted sentences
txt = open(txt_path, 'r', encoding='utf-8')

for l in txt:
    key = random.randint(1, 25)  # The amount which each letter is shifted by e.g. key = 3 means a -> d
    label.write(f"{key}\n")

    line = l.lower()    # Converts everything to lowercase so the maths later is easier 
    ascii_val = []  # Array containing the ASCII values of every character in a sentence
    for c in line:
        ascii_val.append(ord(c))
    for a in ascii_val:
        if a >= 97:  # ASCII value of 'a' is 97, anything less is punctuation or numbers which are not needed
            encrypted.write(chr(97 + ((a - 97 + key) % 26)))
        elif a == 32 or a == 10:   # ASCII value of ' ' is 32 and '\n' is 10; needed for decryption
            encrypted.write(chr(a))

label.close()
encrypted.close()
txt.close()