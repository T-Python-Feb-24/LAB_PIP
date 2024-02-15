from art import text2art
from colorama import Fore
Art1=text2art("BELIEVE AND ACHEIVE",font="block",chr_ignore=True)
print(Art1)
Art2=text2art("HELLO",font="sub-zero",chr_ignore=True)
print(Art2)

# Bonus
Art3=text2art('''Rayan  Alshehri ''', font="small")
print(Fore.BLUE, Art3)
