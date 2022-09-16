import os, sys, pyperclip, shelve, time
import string, random

class Password:
  
  # This function checks for any duplicate record
  def duplicate_check(self, account):
    self.account = account
    shelfFile = shelve.open('passdata')

    if self.account in shelfFile.keys():
      return True
    else:
      return False


  def input(self):  
    
    # if this file exists it will be opened otherwise it'll be created
    shelfFile = shelve.open('passdata')  
    duplicate = False

    # taking the input for account and it's password
    account = input('Enter account : ')
    account = account.lower()

    # check if the account exists in the records or not
    if self.duplicate_check(account):
      ans = input('Account already exists. Do you want to overwrite it ? (y/n) : ')
      ans = ans.lower()
      if ans == 'y':
        password = input('Enter password : ')
        shelfFile[account] = password
        print('Data successfully entered')
        time.sleep(3)
        shelfFile.close()
        return
      
    # if a duplicate doesn't exist then input password and exit the program
    elif self.duplicate_check(account) == False:
      password = input('Enter password : ')
      shelfFile[account] = password
      print('Data successfully entered')
      time.sleep(3)
      shelfFile.close()
      return

    # storing it into the shelfFile
    print('No data entered')
    shelfFile.close()
    return

  # displays passwords in the main menu
  def dispPass(self):
    shelfFile = shelve.open('passdata')
    i = 1
    for key in shelfFile.keys():
      print(f'{i}) {key}')
      i += 1

    shelfFile.close()
  
  # fetches password from the database
  def retrievePass(self):
    shelfFile = shelve.open('passdata')
    account = input('Enter the account whose password you want : ')
    account = account.lower()

    # checking if account exists or not
    if not self.duplicate_check(account):
      print('No such account found !!!!')
      ans = input('Do you want to store new account ? (y/n) : ')
      ans = ans.lower()
      
      if ans == 'y':
        self.input()
      else:
        shelfFile.close()
        return

    # copying the password to the clipboard
    pyperclip.copy(shelfFile[account])
    print('Password succesfully copied to clipboard !!!')
    time.sleep(3)
    shelfFile.close()
    return


  def deleteRecord(self):
    shelfFile = shelve.open('passdata')
    account = input('Enter the account you want to delete : ')
    account = account.lower()

    if self.duplicate_check(account) == False:
      print("This account doesn't exist !!!!")
      time.sleep(3)
      return
    
    ans = input('Are you sure ? (y/n) : ')
    ans = ans.lower()
    if ans == 'y':
      del shelfFile[account]
      print('Account successfully deleted !!!!')
      time.sleep(3)
    
    shelfFile.close()
    return
  
