'''
Contains banner for the application.
'''

class COLORS:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    LINK = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    PRIMARY = '\033[97m'
    SECONDARY = '\033[90m'
    END = '\033[0m'
    PINK = '\033[95m'


banner = f"""
{COLORS.GREEN}
          ___  __             ___  __   __  
 /\  |  |  |  /  \  |\/|  /\   |  /  \ |__) 
/~~\ \__/  |  \__/  |  | /~~\  |  \__/ |  \ 
{COLORS.PINK}
                              - Made with <3       

{COLORS.SECONDARY}Find out more at:{COLORS.LINK} github.com/Aayush9029/Authomator{COLORS.END}
"""


def print_banner():
    '''
    Function to print the banner.
    '''
    print(banner)


if __name__ == '__main__':
    print_banner()