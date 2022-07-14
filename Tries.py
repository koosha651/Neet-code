
# NeetCode Challenge
# Solving Problems from NeetCode website, Tries

A Trie (prefix tree) is a special data structure used to store strings that can be visualized like a graph. There are various applications of this data structure, such
as autocomplete and spellchecker
Tries is useing for word validation
#=============================================================================================================================================================================

# The child of each node must be unique so at most for each node we have 26 unique child wich represent the lenght of english alphabet. Also, we dealing with 4 sub-function
# such as insert(), search(), startWith(). one of the advantage of using Tries is the startWith() function, which in compare to array reduce memory usage and time complexity

# Create seperate class named TriesNode: include children, endOfWord


class TrieNode:                         # build constractor for initialize with a base root
    def __init__(self):
        self.children = {}              # each node comes with it's own children. it can be 26 children
        self.endOfNode = False          # mark the last single node as end of a word

class Trie:

    def __init__(self):

        self.root = TrieNode()          # initialize the class with a root

    def insert(self, word: str) -> None:
        cur = self.root                 # initialize our current node to start from the root

        for c in word:                         # go trought every single charecter of the word and check 2 thing: does the charecter already exist or not
            if c not in cur.children:                    # if the charecter doesn't exist in our current hashmap,
                cur.children[c] = TrieNode()             # will create a Trie node for that. use charecter as key value and then create empty trie node
            cur = cur.children[c]                  # but if the charecter does already exist, set the curent to that node
        cur.endOfNode = True            # after iterating trough the word, set the last character as end of the word

    def search(self, word: str) -> bool:
        cur = self.root

        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.endOfNode


    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True

#=============================================================================================================================================================================
