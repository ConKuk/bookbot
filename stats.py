def get_num_words_in_text(text):
    words = text.split()
    return len(words)
    
def num_letters_in_text(text):
    counts = {}

    for char in text:
        if char:
            if char.lower() in counts:
                counts[char.lower()] += 1
            else:
                counts[char.lower()] = 1

    return counts

def sort_letter_counts(counts):

    def sort_on(item):
        return item["num"]

    counts_array = []
    for letter, count in counts.items():
        counts_array.append({"char": letter, "num": count})
    
    counts_array.sort(key=sort_on, reverse=True)

    return counts_array