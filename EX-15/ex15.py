# from sys import argv

import sys

script, filename = sys.argv

text = open(filename)

print (f"Here is your file {filename}:")

print (text.read())

print ("Type the filename again:")

file_again = input(">")

text_again = open(file_again)

print (text_again.read())