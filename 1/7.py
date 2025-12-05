# 7. Анализатор текста
def analyze_text(text):
    words = text.split()
    chars = len(text)
    sentences = text.count('.') + text.count('!') + text.count('?')
    return len(words), chars, sentences

print("Анализатор текста")
text = input("Введите текст: ")
words, chars, sentences = analyze_text(text)
print(f"Слов: {words}, Символов: {chars}, Предложений: {sentences}")
