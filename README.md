# CollectionDataBaseManager
-------------------------------

Commands:
	help: displays this message
	add: Create a new collection example -> add [name]
	delete: delete a particular collection example -> delete [index]
	edit: edit a collection using the index of the collection
	display: displays collections in this format: Index -> name
	Fdisplay: force display to display the paths
	key: display encryption key.

## Notes
	- Indexing will be provided
	- for the display command, if an index was provided, it loads and displays the content of a collection.


## Algorithms used
	- Fernet (to hash data)
	- base64 (to give an additional layer of protection)
	- sha256 (to hash the password)

