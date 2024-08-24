# Вводим размеры рамки
width = int(input("Введите ширину рамки: "))
height = int(input("Введите высоту рамки: "))

# Внешний цикл отвечает за строки (высота)
for line in range(height):
    # Внутренний цикл отвечает за столбцы (ширина)
    for col in range(width):
        # Если текущий столбец - первый или последний, рисуем вертикальную границу
        if col == 0 or col == width - 1:
            print("|", end="")
        # Если текущая строка - первая или последняя, рисуем горизонтальную границу
        elif line == 0 or line == height - 1:
            print("-", end="")
        else:
            print(" ", end="")
    print()