from .Encryption import CryptoGraphy
from os import scandir, path, remove

from .util import (
	JSON, 
	B64E,
	B64D, 
	parseSepValue, 
	printp
)

import pprint
from .vars import shellPadding




class CollectionsClass:
	
	def __init__(self, CollectionsPath):
		
		self.CollectionsPath = CollectionsPath
		
		self.StoredCollections = {
			B64D(i.name): path.join(self.CollectionsPath, i.name) for i in scandir(self.CollectionsPath)
		}

		self.key = None

	def setDataProvider(self, k: str):
		self.key = k
		self.dataProvider = CryptoGraphy(self.key)

	@property
	def CollectionNames(self): return list(self.StoredCollections.keys())
	
	@property
	def CollectionPaths(self): return list(self.StoredCollections.values())

	def encryptData(self, d): return self.dataProvider.Cipher(d)
	
	def decryptData(self, d): return self.dataProvider.Decipher(d)
	
	def DeleteCollection(self, index):
		""" Deleting a data collection. """

		# Because we already get and decode the names.
		# I store all the paths for the collections in a dictionary. after initialization.
		Path = self.CollectionPaths[index]
		
		if path.exists(Path): 
			remove(Path)
			printp(f"* Deleted -> {Path} ")
		else:
			printp(f"* Did not delete -> {Path}, could not be found ")
	
	def EditData(self, prevData):
		UpdatingData = True
		newData = prevData

		if prevData:
			printp('Present data:')
			pprint.pprint(prevData)

		while UpdatingData:
			#THis block editing the object but I want to edit the collection??? lol.

			temp = {}

			command = input(f"{shellPadding}Enter command (Exit to finish process): ")
			if command.strip().upper() == "EXIT":
				return False
			elif command.strip().upper() == "SAVE":
				UpdatingData = False
				return newData
			else:
				temp = parseSepValue(command)
				if temp:
					newData.update(temp)
				else:
					printp("Failed to process you command, because the sep does not seem correct or you entered an invalid command.")
					printp("Righ syntax: Field: value.")


	def createNewCollection(self, name):
		""" add a new collection. """		
		NCODED = B64E(name)
		CollectionAbpath = path.join(self.CollectionsPath, f"{NCODED}.enc")

		prevData = {}
		UpdatingData = True

		printp(f"# Add/update using -> field and value seperated by \':\'")
		printp(f"# save using -> save command")

		NewData = self.EditData(prevData)
		
		if NewData:
			# saving the collection.
			self.saveCreatedCollection(CollectionAbpath, JSON.stringify(NewData), NCODED)


	def saveCreatedCollection(self, path_, data, NCODED):
		if not path.exists(path_):
			with open(path_, "w+") as fp:
				if data:
					fp.write(B64E(self.encryptData(data)))
				else: 
					fp.write("")
				printp("The collection was created ->", NCODED)
		else:
			cmd = input(f"{shellPadding}Collection already exists want to proceed regardless, [Y/y to confirm, any to deny.]: ")
			if cmd.strip().upper() == "Y":
				with open(path_, "w+") as fp: 
					if data:
						fp.write(B64E(self.encryptData(data)))
					else: 
						fp.write("")
					printp("The collection was created!", NCODED)
			else:
				printp("the collection was not saved.")

	def loadCollection(self, path_):
		if path.exists(path_):
			with open(path_) as fp:
				data = fp.read()
				
				if data:
					return JSON.parseJsonString(self.decryptData(B64D(data)))
				else:
					printp("Empty collection.")
					
		else:
			printp(f"Could not find the collectin {path_}")

	def saveCollection(self, Data, path_):
		with open(path_, "w+") as fp:
			# some security?..
			if isinstance(Data, dict): Data = JSON.stringify(Data)

			fp.write(B64E(self.encryptData(Data)))

	def EditCollection(self, index):
		
		if index < len(self.CollectionPaths) and index >= 0:
			p = self.CollectionPaths[index]		
			PrevData = self.loadCollection(p)
			if PrevData:
				NewData = self.EditData(PrevData)
				if NewData:
					self.saveCollection(NewData, p)
					printp(f"Collection was saved.")

			else: printp(f"Collection could not be loaded.")

		else:

			printp("Invalid index!!")

	def setCollection(self, path_: str): self.CollectionsPath = path_

	def AccessCollection(self, index):
		if index < len(self.CollectionPaths) and index >= 0:

			colData = self.loadCollection(self.CollectionPaths[index])
			if colData:
				pprint.pprint(colData)

		else:
			printp("Invalid index!!")

# url = 'https://www.youtube.com/watch?v=nykOeWgQcHM&list=PLUl4u3cNGP63WbdFxL8giv4yhgdMGaZNA'
