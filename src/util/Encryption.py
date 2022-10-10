from cryptography.fernet import Fernet
from base64 import b64encode

class KeyNotSpecifiedException(Exception):
	pass

class CryptoGraphy:
	""" An encryptor using the Fernet algorithm. """
	def  __init__(self, key = None):
		
		if key:

			padding = "$" * (32 - len(key))
			self.key = b64encode((key + padding).encode())
			self.superV = Fernet(self.key)

		else:

			raise KeyNotSpecifiedException("Key was not specified.")
			exit(1)

	def updateKey(self, new):
		""" Updates the key to use to Cipher/Decipher with. """
		padding = "$" * (32 - len(new))
		self.key = b64encode((new + padding).encode())

	def Cipher(self, plain):
		return self.superV.encrypt(plain.encode()).decode()

	def Decipher(self, cypher):
		return self.superV.decrypt(cypher).decode()
