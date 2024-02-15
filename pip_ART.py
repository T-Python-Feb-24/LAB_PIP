from art import *

tprint("Text ART")

tprint("BELIEVE", font='block', chr_ignore=True)
tprint("AND", font='block', chr_ignore=True)
tprint("ACHEIVE", font='block', chr_ignore=True)

tprint("HELLO", font='sub-zero', chr_ignore=True)

tprint("HAPPY HOLIDAY", font="rnd-medium")
tprint("HAPPY", font="rnd-xlarge")
tprint("Ring","mix")
tprint("HI", font="large")


from colorama import Fore, Back, Style

print(Fore.LIGHTGREEN_EX + Back.RED + Style.BRIGHT + "Hello")