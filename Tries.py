
# NeetCode Challenge
# Solving Problems from NeetCode website, Tries

A Trie (prefix tree) is a special data structure used to store strings that can be visualized like a graph. There are various applications of this data structure, such
as autocomplete and spellchecker
Tries are used for word validation
#=============================================================================================================================================================================

# The child of each node must be unique so at most for each node we have 26 unique children which represent the length of the english alphabet. Also, we dealing with 4 sub-function
# such as insert(), search(), startWith(). one of the advantages of using Tries is the startWith() function, which in comparison to array reduce memory usage and time complexity




class TrieNode:                         # Create separate class named TriesNode: include children, endOfWord // build contractor for initialize with a base root
    def __init__(self):
        self.children = {}              # each node comes with it's own children. it can be 26 children
        self.endOfNode = False          # can mark every single word as a last single node as the end of a word

class Trie:

    def __init__(self):

        self.root = TrieNode()          # initialize the class with a root node

    def insert(self, word: str) -> None:
        cur = self.root                 # initialize our current node to start from the root

        for c in word:                         # go through every single character of the word and check 2 things: does the character already exist or not

            if c not in cur.children:                    # if the character doesn't exist in our current hashmap,
                cur.children[c] = TrieNode()             # will create a Trie node for that. use a character as a key value and then create an empty trie node

            cur = cur.children[c]                  # but if the character does already exist, set the curent to that node
        cur.endOfNode = True            # after iterating through the word, set the last character as end of the word

    def search(self, word: str) -> bool:
        cur = self.root

        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.endOfNode            # cur is the last element of the word. return True if the last current node was the end of the node


    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True

#=============================================================================================================================================================================

2.  Design Add and Search Words Data Structure

# except search function all of the code is the same
# very complex part

https://www.youtube.com/watch?v=BTf05gs_8iU&t=1059s

https://www.youtube.com/watch?v=h-F2jRUzpBo&t=974s

class TrieNode:
    def __init__(self):
        self.children = {}  # a : TrieNode
        self.word = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True

    def search(self, word: str) -> bool:
        def dfs(j, root):
            cur = root

            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for child in cur.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.word

        return dfs(0, self.root)
