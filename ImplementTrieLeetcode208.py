
class Node:
    def __init__(self,val,isWord=False):
        self.val = val 
        self.child = {}
        self.isWord = isWord
        

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node("")
        
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        # Setting current to the root Node
        current = self.root
        # Iterating character by character and checking it is not present in the child nodes if present then point to the node else create a new node with the          character and point it towards the character.
        for ch in word:
            if ch not in current.child:
                current.child[ch] = Node(ch)
            current = current.child.get(ch)
        current.isWord = True    
            
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        current = self.root
        for ch in word:
            if ch in current.child:
                current = current.child.get(ch)
            else:
                return False
        return current.isWord
    

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        current = self.root
        for ch in prefix:
            if ch in current.child:
                current = current.child.get(ch)
            else:
                return False
        return True
    


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)