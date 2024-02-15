from art import text2art
from colorama import init, Fore


init(autoreset=True)

print(Fore.MAGENTA + text2art("Be-Yourself", font="epic"))

print(Fore.MAGENTA + text2art("With", font="epic"))

print(Fore.LIGHTBLACK_EX + text2art("TUWAIQ", font="starwars"))

never_give_up_art = text2art("Never-Give-Up", font="starwars")
print(never_give_up_art + Fore.RED + "*")

print(Fore.CYAN + text2art("And-Look-At-Big-Dreem", font="epic"))




