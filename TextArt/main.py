from art import *
from colorama import Fore,Back

# Print the phrase "BELIEVE AND ACHEIVE" designed with font `block`.
phrase1=text2art('''BELIEVE 
                 AND 
                 ACHEIVE''',font='block',chr_ignore= True)
print(phrase1)

#print the phrase "HELLO" designed with font sub-zero
phrase2=text2art('''HELLO''', font='sub-zero')
print(phrase2)


#bonus
phrase3=text2art("lama","rand")
print(phrase3)
phrase4=text2art("loreen",space=10)
print(phrase4)

print(Fore.GREEN + phrase3)
print(Back.LIGHTYELLOW_EX + "Hi")

