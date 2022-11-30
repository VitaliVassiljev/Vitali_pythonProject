with open('venv/txt_files/Akkords.txt', 'r', encoding='utf-8') as book:
    data = book.read() .lower()
print(len(data))
print(book.name)
with open('Akkords_copy.txt', 'w', encoding='utf8') as book:
    unique_words = list(set(data))
print(unique_words)
with open('Akkords_copy.txt', 'w', encoding='utf8') as result:
    result.write(f'There are {len(data)} words in {book.name} .\n')
    result.write(f'There are {len(unique_words)} unique_words in {book.name}.\n')
    unique_words.sort()

    for word in unique_words:
        result.write(word + '\n')