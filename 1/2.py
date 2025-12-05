# 2. Генератор паролей
import random
import string

def generate_password(length=12):
    chars = string.ascii_letters + string.digits + "!@#$%"
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

print("Генератор паролей")
length = int(input("Длина пароля (8-20): "))
if 8 <= length <= 20:
    pwd = generate_password(length)
    print(f"Пароль: {pwd}")
else:
    print("Длина должна быть 8-20 символов")
