try:
    num = float(input("Введіть число: "))
    okr = round(num)
    print("Округлений результат:", okr)
except ValueError:
    print("Помилка")
