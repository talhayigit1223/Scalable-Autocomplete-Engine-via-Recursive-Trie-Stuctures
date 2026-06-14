import time 
import timeit
import tracemalloc
from engine import SearchEngine

import os


"""KURULUM"""

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE_DIR, "data", "unigram_freq.csv")

print("=" * 55)
print("SEARCH ENGINE BENCHMARK")
print("=" * 55)

print("\n[1] Trie inşa ediliyor...")
start = time.perf_counter()
engine = SearchEngine()
engine.build(CSV_PATH, verbose=False)
build_time = time.perf_counter() - start
print(f"    Inşa süresi : {build_time:.3f} saniye")
print(f"    Kelime sayısı: {engine.word_count:,}")


word_list = list(engine.trie.root.children.keys())

all_words = engine.search("", limit=1000000)
word_list = [w for w, f in all_words] if all_words else []

def get_all_words(trie):
    results = []
    def dfs(node, current):
        if node.is_end_of_word:
            results.append(current)
        for char, child in node.children.items():
            dfs(child, current + char)
    dfs(trie.root, "")
    return results

print("\n[2] Tüm kelimeler çekiliyor (linear search için)...")
all_words = get_all_words(engine.trie)
print(f"    Toplam: {len(all_words):,} kelime")


"""HIZ KARŞILAŞTIRMASI"""

def linear_search(words: list, prefix: str) -> list[str]:
    return [w for w in words if w.startswith(prefix)]

def trie_search(engine, prefix: str) -> list:
    return engine.search(prefix, limit=10)

REPEATS = 1000
test_prefixes = ["co", "comp", "comput", "a", "xyz"]

print("\n[3] Hız Karşılaştırması")
print("-" * 55)
print(f"{'Prefix':<10} {'Linear (ms)':>12} {'Trie (ms)':>12} {'Hızlanma':>10}")
print("-" * 55)

for prefix in test_prefixes:
    # Linear search zamanı
    linear_time = timeit.timeit(
        lambda: linear_search(all_words, prefix),
        number=REPEATS
    ) / REPEATS * 1000  # ms cinsinden

    # Trie search zamanı
    trie_time = timeit.timeit(
        lambda: trie_search(engine, prefix),
        number=REPEATS
    ) / REPEATS * 1000  # ms cinsinden

    speedup = linear_time / trie_time if trie_time > 0 else float('inf')

    print(f"{prefix:<10} {linear_time:>11.4f}ms {trie_time:>11.4f}ms {speedup:>9.1f}x")

print("-" * 55)


"""BELLEK KULLANIMI"""

print("\n[4] Bellek Kullanımı")
print("-" * 55)

# Trie bellek kullanımı
tracemalloc.start()
engine2 = SearchEngine()
engine2.build(CSV_PATH, verbose=False)
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

print(f"    Trie peak bellek : {peak / 1024 / 1024:.2f} MB")
print(f"    Trie anlık bellek: {current / 1024 / 1024:.2f} MB")

# Liste bellek kullanımı
import sys
list_memory = sys.getsizeof(all_words) + sum(sys.getsizeof(w) for w in all_words)
print(f"    Liste bellek     : {list_memory / 1024 / 1024:.2f} MB")


"""WORST CASE ANALİZİ"""


print("\n[5] Worst Case Analizi")
print("-" * 55)

worst_prefixes = ["a", "s", "t"]
for prefix in worst_prefixes:
    count = len(linear_search(all_words, prefix))
    trie_result = engine.search(prefix, limit=999999)
    print(f"    '{prefix}' prefix → {count:,} kelime")

print("\n" + "=" * 55)
print("BENCHMARK TAMAMLANDI")
print("=" * 55)