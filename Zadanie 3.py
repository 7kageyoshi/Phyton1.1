# Вводим количество чисел
n = int(input("Введите количество чисел в последовательности: "))

# Инициализация счётчика простых чисел
count = 0

# Основной цикл для ввода чисел
for i in range(n):
    number = int(input("Введите число: "))
    if number > 1:  # Простые числа начинаются с 2
        for divider in range(2, int(number**0.5) + 1):
            if number % divider == 0:
                break
        else:
            count += 1

print("Количество простых чисел:", count)
