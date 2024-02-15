from art import text2art
from colorama import Fore, Back

line1 = text2art("BELIEVE AND ACHEIVE", font='block')
print(line1)


line2 = text2art("HELLO", font='sub-zero')
print(line2)

########################################
line3=text2art("this text in blue color",font='smallcaps')
print(Fore.BLUE + line3)