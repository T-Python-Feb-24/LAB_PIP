from art import *
from colorama import Fore, Back
Art=text2art("BELIEVE AND ACHEIVE",font='block',chr_ignore=True) 
print(Art)

Art2=text2art("HELLO",font="sub-zero",chr_ignore=True)
print (Art2)

Art3=text2art("Mohammed",font="random",chr_ignore=True)
print(Fore.BLUE+Art3)