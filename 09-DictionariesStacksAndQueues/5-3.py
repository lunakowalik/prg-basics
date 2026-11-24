translations = {
    'computer': 'komputer',
    'mouse': 'myszka',
    'keyboard': 'klawiatura',
    'printer': 'drukarka'
}

word = input("Enter a word in English: ").strip().lower()

if word in translations:
    print(f"Translation: {translations[word]}")
else:
    print("Translation is unavailable.")