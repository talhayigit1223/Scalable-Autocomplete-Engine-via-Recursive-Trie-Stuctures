from engine import SearchEngine

engine = SearchEngine()
engine.build(r"C:\Users\talha\OneDrive\Desktop\DSA\Search Engine Project\data\unigram_freq.csv")

test_prefixes = ["comp", "sea", "py", "auto"]

for prefix in test_prefixes:
    print(f"\n--- '{prefix}' için öneriler ---")
    suggestions = engine.search(prefix, limit=10)
    for word, freq in suggestions:
        print(f"{word}: {freq}")
        
