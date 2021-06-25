from colorama import Fore as F
import os
import requests


def aboutMe():
    token = input(F.RED + 'Token > ')
    clear()
    bio = input(F.RED + 'O que queres colocar na bio? > ')
    site = 'https://discord.com/api/v9/users/@me'
    headers = {
        'Authorization': token
    }
    json ={
        'bio': bio
    }
    r = requests.patch(site, headers=headers, json=json)
    print(r)
    
    
def clear():
  if os.name == 'nt':
    os.system('cls')
  else:
    os.system('clear')
    
    
if __name__ == '__main__':
  aboutMe()
