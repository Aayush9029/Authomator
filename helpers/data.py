'''
Data class app which parses command line arguments, displays, saves and loads data.
'''
import argparse
import json
from os import getenv, mkdir
from helpers import encryptor_decryptor as ed
from helpers.banner import COLORS as c
from util.test_modules import string_to_bytes

class Data:
    '''
    Main class that handles data parsing, json encoding decoding
    '''

    def __init__(self, key) -> None:
        self.save_path = getenv('HOME') + '/.authomator/data.json'
        self.selected_index = None
        self.encrypted_data = []
        self.decrypted_data = []
        self.key = key
        self.load_json()
        self.decrypt()

    def create_json(self) -> None:
        '''
        Creates a json file using the encrypted data
        '''
        try:
            with open(self.save_path, 'w') as f:
                json.dump(self.encrypted_data, f)
        except FileNotFoundError:
            print(c.RED + 'File not found, crearing ~/.authomator/data.json' + c.END)
            # make folder and file if it doesn't exist
            try:
                mkdir(self.save_path[:self.save_path.rfind('/')])
                with open(self.save_path, 'w') as f:
                    json.dump(self.encrypted_data, f)
            except FileExistsError:
                print('File already exists')
                exit()
            except OSError:
                print('Invalid path')
                exit()


    def load_json(self) -> None:
        '''
        Loads json file and creats a json file if it doesn't exist
        '''
        try:
            with open(self.save_path, 'r') as f:
                self.encrypted_data = json.load(f)
        except FileNotFoundError:
            self.create_json()

        

    def decrypt(self):
        '''
        Decrypts a message
        '''
        self.decrypted_data = []
        for data in self.encrypted_data:
            data = {
                'index': data['index'],
                'username': data['username'],
                'password': ed.decrypt(self.key, data['password']),
            }
            self.decrypted_data.append(data)

    def display_list(self) -> None:
        '''
        Displays username with index
        '''
        if len(self.decrypted_data) == 0:
            print('No passwords found, you need to add some!')
            return
        print('{}'.format(c.PRIMARY + 'List of passwords' + c.END))
        for item in self.decrypted_data:
            # Print username with index and spacing with padding using {0:<10} and .format
            print('{} {:<10s} {} {:<10s} {}'.format(c.SECONDARY, item['index'], c.PRIMARY, item['username'], c.END))
        

    def add_password(self) -> None:
        '''
        Saves all passwords
        '''
        data = {
            'index': str(len(self.encrypted_data)),
            'username': input('Username: '),
            'password': ed.encrypt(self.key, string_to_bytes(input('Password: ').strip())),
        }
        print(f"Adding {data['username']} to the encrypted database")
        self.encrypted_data.append(data)
        self.create_json()

    def delete_password(self) -> None:
        '''
        Deletes a password
        '''
        with open(self.save_path, 'r') as f:
            self.encrypted_data = json.load(f)
        self.decrypt()
        self.display_list()
        self.selected_index = input('Select a password to delete: ')
        # confrims user input and asks for confirmation

        if self.selected_index.isdigit():
            self.selected_index = int(self.selected_index)
            if self.selected_index < len(self.encrypted_data):
                print('Are you sure you want to delete {}? (y/n)'.format(self.decrypted_data[self.selected_index]['username']))
                confirmation = input('> ')
                if confirmation == 'y':
                    del self.encrypted_data[self.selected_index]
                    self.create_json()
                    print('Password deleted')
                self.create_json()
            else:
                print('Invalid index')
        else:
            print('Index must be between 0 and {}'.format(len(self.encrypted_data)))
        
    def edit_password(self) -> None:
        '''
        Edits a password
        '''
        with open(self.save_path, 'r') as f:
            self.encrypted_data = json.load(f)
        self.decrypt()
        self.display_list()
        self.selected_index = input('Select a password to edit: ')
        if self.selected_index.isdigit():
            self.selected_index = int(self.selected_index)
            if self.selected_index < len(self.encrypted_data):
                print('Are you sure you want to edit {}? (y/n)'.format(self.decrypted_data[self.selected_index]['username']))
                confirmation = input('> ')
                if confirmation == 'y':
                    self.encrypted_data[self.selected_index]['password'] = ed.encrypt(self.key, string_to_bytes(input('Password: ').strip()))
                    self.create_json()
                    print('Password edited')
                self.create_json()
            else:
                print('Invalid index')
        else:
            print('Index must be between 0 and {}'.format(len(self.encrypted_data)))

    def display_passwords(self) -> None:
        '''
        Displays all passwords
        '''
        self.load_json()
        self.decrypt()
        self.display_list()
