#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
from modules import stegatonic

def main():
    parser = argparse.ArgumentParser(description='Stegatonic uses steganography to hide data within images')

    parser.add_argument("--encode", "-e", help="Encode", action="store_true",dest='encode')
    parser.add_argument("--decode", "-d", help="Decode", action="store_true",dest='decode')
    parser.add_argument("--image", "-i", help="Image to encode/decode", required=True, type=str, action="store",dest='image')
    parser.add_argument("--password","-p", help="Password to protect your message", required=True,type=str, action="store",dest='password')
    parser.add_argument("--message","-m", help="Message to embed within your image",type=str, action="store",dest='message')

    args = parser.parse_args()

    stega = StegaTonic(args.image)
    if args.encode:
        stega.encode(args.password,args.message)

    if args.decode:
        stega.decode(args.image, args.password)

if __name__ == "__main__":
    main()