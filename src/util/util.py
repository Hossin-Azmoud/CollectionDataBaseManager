from .vars import DATAPATH, shellPadding, COLORS
from os import path
from json import dumps, loads, dump, load
from hashlib import sha256
from base64 import b64encode, b64decode

def printp(s, *args): print(f"{shellPadding}{s}", *args)

class JSON:
	def parseJsonFile(Fname: str) -> dict:
		""" parsing the content of a file to become a python dict. """
		if path.exists(Fname): return load(open(Fname))
		else:
			print("The file you are trying to access does not exist, check the path you specified.")
			exit(1)

	def parseJsonString(s: str) -> dict:
		""" parsing a string -> dict. """
		return loads(s)

	def stringify(data: dict) -> str: 
		""" stringifying a python dict. """
		return dumps(data)

	def dumpToFile(Data, Fname) -> int:
		""" Dump dict into a file. """

		dump(Data, open(Fname, "w"), indent=2)
		return 0

def hash_(s: str):
	return sha256(s.encode()).hexdigest()

def checkHash(s: str, hashedString: str):
	return hash_(s) == hashedString



def ListToDict(list_: list):
	Map = {}

	for i, v in enumerate(list_):
		Map[i] = v

	return Map

def URandomID():
	return 

def cleanSTR(s): return s.strip()

def parseStrCommand(s, sep=" "): return [cleanSTR(i) for i in s.split(sep)]

def parseSepValue(data, sep=":"): 

	data = data.split(sep)

	if len(data) == 2:
		return { data[0].strip(): data[1].strip() }
	else:
		return False

def map(list_: list, fn: callable = None):
	if not fn:
		fn = lambda x: print(x)	

	for i in list_: fn(i)

def B64E(data): return b64encode(data.encode()).decode() if isinstance(data, str) else b64encode(data).decode()
def B64D(data): return b64decode(data).decode()


# wanted to use this class but it is clearly not working. for my pc atleast..
class console:
	""" basic class to write messages to the console. """
	def __init__(self):
		self.colors = COLORS
	def writeSuccess(self, s): printp(COLORS["green"] + s)
	def writeError(self, s): printp(COLORS["red"] + s)
	def writeInfo(self, s): printp(COLORS["yellow"] + s)
	def write(self, s, colorKey="yellow"): printp("{}".format(COLORS[colorKey])) if colorKey in list(self.colors.keys()) else printp("{}".format(COLORS["white"]))


