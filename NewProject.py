'''
- Create a virtual environment & activate it
- Use ART package to print Text Art.
- Print the phrase "BELIEVE AND ACHEIVE" designed with font `block`.
- print the phrase "HELLO" designed with font `sub-zero`.
'''

from art import text2art
from colorama import Fore, Back

text2art 
line1 = text2art("BELIEVE AND ACHIEVE", font = "block")
print (Fore.LIGHTBLACK_EX  + line1)


line2 = text2art("HELLO", font = "sub-zero")
print (Fore.CYAN + line2)