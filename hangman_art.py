import colorama
from colorama import init, Fore
colorama.init(autoreset=True)

hangman_pics = [
    Fore.GREEN +
    '''
      +---+
      |   |
          |
          |
          |
          |
    =========''',
    Fore.GREEN +
    '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''',
    Fore.GREEN +
    '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''',
    Fore.GREEN +
    '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''',
    Fore.RED +
    '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''',
    Fore.RED +
    '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''',
    Fore.RED +
    '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''',
    Fore.RED +
    '''
      +---+
      |   |
      x   |
     /|\  |
     / \  |
          |
    =========''']

hangman_win = (
    Fore.CYAN +
    '''
      +---+
      |   |
          |
     \o/  |
      |   |
     / \  |
    =========''')
