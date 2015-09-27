#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import sys
from stegatonic.stegatonic import StegaTonic

def main():

    banner = '''
   _____ _                _______          _      
  / ____| |              |__   __|        (_)     
 | (___ | |_ ___  __ _  __ _| | ___  _ __  _  ___ 
  \___ \| __/ _ \/ _` |/ _` | |/ _ \| '_ \| |/ __|
  ____) | ||  __/ (_| | (_| | | (_) | | | | | (__ 
 |_____/ \__\___|\__, |\__,_|_|\___/|_| |_|_|\___|
                  __/ |                           
                 |___/  By Michael Dubell <michael@mdubell.com>                                                                                                                     
    '''

    if len(sys.argv) >= 2:
        if sys.argv[1] == "-h" or sys.argv[1] == "--help":
            print banner

    parser = argparse.ArgumentParser(description='Stegatonic hides your secret messages in images',
        epilog='Example: ./stega.py -e -i wallpaper.png -p MyCoolPassword -m "Secret message"')

    parser.add_argument("--encode", "-e", help="Encode", action="store_true",dest='encode')
    parser.add_argument("--decode", "-d", help="Decode", action="store_true",dest='decode')
    parser.add_argument("--image", "-i", help="Image to encode/decode", required=True, type=str, action="store",dest='image')
    parser.add_argument("--password","-p", help="Password to protect your message", required=True,type=str, action="store",dest='password')
    parser.add_argument("--message","-m", help="Message to embed within your image",type=str, action="store",dest='message')

    args  = parser.parse_args()
    stega = StegaTonic(args.image)

    if args.encode:
        stega.encode(args.password, args.message)

    if args.decode:
        data = stega.decode(args.image, args.password)
        print "[+] Decoded message: %s" % (data)

if __name__ == "__main__":
    main()