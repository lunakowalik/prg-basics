import MyText

text = "An apple a day keeps the doctor away"

by_len = MyText.words_by_length(text)
alphabetical = MyText.words_alphabetical(text)

print("Text:", text)
print("Number of words:", MyText.word_count(text))
print("Words from the longest:", ",".join(by_len))
print("Words ordered alphabetically:", ",".join(alphabetical))