import math

try:
    result = math.sqrt(25)
    print("Результат:", result)

except AttributeError:
    print("Помилка, функцію не знайдено в модулі.")

except ImportError:
    print("Помилка, модуль не вдалося імпортувати.")

except Exception as e:
    print("Інша помилка, ", e)


