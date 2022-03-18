import colorama
from colorama import Fore
colorama.init(autoreset=True)

hangman_logo = ['''
╭╮╱╭╮╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭━━━━┳╮╱╱╱╱╱╭━━━╮
┃┃╱┃┃╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱┃╭╮╭╮┃┃╱╱╱╱╱┃╭━╮┃
┃╰━╯┣━━┳━╮╭━━┳╮╭┳━━┳━╮╱╱╱╱╱╰╯┃┃╰┫╰━┳━━╮┃┃╱╰╋━━┳╮╭┳━━╮
┃╭━╮┃╭╮┃╭╮┫╭╮┃╰╯┃╭╮┃╭╮╮╭━━╮╱╱┃┃╱┃╭╮┃┃━┫┃┃╭━┫╭╮┃╰╯┃┃━┫
┃┃╱┃┃╭╮┃┃┃┃╰╯┃┃┃┃╭╮┃┃┃┃╰━━╯╱╱┃┃╱┃┃┃┃┃━┫┃╰┻━┃╭╮┃┃┃┃┃━┫
╰╯╱╰┻╯╰┻╯╰┻━╮┣┻┻┻╯╰┻╯╰╯╱╱╱╱╱╱╰╯╱╰╯╰┻━━╯╰━━━┻╯╰┻┻┻┻━━╯
╱╱╱╱╱╱╱╱╱╱╭━╯┃
╱╱╱╱╱╱╱╱╱╱╰━━╯
''']

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