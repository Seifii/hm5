names = ["Ann", "Peter", "Ben", "Kris", "Ellie"]
age = ["15", "22", "13", "16", "18"]

try:
    cinl = input("Введіть ім'я: ")
    index = names.index(cinl)
    cina = input("Введіть вік: ")
    index = age.index(cina)
    print("Вітаємо,", cinl, "Ваш вік - ", cina)
except ValueError:
    print("Помилка: таке ім'я не знайдено.")
