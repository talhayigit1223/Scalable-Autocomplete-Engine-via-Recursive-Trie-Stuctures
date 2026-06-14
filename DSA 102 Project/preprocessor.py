import csv
import re

def load_frequency_csv(file_path):
    word_freq = {}
    with open(file_path, "r", encoding = "utf-8") as f:
        reader = csv.reader(f)
        next(reader)

        for row in reader:
            if len(row) < 2:
                continue
            word = row[0].strip().lower()

            try:
                count = int(row[1].strip())
            except ValueError:
                continue

            if len(word) < 2:
                continue
            if not re.match("^[a-z]+$", word):
                continue
            if count < 10:
                continue

            word_freq[word] = count
    return word_freq

def print_stats(word_freq):
    print(f"Toplam kelime sayısı: {len(word_freq)}")
    print(f"En sık kullanılan 10 kelime:")
    top10 = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)[:10]
    for word, count in top10:
        print(f"{word}: {count}")
    
    print(f"En nadir kullanılan 10 kelime:")
    bottom10 = sorted(word_freq.items(), key=lambda x: x[1])[:10]
    for word, count in bottom10:
        print(f"{word}: {count}")