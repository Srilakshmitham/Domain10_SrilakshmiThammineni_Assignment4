def longest_word(sentence):
    words = sentence.split()
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest


print(longest_word("The quick brown fox jumps over the lazy dog"))