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


def process_file(file):
    with open(file) as emails_file:
        for email in emails_file:
            process_email(email)


def process_email(email):
    print(email)


def main():
    arguments = parse_arguments()

    if arguments.file:
        process_file(arguments.file)
    elif arguments.email:
        process_email(arguments.email)


if __name__ == "__main__":
    try:
        banner()
        main()
    except KeyboardInterrupt as e:
        exit()
