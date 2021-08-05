import ctypes
from os import system, name

#Routine: configure this terminal
if name == 'nt':
    # Enable Virtual Terminal Processing for terminals on Windows that do not support it by default
    kernel32 = ctypes.windll.kernel32
    kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 5)
    # -11 refers to the the standard output device. 5 is the result of bitwise OR operations on the modes we want enabled (0x0001, 0x0004) on this terminal for the execution of this program
    # See References section of the Readme.md for more information
else:
    print("\033[?7l") # xterm control sequence to disable Auto-Wraparound

print("\nAscii Mountains\n")

print("Pre-flight check list:")
print("[*] Please ensure the terminal is running in Full-Screen mode")
print("[*] Please ensure this terminal supports VT100/XTerm/ANSI control sequences (xterm for Linux, Windows Terminal, etc)")
#TODO: validate these requirements on current terminal session


userInput = input("\nEnter input digits separated by space: ")
if userInput.strip():
    numList = userInput.split()
    numList = [int(i) for i in numList]
else:
    exit("\n[!] Empty input")
#TODO: implement input validation
print("[#] OK. Please enjoy these mountains")

guy = "<   >\033[1A\033[5D/ | \\\033[1A\033[5D  o" # This is the guy atop the mountain, represented in-line using an ANSI escape sequence


#Routine: find the mountain-peak position and value from the user input
# Flip variable operates in accordance to a pattern in the user input, where escalation is followed by a de-escalation in a flip-flop manner
flip = True
intmod = 0
height = []

for i in numList:
    if flip==True:
        intmod += i
        height.append(intmod)
        flip = False

    elif flip==False:
        intmod -= i
        height.append(intmod)
        flip = True

print("\n" * (max(height)+6) , end="") # Print the necessary amount of padding space required for the mountains



#Routine: start drawing the mountains
# Note the following ANSI escape sequences used in this routine, and their functions:
# " \033[1A " moves the cursor position up one line
# " \033[1B " moves the cursor position down one line
# " \033[1D " moves the cursor position one character to the left
# " \033[s " saves the current cursor position
# " \033[u " loads and restores to the saved cursor position
# " \033[E " Goes to the beginning of next line

flip=True

for idx, i in enumerate(numList):
    if flip==True:
        print("/\033[1A" * int(i-1) + "/", end="") # Draw the escalating mountain slashes
        flip=False
        if idx==height.index(max(height)): # We have reached the peak, guy goes here
            print("\033[1A\033[s"+ guy +"\033[u\033[1B     ", end="")

    elif flip==False:
        print("\\\033[1B" * int(i-1) + "\\", end="") # Draw the de-escalating mountain slashes
        flip=True



# Stall the app to prevent shell prompt from overwriting any mountains
input("\033[E\033[99B Press the Enter key to clear screen and exit.")


# cleanup
system('cls') if name == 'nt' else system('clear')
