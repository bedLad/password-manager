import password, os, sys, pyperclip, shelve

p = password.Password()

while True:
  print(' ###### Welcome to your password manager ######')
  print('\n Following passwords exist in the record :-\n')
  p.dispPass()

  print('\nWhat do you want to do ? ')
  print('1) Input Data.   2) Retrieve Password.   3) Delete Data.   4) Exit program')
  ans = int(input('Please enter number corresponding to the option : '))
  
  if ans == 1:
    p.input()
  elif ans == 2:
    p.retrievePass()
  elif ans == 3:
    p.deleteRecord()  
  elif ans == 4:
    exit()
