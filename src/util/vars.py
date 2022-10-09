from os import environ
from dataclasses import dataclass



DATAPATH = environ["PROGRAMFILES"] + "\\" + "CollectionApp"
shellPadding = " " * 2
DashBoardDocumentation = """
-----------------------------------------------------------------
COLLECTION DASHBOARD
Commands:
	help: displays this message
	add: Create a new collection example -> add [name]
	delete: delete a particular collection example -> delete [index]
	edit: edit a collection using the index of the collection
	display: displays collections in this format: Index -> name
	Fdisplay: force display to display the paths
	key: display encryption key.

Notes:
	- Indexing will be provided
	- for the display command, if an index was provided, it loads and displays the content of a collection.
-----------------------------------------------------------------
"""


class colors:
	""" Coloring later. """
	pass
