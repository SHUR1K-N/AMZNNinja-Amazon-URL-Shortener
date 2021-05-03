import re; import os
import pyperclip
from termcolor import colored
import colorama

colorama.init()

loopFlag = 0; decoyIter = 1

BANNER1 = colored('''
   ▄▄▄       ███▄ ▄███▓▒███████▒ ███▄    █  ███▄    █  ██▓ ███▄    █  ▄▄▄██▀▀▀▄▄▄
  ▒████▄    ▓██▒▀█▀ ██▒▒ ▒ ▒ ▄▀░ ██ ▀█   █  ██ ▀█   █ ▓██▒ ██ ▀█   █    ▒██  ▒████▄
  ▒██  ▀█▄  ▓██    ▓██░░ ▒ ▄▀▒░ ▓██  ▀█ ██▒▓██  ▀█ ██▒▒██▒▓██  ▀█ ██▒   ░██  ▒██  ▀█▄
  ░██▄▄▄▄██ ▒██    ▒██   ▄▀▒   ░▓██▒  ▐▌██▒▓██▒  ▐▌██▒░██░▓██▒  ▐▌██▒▓██▄██▓ ░██▄▄▄▄██
   ▓█   ▓██▒▒██▒   ░██▒▒███████▒▒██░   ▓██░▒██░   ▓██░░██░▒██░   ▓██░ ▓███▒   ▓█   ▓██▒
   ▒▒   ▓▒█░░ ▒░   ░  ░░▒▒ ▓░▒░▒░ ▒░   ▒ ▒ ░ ▒░   ▒ ▒ ░▓  ░ ▒░   ▒ ▒  ▒▓▒▒░   ▒▒   ▓▒█░
    ▒   ▒▒ ░░  ░      ░░░▒ ▒ ░ ▒░ ░░   ░ ▒░░ ░░   ░ ▒░ ▒ ░░ ░░   ░ ▒░ ▒ ░▒░    ▒   ▒▒ ░
    ░   ▒   ░      ░   ░ ░ ░ ░ ░   ░   ░ ░    ░   ░ ░  ▒ ░   ░   ░ ░  ░ ░ ░    ░   ▒
        ░  ░       ░     ░ ░             ░          ░  ░           ░  ░   ░        ░  ░''', 'blue')
BANNER2 = colored('''                         ----------------------------------------''', 'blue')
BANNER3 = colored('''                         || AMZNNinja: The Amazon URL Shortener ||''', 'red')
BANNER4 = colored('''                         ----------------------------------------''', 'blue')


def printBanner():
    print(BANNER1), print(BANNER2), print(BANNER3), print(BANNER4)


def clrscr():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')
    printBanner()


if __name__ == '__main__':

    printBanner()

    while(True):

        finalURL = ""

        URL = input("\nEnter Amazon URL to shorten: ")

        if (URL != ""):
            domainURL = re.findall(r"(.+/{2}.+?)[/]", URL)
            slugURL = re.findall(r"(/dp.+?)[/]", URL)
            finalURL = "".join(domainURL + slugURL)
        elif (URL == ""):
            break

        print("\nShortened URL: " + finalURL)
        pyperclip.copy(finalURL)
        print("\nCopied to clipboard, press Enter to shorten another URL.")
        input()

        clrscr()
