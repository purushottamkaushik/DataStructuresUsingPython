class Node:
	def __init__(self, val ,isWord = False):
		"""
		Creating a node with given value and its child and special variable isWord to check if a word is completed or not
		"""
		self.val = val
		self.child = {}
		self.isWord = isWord


class Trie:
	def __init__(self):
		self.root = Node("")

	def insert(self,word):
		# Current variable is intialized to root node
		current = self.root 

		for ch in word: # Iterating each character 
			if ch not in current.child:	# If the character is not present in current nodes child nodes
			# then simply create a new node with the current character and add to the children		
				current.child[ch] = Node(ch)
			current = current.child.get(ch) # Updatinf the current node 
		
		# If for loop completes successfully then update the isWord Variable of the current Node to True 
		current.isWord = True 

	def search(self,word):
		current = self.root

		for ch in word: # Iterating over each character 
			if ch in current.child: # character present in current node child nodes  
				current = current.child.get(ch)
			else:
				return False

		return current.isWord
		
	def startswith(self, prefix):
		current = self.root

		for ch in prefix:
			if ch in current.child: #  character is present in the current node child nodes 
				current = current.child.get(ch)
			else:
				return False
		# IF FOR LOOP COMPLETED successfully means the all the characters are found in the tree then 
		# return true.		
		return True


s  = Trie()												
s.insert("apple")	
print(s.search("appple"))
print(s.startswith("app"))

