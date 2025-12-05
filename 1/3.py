# 3. Конвертер валют
rates = {"USD": 97.5, "EUR": 106.2, "RUB": 1.0}

def convert_currency(amount, from_curr, to_curr):
    return amount * rates[from_curr] / rates[to_curr]

print("Конвертер валют")
amount = float(input("Сумма: "))
from_curr = input("Из валюты (USD/EUR/RUB): ").upper()
to_curr = input("В валюту (USD/EUR/RUB): ").upper()
result = convert_currency(amount, from_curr, to_curr)
print(f"{amount} {from_curr} = {result:.2f} {to_curr}")
