#from the module sys import argv into the current name context.
#If you wrote import sys then you would have all things in sys available
from sys import argv

#script and filename are passed as arguments
script, filename = argv

#assign txt to open the file name
txt = open(filename)

#print on the screen that here's your file
print(f"Here's your file {filename}:")

#open the file and read it
print(txt.read())

#print on the screen to type the file name again
print("Type the filename again:")

#assign file_again a string input of > to show on the screen
file_again = input("> ")

#assign txt_again to open and display the input sign
txt_again = open(file_again)

#display on the screen the contents of the file
print(txt_again.read())
