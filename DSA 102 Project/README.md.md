# High-Performance Prefix Autocomplete Engine (Weighted Trie & Pruned DFS)

This repository contains a high-performance, real-time prefix autocomplete engine built with Python. Developed as part of the DSA 102 course at Gebze Technical University, this project implements a custom **Weighted Trie** data structure combined with a **Heuristic Pruned Depth-First Search (DFS)** to fetch top recommendations instantaneously from massive wordcorpuses.

## 🚀 Key Features (Delivered Milestones)
* **Frequency-Weighted Suggestions:** Instead of slow post-retrieval sorting or simple alphabetical matching, nodes keep track of vocabulary statistical weights. Matches are ranked dynamically via a priority queue/min-heap structure.
* **Subtree Max Weight ($W_{max}$):** The computational load is shifted to the ingestion phase. Parent nodes cache the maximum weight among all nested descendants (`max_freq_below`), allowing the engine to proactively skip/prune non-optimal sub-branches during real-time queries.
* **Memory Management:** To eliminate Python's standard object-oriented structural overhead (`__dict__`), data structures are optimized using a highly predictable flat memory layout, significantly dropping the overall RAM footprint.

---

## 📁 Repository Structure

```text
├── data/
│   └── unigram_freq.csv       # Dataset extracted from the Google Web Trillion Word Corpus
├── preprocessor.py            # Text sanitization, case-folding, and tokenization pipeline
├── trie.py                    # Custom TrieNode and Weighted Trie implementation
├── engine.py                  # Search Engine abstraction wrapper
├── main.py                    # Interactive/demonstrative CLI script
├── benchmark.py               # Algorithmic efficiency and memory profiling metrics
└── README.md                  # Project documentation (This file)