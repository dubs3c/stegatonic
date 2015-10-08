#!/usr/bin/env python

from nose.tools import *
from ..stegatonic.stegatonic import StegaTonic
from ..stegatonic.stegatonicCrypto import StegaTonicCrypto

def test_encryption_decryption():
	crypto        = StegaTonicCrypto()
	test_string   = "Testing encryption and decryption"
	test_password = "test this"

	encrypted = crypto.encrypt(test_string, test_password)
	decrypted = crypto.decrypt(encrypted, test_password)
	
	assert_equal(decrypted, test_string)

def test_encode_decode():
	test_message  = "Testing encoding"
	test_password = "Test"
	test_image = "test/lime.png"

	stega = StegaTonic(test_image)

	stega.encode(test_password, test_message)
	decoded = stega.decode(test_image.replace(".png","_out.png"), "Test-288")

	assert_equal(decoded, test_message)


