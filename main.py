from colorama import Fore as F
import os
import requests
import time


def aboutMe():
    token = input(F.RED + 'Token > ')
    clear()
    bio = input(F.RED + 'O que queres colocar na bio? (separa com virgulas) > ')
    lista = bio.split(',')
    site = 'https://discord.com/api/v9/users/@me'
    while True:
        for a in lista:
            headers = {
                'Authorization': token
            }
            json ={
                'bio': a
            }
            r = requests.patch(site, headers=headers, json=json)
            print(r)
            time.sleep(5)

    
    
def clear():
  if os.name == 'nt':
    os.system('cls')
  else:
    os.system('clear')
    
    
if __name__ == '__main__':
  aboutMe()
