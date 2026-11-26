def word_count(text):
    words = text.split()
    count = 0
    for _ in words:
        count += 1
    return count


def words_by_length(text):
    words = text.split()
    n = len(words)
    for i in range(n):
        for j in range(0, n - i - 1):
            if len(words[j]) < len(words[j + 1]):
                words[j], words[j + 1] = words[j + 1], words[j]
    return words


def words_alphabetical(text):
    words = text.split()
    n = len(words)
    for i in range(n):
        for j in range(0, n - i - 1):
            if words[j].lower() > words[j + 1].lower():
                words[j], words[j + 1] = words[j + 1], words[j]
    return words