import argparse
import getpass
from os import getenv
from pyautogui import typewrite, press
from helpers import data as d
from time import sleep

from util.test_modules import string_to_bytes

# extends the data class
class Authomator(d.Data):
    def __init__(self) -> None:
        self.key = string_to_bytes(getpass.getpass('Enter your key: ').strip())
        super().__init__(self.key)
        self.selected_index = None

    def main(self) -> None:
        '''
        Main function that handles all the logic related to automation
        '''
        args = self.parse_args()
        if args.add:
            self.add_password()
        elif args.edit:
            self.edit_password()
        elif args.delete:
            self.delete_password()
        elif args.list:
            self.display_list()
        else:
            print('Invalid argument')

    def parse_args(self) -> argparse.Namespace:
        '''
        Parses the arguments passed to the script

            Arguments:
                - add
                - edit
                - delete
                - list
        '''
        parser = argparse.ArgumentParser()
        parser.add_argument('-a', '--add', action='store_true',
                            help='Add a new account')
        parser.add_argument('-e', '--edit', action='store_true',
                            help='Edit an existing account')
        parser.add_argument('-d', '--delete', action='store_true',
                            help='Delete an existing account')
        parser.add_argument('-l', '--list', action='store_true',
                            help='List all accounts')
        return parser.parse_args()


    def write_username_pass(self) -> None:
        '''
        Writes the username and password to the screen using pyautogui
        '''
        typewrite(self.data['username'])
        press('tab')
        typewrite(self.data['password'])

    def countdown(self, seconds: int=5) -> None:
        '''
        Counts down from the given seconds
        '''
        print("Auto-logging in in {} seconds".format(seconds))
        for i in range(seconds, 0, -1):
            print(i)
            sleep(1)
    
    

if __name__ == '__main__':
    autho = Authomator()
    autho.main()