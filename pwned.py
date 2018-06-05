#!/usr/bin/env python
from __future__ import unicode_literals

import os
import sys
import argparse


R = '\033[31m'  # red
G = '\033[32m'  # green
C = '\033[36m'  # cyan
W = '\033[0m'  # white

version = "0.1"
author = "Phanatos"


def banner():

    # Clear the screen before showing the banner
    os.system('cls' if sys.platform == 'win32' else 'clear')

    banner_text = """
                                                                 ..         ..      
                    x=~                                        dF          888B.    
     .d``          88x.   .e.   .e.     u.    u.              '88bu.      48888E    
     @8Ne.   .u   '8888X.x888:.x888   x@88k u@88c.      .u    '*88888bu   '8888'    
     %8888:u@88N   `8888  888X '888k ^"8888""8888"   ud8888.    ^"*8888N   Y88F     
      `888I  888.   X888  888X  888X   8888  888R  :888'8888.  beWE "888L  '88      
       888I  888I   X888  888X  888X   8888  888R  d888 '88%"  888E  888E   8F      
       888I  888I   X888  888X  888X   8888  888R  8888.+"     888E  888E   4       
     uW888L  888'  .X888  888X. 888~   8888  888R  8888L       888E  888F   .       
    '*88888Nu88P   `%88%``"*888Y"     "*88*" 8888" '8888c. .+ .888N..888   u8N.     
    ~ '88888F`       `~     `"          ""   'Y"    "88888%    `"888*""   "*88%     
       888 ^                                          "YP'        ""        ""      
       *8E                                                                          
       '8>                                                                          
        "                                                                           
    """

    print(C + banner_text + W)
    print(C + '	Developed by: ' + W + author)
    print(C + '	Version: ' + W + version + '\n')


def parse_arguments():
    # Get commandline arguments
    parser = argparse.ArgumentParser()

    parser.add_argument('-e', '--email', required=False,
                        help='Email account you want to test')

    parser.add_argument('-f', '--file', required=False,
                        help='Load a file with multiple email accounts')

    return parser.parse_args()


class PwnChecker(object):

    def __init__(self, email=None, file=None):
        if email and file:
            raise ValueError("The class expects either a file or an email")

        self._file = file
        self._email = email

    def check(self):
        if not (self._email or self._file):
            raise ValueError("No file or email to process")

        if self.file:
            self.__process_file()
        else:
            self.__process_email(self._email)

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    @property
    def file(self):
        return self._file

    @file.setter
    def file(self, file):
        self._file = file

    def __process_email(self, email):
        (email)

    def __process_file(self):
        with open(self._file) as emails:
            for email in emails:
                self.__process_email(email)


def main():
    arguments = parse_arguments()
    pwned = PwnChecker()

    if arguments.file:
        pwned.file = arguments.file
    elif arguments.email:
        pwned.email = arguments.email

    pwned.check()


if __name__ == "__main__":
    try:
        banner()
        main()
    except KeyboardInterrupt as e:
        print('\n' + R + '[!]' + C + ' Keyboard Interrupt.' + W)
        exit()
