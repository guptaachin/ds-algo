class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)] # of size 26 - ALPHABET SIZE
        self.is_word = False # this current alphabet is a word

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        current = self.root
        for c in word:
            if current.children[ind(c)] == None:
                current.children[ind(c)] = TrieNode()
            current = current.children[ind(c)]
        current.is_word = True

    def search(self, word: str) -> bool:
        current = self.root
        for c in word:
            if current.children[ind(c)] != None:
                current = current.children[ind(c)]
            else:
                return False
        return current.is_word

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for c in prefix:
            if current.children[ind(c)] != None:
                current = current.children[ind(c)]
            else:
                return False
        return True

def ind(char):
    return ord(char) - ord('a')
