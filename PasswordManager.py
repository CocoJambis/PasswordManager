import random
import os
import json
import pandas as pd

lista  = []


caratteri = (# Lettere minuscole (26)
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',

    # Lettere maiuscole (26)
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',

    # Numeri (10)
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',

    # Caratteri speciali e simboli (32)
    '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-',
    '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^',
    '_', '`', '{', '|', '}', '~')


def create_password(num):

    password_definitiva = ''

    for i in range(num):
        random_index = random.randint(0, len(caratteri) - 1)
        password = caratteri[random_index]

        password_definitiva += password

    return password_definitiva

def main():

    global lista

    nome_file = 'passwords.csv'

    if os.path.exists(nome_file):
        try:
            df = pd.read_csv(nome_file)
            lista = df.to_dict(orient='records')
            print(lista)
        except json.JSONDecodeError:
            lista = []
    else:
        lista = []

    while True:
        print('Enter WebSite : ')
        choice = input('>')
        print('Enter your username :')
        username = input('>')

        trovato = False

        for elemento in lista:

            if elemento['website'].lower() == choice.lower() and elemento['username'].lower() == username.lower():

                trovato = True

                print(f'{choice} is already in database, are you sure to overwrite it? y/n')
                overwrite = input('>')

                match(overwrite):
                    case 'y':
                        print(f'Updating password and username for {choice}')
                        elemento['password'] = create_password(12)
                        elemento['username'] = username
                        break
                    case 'n':
                        break
                    case _:
                        print('invalid input..')
                        break

        if not trovato:

            password = create_password(12)

            passwords = {
                'website' : choice,
                'username': username,
                'password': password
            }

            lista.append(passwords)

            print(f'Password for {choice} saved successfully')


        df = pd.DataFrame(lista, columns=['website','username','password'])

        df.to_csv(nome_file, index=False)


if __name__ == '__main__':
    main()


