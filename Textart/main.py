from art import*
from colorama import Fore
text=(''''BELIEVE AND ACHEIVE''')
art_text=text2art(text,chr_ignore=True)
print(Fore.BLACK,art_text)
text1='''HELLO'''
art_text1=text2art(text1,font="sub-zero",chr_ignore=True)
print(art_text1)


#bonus
Art=text2art('''welcom''',chr_ignore=True) 
print(Fore.YELLOW,Art)
Art=text2art('''jmail''',chr_ignore=True) 
print(Fore.BLUE,Art)