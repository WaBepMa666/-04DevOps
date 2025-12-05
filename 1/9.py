# 1. Калькулятор BMI
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        return "Недовес"
    elif bmi < 25:
        return "Норма"
    elif bmi < 30:
        return "Избыток"
    else:
        return "Ожирение"

print("Калькулятор ИМТ")
weight = float(input("Вес (кг): "))
height = float(input("Рост (м): "))
result = calculate_bmi(weight, height)
print(f"Ваш ИМТ: {weight / (height ** 2):.1f} - {result}")
