from trie import Trie
from preprocessor import load_frequency_csv, print_stats

class SearchEngine:
    def __init__ (self):
        self.trie = Trie()
        self.word_count = 0

    def build (self, file_path, verbose: bool = True):
        word_freq = load_frequency_csv(file_path)

        if verbose:
            print_stats(word_freq)
        
        for word, freq in word_freq.items():
            self.trie.insert(word, freq)
            self.word_count += 1

    def search (self, prefix, limit: int = 10):
        if not prefix:
            return []
        return self.trie.get_suggestions(prefix.lower(), limit)
    