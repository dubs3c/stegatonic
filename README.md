Steganography is the art and science of writing hidden messages in such a way that no one, apart from the sender and intended recipient, suspects the existence of the message, a form of security through obscurity.

The word steganography is of Greek origin and means "concealed writing" from the Greek words steganos (στεγανός) meaning "covered or protected", and graphei (γραφή) meaning "writing". - Wikipedia

StegaTonic encrypts your message with AES256 and emebds it within your specified image.

The method of encoding data within the image is a slighty modified version of the traditional LSB method. Instead of encoding the data in each pixel LSB StegaTonic first analyses all the pixels in the image and counts all the RGB channel values to find the one with highest total value (most used channel). The the channel with the highest value have been found, StegaTonic will start encoding data only in this channel.

This way you reduce the total amount of distortion made to the stego image which limits statistical analysis.

For encryption I'm using the pycrypto library.

# Install
1. git clone git@github.com:mjdubell/stegatonic.git
2. Change directory to stegatonic
3. python setup.py install
4. Done

If you have troubles installing pycrypto on Ubuntu, try installing the following:
	sudo aptitude install autoconf g++ gcc python2.7-dev gmp-devel