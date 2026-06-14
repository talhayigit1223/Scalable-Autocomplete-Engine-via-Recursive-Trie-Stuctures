class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.frequency = 0
        self.max_freq_below = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word, frequency):
        node = self.root
        node.max_freq_below = max(node.max_freq_below, frequency)

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.max_freq_below = max(node.max_freq_below, frequency)
        
        node.is_end_of_word = True
        node.frequency = frequency

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word
    
    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
    
    def get_suggestions(self, prefix, limit: int = 10):
        node = self.root

        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]

        suggestions = []
        self._dfs(node, prefix, suggestions, limit)
        return suggestions

    def _dfs(self, node, current_word, suggestions, limit):
        if len(suggestions) >= limit:
            return
        
        if node.is_end_of_word:
            suggestions.append((current_word, node.frequency))

        for char, child_node in node.children.items():
            self._dfs(child_node, current_word + char, suggestions, limit)

trie = Trie()

