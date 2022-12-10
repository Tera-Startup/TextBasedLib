# Devs : @NaolNinja, @PancakeDev

import platform # To detect the platform
from os import system as cmd # To create terminal commands
import sys, time, colorama, pickle
# To get the time + typewrite text + colors in the terminal + saving data

colorama.init() # Initializes colorama
dialogspath = "dialogs.txt" # Opens the default file for dialogs
dialogs = open(dialogspath, "r").read() # Reads it
dialogs = dialogs.splitlines() # Makes the lines of the dialogs file a list

colors = { # Quicker way to add color in the terminal
  "red": colorama.Fore.RED,
  "green": colorama.Fore.GREEN,
  "yellow": colorama.Fore.YELLOW,
  "blue": colorama.Fore.BLUE,
  "default": colorama.Style.RESET_ALL,
  "bright": colorama.Style.BRIGHT 
}
# Once this buffer is filled with data, you can reassign variables
save_sentence = "Saved data successfully!" # Sentence to say when data is saved
# You can change it if you need it in another language

def w(seconds): # Equivalent of time.sleep(), but easier to access
  time.sleep(seconds)

def clear(): # Polyvalent console clearer
  ostype = platform.system()
  if ostype == "Linux" or ostype == "Darwin":
    cmd("clear")
  else:
    cmd("cls")

def quit(): # Basic quit function
  c = inp("Are you sure you want to quit ?\ny/n")
  if c == "y":
    quit()
  else:
    pass
def inp(prompt): # Quicker complete input
  userchoice = input(f"{prompt}\n> ")
  return userchoice

def pe(): # "Press enter" basic function
  input("Press Enter to continue./")

def pev(verb): # "Press enter" basic function with the possibilty to change the verb
  input(f"Press Enter to {verb}./")

def tw(text): # Typewrites text (by @NaolNinja on replit)
  for char in text:
    sys.stdout.write(char)
    sys.stdout.flush()
    w(0.065)
  print("")

def setDialogs(path): # To get a different dialogs set if needed
  global dialogspath
  global dialogs
  dialogspath = path
  dialogs = open(dialogspath, "r").read()
  dialogs = dialogs.splitlines()

def passage(text, options, functions, typewrite): # Passage function
  while True:
    clear()
    if typewrite:
      tw(text)
    else:
      print(text)
    print("")
    for i in range(0, len(options)):
      print(f"{i+1} : {options[i]}")
    userchoice = input("> ")
    if int(userchoice) <= len(options+1):
      f = functions[(int(userchoice) - 1)]
      break
    else:
      print("Please enter a choice")
      pe()
  eval(f)

def save(data, filename): # Complete saving system
  with open(filename, "wb") as pickle_file:
    pickle.dump(data, pickle_file)
  print(save_sentence)
  pe()
  
def getSavedData(filename): # Returns data from a saved file
  with open(filename, "rb") as pickle_file:
    data = pickle.load(pickle_file)
  return data