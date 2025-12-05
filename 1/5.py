# 5. TODO список
todos = []

def show_todos():
    for i, todo in enumerate(todos, 1):
        print(f"{i}. {todo}")

print("TODO список")
while True:
    print("\n1.Добавить 2.Показать 3.Удалить 4.Выход")
    choice = input("Выбор: ")
    if choice == "1":
        todos.append(input("Задача: "))
    elif choice == "2":
        show_todos()
    elif choice == "3":
        show_todos()
        idx = int(input("Номер для удаления: ")) - 1
        if 0 <= idx < len(todos):
            todos.pop(idx)
    elif choice == "4":
        break
