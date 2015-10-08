import warnings
import binascii
import random
import math
import sys
from stegatonicCrypto import StegaTonicCrypto

try:
    from PIL import Image
except ImportError:
    warnings.warn("You need to install Pillow")

class StegaTonic(object):

    def __init__(self, image):
        self.image  = image
        self.stegaCrypto = StegaTonicCrypto()

    def msg2bin(self, msg):
        text = ""
        for x in msg:
            text += bin(ord(x))[2:].rjust(8, '0')
        return text

    def msg2dec(self, msg):
        dec = 0
        for t in msg:
            dec += ord(t)
        return dec

    def encode(self, pw, message):
        try:
            im = Image.open(self.image)
        except IOError:
            sys.exit("[-] Could not load image. Did you specify correct path?")

        load = im.load()

        encryptedText = self.stegaCrypto.encrypt(message, pw)

        pix    = im.getdata()
        imageWidth,imageHeight = im.size
        text   = self.msg2bin(encryptedText)

        pixelsNeeded = len(encryptedText) * 3

        if pixelsNeeded > (imageHeight * imageWidth):
            print "[-] Not enough pixels to encode! Quiting..."
            sys.exit(1)
        
        msgToDec = self.msg2dec(pw)

        dominantColor = self.analyze(pix)
        channels      = {'RED':0, 'GREEN':1, 'BLUE':2}

        print "[+] Your password is %s-%d" % (pw, pixelsNeeded)

        count = 0
        start = 0
        end   = 3
        for x in xrange(0,pixelsNeeded):

            random.seed(msgToDec+x)

            pixelsHeight = random.randint(0,imageHeight-1)
            pixelsWidth  = random.randint(0,imageWidth-1)

            pixel = load[pixelsWidth, pixelsHeight]
            val   = pixel[channels[dominantColor]]
            bin   = '{0:08b}'.format(val)

            if count == 2:
                lsbBits = text[start:end-1]
                count   = 0
                bits    = str(bin)[0:6]
                start   += 2
                end     = start + 3
            else:
                lsbBits = text[start:end]
                count   += 1
                bits    = str(bin)[0:5]
                start   += 3
                end     += 3

            new = bits + lsbBits

            newPixelColor = int(new, 2)

            if dominantColor == 'RED':
                load[pixelsWidth,pixelsHeight] = (newPixelColor, pixel[1], pixel[2])
            if dominantColor == 'GREEN':
                load[pixelsWidth,pixelsHeight] = (pixel[0], newPixelColor, pixel[2])
            if dominantColor == 'BLUE':
                load[pixelsWidth,pixelsHeight] = (pixel[0], pixel[1], newPixelColor)

        newFile = self.fileOut(self.image)
        im.save(newFile)
        print "[+] Message has been embedded."

    def decode(self, pic, password):
        try:
            im = Image.open(pic)
        except IOError:
            print "[-] Could not load image. Did you specify correct path?"

        load = im.load()
        pix  = im.getdata()
        imageWidth,imageHeight = im.size

        print "[+] Image loaded..."

        msgToDec     = 0
        index        = password.rfind("-")
        pw           = password[:index]
        pixelsNeeded = int(password[index+1:])

        for t in password[:index]:
            msgToDec += ord(t)

        encoded = ""
        dominantColor = self.analyze(pix)

        channels = {'RED':0, 'GREEN':1, 'BLUE':2}
        binCount = 0
        for x in xrange(0,pixelsNeeded):

            random.seed(msgToDec+x)

            pixelsHeight = random.randint(0,imageHeight-1)
            pixelsWidth  = random.randint(0,imageWidth-1)

            pixel = load[pixelsWidth, pixelsHeight]
            val   = pixel[channels[dominantColor]]

            bin = '{0:08b}'.format(val)

            if binCount == 2:
                encoded += bin[-2:]
                binCount = 0
            else:
                encoded += bin[-3:]
                binCount += 1

        bin2int = int(encoded,2)
        decoded = binascii.unhexlify('%x' % bin2int)
        decrypted = self.stegaCrypto.decrypt(decoded, pw)
        if decrypted != False:
            return decrypted
        else:
            sys.exit("[-] HMAC failed, you probably have the wrong password")
        #print "[+] Decoded message: %s" % (decoded)

    def analyze(self, data):
        channel = {'RED': 0, 'GREEN':0, 'BLUE':0}

        totalPixels = len(data);

        for x in xrange(0,totalPixels):
            channel['RED']   += data[x][0]
            channel['GREEN'] += data[x][1]
            channel['BLUE']  += data[x][2]

        return max(channel, key=channel.get)

    def fileOut(self, path):
        filename = path[:-4]
        fileType = path[-4:]

        return "%s_out%s" % (filename, fileType)
