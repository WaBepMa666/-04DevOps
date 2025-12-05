# 4. Проверка палиндрома
def is_palindrome(text):
    cleaned = ''.join(c.lower() for c in text if c.isalpha())
    return cleaned == cleaned[::-1]

print("Проверка палиндрома")
text = input("Введите текст: ")
if is_palindrome(text):
    print("Это палиндром!")
else:
    print("Это не палиндром")
