from art import *
from colorama import Back, Fore

lab_string:str = 'BELIEVE AND ACHEIVE'
lab_string2:str = 'HELLO'

lab_bonus_phrase:str = 'Im Hammam'
lab_bonus_phrase2:str = 'Tuwaiq Camp'
lab_bonus_phrase3:str = 'I Love Python'
tprint(lab_string,font="block",chr_ignore=True)
tprint(lab_string2, font='sub-zero',chr_ignore=True)
#for the bonus
tprint(lab_bonus_phrase, font='rand')
print(Fore.CYAN + lab_bonus_phrase)
print(Fore.MAGENTA + lab_bonus_phrase2)
print(Fore.GREEN + lab_bonus_phrase3)