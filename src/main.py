from os import path, mkdir, rmdir, system, scandir
from util.vars import DATAPATH, DashBoardDocumentation, shellPadding
from util.util import JSON, hash_, checkHash, parseStrCommand, printp
from util.dbUtil import CollectionsClass
from time import sleep


class CollectionManager:

	def __init__(self):

		cmd = input("""
  (1) Login
  (2) Sign in

  answer: """
)


		# Login.
		
		if cmd.strip() == "1": self.login()
		# sign_in.
		elif cmd.strip() == "2": self.SignIn()
		else:
			printp("did not understand the option you specified, you could try again.")
			self.__init__()


	def mkdirIfNotExist(self, path):

		if not path.exists(path):
			mkdir(path)
			sleep(1)

	def SignIn(self):
		printp("Making data files and folders..")

		# Making the data folder.		
		self.mkdirIfNotExist(DATAPATH)

		# Making user folder
		self.mkdirIfNotExist(self.UserFolderPath)

		# startup config
		data = {
			"username": self.userName,
			"pwd": hash_(self.password)
		}

		# saving config variables.
		JSON.dumpToFile(data, self.ConfigFilePath)

		# making collections folder.
		self.mkdirIfNotExist(self.collectionsPath)

		# Quitting
		printp("You account was made with success, you can now Login and try our product.")
		
		cmd = input(f"{shellPadding}want to be directed to the dashboard ? (y/n) ")

		if cmd.strip().upper() == "Y": self.dashBoard() 

	def GetPasswordHash(self):
		return JSON.parseJsonFile(self.ConfigFilePath)["pwd"]


	def displayData(self, data, force=False):
		if len(data) > 0:
				for i, v in enumerate(data):
					if force:
						printp(f'[{i}] : {v} -> {self.Db.CollectionPaths[i]}')
					else:
						printp(f'[{i}] : {v}')
		else:
			printp("---- No collections added yet ----")

	def load(self):
		self.Db = CollectionsClass(self.collectionsPath)
		self.Db.setDataProvider(self.password)
		return self.Db.CollectionNames

	def info(self):
		print()
		printp(f"current user: {self.userName}")
		printp(f"user folder: {self.UserFolderPath}")
		printp(f"Collection path: {self.collectionsPath}")
		printp(f"Collection count: {len(self.load())}")
		print()

	def dashBoard(self):
		run_ = True
		init = True
		printp(DashBoardDocumentation)

		while run_:
			Data = self.load()
			if init:
				self.displayData(Data)
				init = False

			command = input(f"[{self.userName}] -> ")
			
			if len(command) > 0:

				parsedCommand = parseStrCommand(command)

				if len(parsedCommand) > 1:
					parsedCommand = {
						'cmd': parsedCommand[0],
						'args': parsedCommand[1:]
					}

					if parsedCommand['cmd'].upper() == "ADD": self.Db.createNewCollection(parsedCommand['args'][0])
					elif parsedCommand['cmd'].upper() == "DELETE": self.Db.DeleteCollection(int(parsedCommand['args'][0])) 
					elif parsedCommand['cmd'].upper() == "EDIT": self.Db.EditCollection(int(parsedCommand['args'][0]))
					elif parsedCommand['cmd'].upper() == "DISPLAY": self.Db.AccessCollection(int(parsedCommand['args'][0]))
					else: printp("This command is invalid!!")
				else:
					parsedCommand = parsedCommand[0].upper()
					if parsedCommand == "EXIT": exit(0)
					elif parsedCommand == "HELP": printp(DashBoardDocumentation)
					elif parsedCommand == "DISPLAY": self.displayData(Data) 
					elif parsedCommand == "FDISPLAY": self.displayData(Data, True)
					elif parsedCommand == "KEY": printp(self.Db.dataProvider.key.decode())
					elif parsedCommand == "INFO": self.info()
					else: printp(f"invalid command  {parsedCommand}")
			else:
				pass


	def CheckConfigPaths(self):
		for i in self.RFolders:
			if not path.exists(i): 
				printp(f"{i} does not exist")
				exit(1)
				



	def login(self, re=False):
		

		if not re:
			self.userName = input(f"{shellPadding}UserName: ")
			
			while len(self.userName) == 0:
				self.userName = input(f"{shellPadding}UserName: ")

		self.password = input(f"{shellPadding}password: ")

		while len(self.password) == 0:
			self.password = input(f"{shellPadding}password: ")
	
		self.UserFolderPath = path.join(DATAPATH, self.userName)
		self.ConfigFilePath = path.join(self.UserFolderPath, ".config.json")
		self.collectionsPath = path.join(self.UserFolderPath, "DataCollections") 
		self.RFolders = [self.UserFolderPath, self.ConfigFilePath, self.collectionsPath]

		if path.exists(self.UserFolderPath):
			
			self.CheckConfigPaths()
			if path.exists(self.ConfigFilePath):
				pwdHashed = self.GetPasswordHash()
				
				if not checkHash(self.password, pwdHashed):
					printp("The password you specified is wrong. try again...")
					self.login(True)
				else:
					printp("Welcome to your account ", self.userName)
					self.dashBoard()
			else:
				printp("Json config file seems to be missing.")

		else:
			cmd = input(f"{shellPadding}Would you like to sign in for a new account [Y/y - N/n]: ")
			
			if cmd.strip().upper() == "Y":
				self.SignIn()
			else:
				exit(0)

if __name__ == "__main__":
	CollectionManager()