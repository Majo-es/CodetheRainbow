print ("Code the Rainbow 🌈", "\n", "🦄🦄🦄🦄🦄🦄" ,"\n")

def codeRainbow(rainbow):
  if rainbow == "a":
    print("\033[38;5;199m", end="")  # Hot Pink
  elif rainbow == "b":
    print ("\033[34m", end="") #Blue
  elif rainbow == "c":
    print("\033[36m", end="") #Cyan
  elif rainbow == "d":
    print("\x1b[38;5;201m", end="") #Hot Pink 2
  elif rainbow == "e":
    print("\x1b[38;5;213m", end="") #Pink
  elif rainbow == "f":
    print("\x1b[38;5;211m", end="") # Flamingo pink
  elif rainbow == "g":
    print ("\033[32m", end="") #Green
  elif rainbow == "h":
    print("\x1b[38;5;141m", end="") #purplelish
  elif rainbow == "i":
    print("\033[38;5;39m", end="") #Pastel Blue
  elif rainbow == "j":
    print("\x1b[38;5;153m", end="") #Pastel Blue 2
  elif rainbow == "k":
    print("\x1b[38;5;117m", end="") #Pastel cyan
  elif rainbow == "l":
    print("\033[38;5;225m", end="")  # Light Pink
  elif rainbow == "m":
    print("\x1b[38;5;81m", end="") #Pastel blue 3
  elif rainbow == "n":
    print("\x1b[38;5;159m", end="") #Neon blue
  elif rainbow == "o":
    print("\033[38;5;221m", end="") #Light Orange
  elif rainbow == "p":
    print("\033[35m", end="") #Purple
  elif rainbow == "q":
    print("\x1b[38;5;228m", end="") #Pastel Yellow
  elif rainbow == "r":
    print("\033[31m", end="")  # Red
  elif rainbow == "s":
    print("\033[38;5;177m", end="")  # Light Purple
  elif rainbow == "t":
    print("\033[38;5;147m", end="")  # Pastel Purple
  elif rainbow == "u":
    print("\x1b[38;5;90m", end="")  # Wine Purple
  elif rainbow == "v":
    print("\x1b[38;5;183m", end="")  # Violet Purple
  elif rainbow == "w":
    print("\033[0m", end="")  # White
  elif rainbow == "x":
    print("\033[38;5;47m", end="")  # Hot Green
  elif rainbow == "y":
    print("\033[33m", end="")  # Yellow
  elif rainbow == "z":
    print("\x1b[38;5;163m", end="")  # Pink/Red

answer = input("What sentence do you want rainbow-ising?: ")
for letter in answer:
  codeRainbow(letter.lower())
  print(letter, end="")
print()
