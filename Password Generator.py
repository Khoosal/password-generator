import random
import os

def clear():
  os.system('cls')

# example file path below
#pf = 'C:\\Users\\ENTER USER NAME\\Desktop\\Coding FILES\\pw.txt'

# text formats
bold = '\033[1m' # bold text
cF = '\033[0m' # clear formatting

special_characters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '[', ']', '<', '>', '/', '?', ';', ':', '~', '`']
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
num = 1
valid_answers = ['Y', 'N']

def clearFile():
  with open(pf, 'w') as file:
    file.truncate(0)

clear()
clearFile()

length = input("Length of password (Integer): ")
if length == "":
    length = 1
else:
    while not length.isdigit() or int(length) <= 0:
      print("\nPlease enter an integer greater than 0.")
      length = input("Length of password (Integer): ")
    print()

amount_of_passwords = input("How many passwords to generate (Integer): ")
if amount_of_passwords == "":
  amount_of_passwords = 1
else:
  while not amount_of_passwords.isdigit() or int(amount_of_passwords) <= 0:
    print("\nPlease enter an integer greater than 0.")
    amount_of_passwords = input("Length of password (Integer): ")

characters = input("\nInclude special characters (Y/N)? ").upper()
while characters not in valid_answers:
  print("\nPlease enter 'Y' or 'N'")
  characters = input("Include special characters (Y/N)? ").upper()
print()

numbers = input("\nInclude numbers (Y/N)? ").upper()
while numbers not in valid_answers:
  print("\nPlease enter 'Y' or 'N'")
  numbers = input("Include numbers (Y/N)? ").upper()

length = int(length) # turn variable into an integer for future use
amount_of_passwords = int(amount_of_passwords) # turn variable into integer for future use

print()
generating_password = None
passwords_list = []

def appendToList(generating_password):
  passwords_list.append(generating_password) # add the password to the file

if characters == 'N' and numbers == "N":
  for k in range(amount_of_passwords):
    for i in range(length):
      randLetter = random.randint(0,51) # choose a random letter from the alphabet (list)
      generating_password = letters[randLetter] # put the letter in the variable
      with open (pf, 'r+') as file:
        line = file.readline()
      editedLine = line.strip() + str(generating_password)
      with open (pf, 'r+') as file:
        file.write(editedLine + "\n")
    with open (pf, 'r') as file:
      line = file.readline()
      appendToList(line)
    clearFile()  
else:
  if characters == "Y":
    if numbers == "Y":
      for k in range(amount_of_passwords):
        for i in range(length):
          character = random.randint(1,3) # 1 means letter, 2 means special character, 3 means numbers
          if character == 1: # letter
            randLetter = random.randint(0,51) # choose a random letter from the alphabet (list)
            generating_password = letters[randLetter] # put the letter in the variable
            with open (pf, 'r+') as file:
              line = file.readline()
            editedLine = line.strip() + str(generating_password)
            with open (pf, 'r+') as file:
              file.write(editedLine + "\n")

          if character == 2: # special character
            randSpecCharacter = random.randint(0, 23) # random special character from the list
            generating_password = special_characters[randSpecCharacter] # put the special character in the variable
            with open (pf, 'r+') as file:
              line = file.readline()
              editedLine = line.strip() + str(generating_password)
            with open (pf, 'r+') as file:
              file.write(editedLine + "\n")

          if character == 3: # number
            randNum = random.randint(0,8)
            generating_password = numbers_list[randNum]
            with open(pf, 'r+') as file:
              line = file.readline()
              editedLine = line.strip() + str(generating_password)
            with open (pf, 'r+') as file:
              file.write(editedLine + "\n")
            
        with open (pf, 'r') as file:
          line = file.readline()
          appendToList(line)
        clearFile()  
    else:
      for k in range(amount_of_passwords):
        for i in range(length):
          character = random.randint(1,2) # 1 means letter, 2 means special character
          if character == 1: # letter
            randLetter = random.randint(0,51) # choose a random letter from the alphabet (list)
            generating_password = letters[randLetter] # put the letter in the variable
            with open (pf, 'r+') as file:
              line = file.readline()
            editedLine = line.strip() + str(generating_password)
            with open (pf, 'r+') as file:
              file.write(editedLine + "\n")
          else:
            randSpecCharacter = random.randint(0, 23) # random special character from the list
            generating_password = special_characters[randSpecCharacter] # put the special character in the variable
            with open (pf, 'r+') as file:
              line = file.readline()
              editedLine = line.strip() + str(generating_password)
            with open (pf, 'r+') as file:
              file.write(editedLine + "\n")
        with open (pf, 'r') as file:
          line = file.readline()
          appendToList(line)
        clearFile()
      
  else:
    for k in range(amount_of_passwords):
      for i in range(length):
        character = random.randint(1,2)
        if character == 1:
          randLetter = random.randint(0,51) # choose a random letter from the alphabet (list)
          generating_password = letters[randLetter] # put the letter in the variable
          with open (pf, 'r+') as file:
            line = file.readline()
          editedLine = line.strip() + str(generating_password) # add the letter to the file
          with open (pf, 'r+') as file:
            file.write(editedLine + "\n")
        else:
          randNum = random.randint(0,8)
          generating_password = numbers_list[randNum]
          with open(pf, 'r+') as file:
            line = file.readline()
          editedLine = line.strip() + str(generating_password)
          with open(pf, 'r+') as file:
            file.write(editedLine + "\n")
      
      with open (pf, 'r') as file: # once the
        line = file.readline()
        appendToList(line) # once all letters have been added to the file, the password is placed in the array; that is one password done
      clearFile() # clear the file, ready for the next password to be generated



clear()
print(f"""{bold}Constraints{cF}:
Length of password: {length}
Amount of passwords generated: {amount_of_passwords}
Special characters: {characters}
Numbers included: {numbers}

{bold}PASSWORDS GENERATED:{cF}\n""")
fixedList = [s.strip() for s in passwords_list] # output the list without the brackets
for item in fixedList:
  print(f"{bold}Password{cF} {num}: {item}")

  num += 1
