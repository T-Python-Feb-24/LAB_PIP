# Import the 'art' module which is used to creat ASCII art
import art

# Import the 'Fore' class from the 'colorama' module which is used to change the color of the output
from colorama import Fore
# Print the string "BELIEVE ACHEIVE" green color using the 'block' font of the 'art' module
print(Fore.GREEN + art.text2art("BELIEVE AND ACHEIVE", font="block"))

# Print the string "HELLO" in cyan color using the 'sub-zero' font of the 'art' module
print(Fore.CYAN + art.text2art("HELLO", "sub-zero"))

# Print the string "WISSAM" in red color using the 'dotmatrix' font of the 'art' module
print(Fore.RED + art.text2art("WISSAM", "dotmatrix"))
