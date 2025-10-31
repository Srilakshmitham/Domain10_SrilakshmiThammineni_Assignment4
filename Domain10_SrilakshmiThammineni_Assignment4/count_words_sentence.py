def count_words(sentence):
    words = sentence.split()
    return len(words)

print(count_words("The quick brown fox jumps over the lazy dog"))