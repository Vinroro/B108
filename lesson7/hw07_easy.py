# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.


class Triangle:
    def __init__(self, A, B, C):
        self.points = (A, B, C)

        self.lengths = (
            ((self.points[2][0] - self.points[1][0]) ** 2 + (self.points[2][1] - self.points[1][1]) ** 2) ** (1 / 2),
            ((self.points[0][0] - self.points[2][0]) ** 2 + (self.points[0][1] - self.points[2][1]) ** 2) ** (1 / 2),
            ((self.points[1][0] - self.points[0][0]) ** 2 + (self.points[1][1] - self.points[0][1]) ** 2) ** (1 / 2)
        )

    def perimeter(self):
        return self.lengths[0] + self.lengths[1] + self.lengths[2]

    def height(self, i):
        perimeter_half = self.perimeter() / 2
        return 2 / self.lengths[i] * (
                    perimeter_half * (perimeter_half - self.lengths[0]) * (perimeter_half - self.lengths[1]) * (
                        perimeter_half - self.lengths[2])) ** (1 / 2)

    def square(self):
        return self.lengths[0] * self.height(0) / 2


t = Triangle([1, 1], [3, 3], [3, 1])

print(f"Parameters of triangle with points {t.points[0]}, {t.points[1]}, {t.points[2]}")
print(f"Perimeter = {t.perimeter():.2f}")
print(f"Square = {t.square():.2f}")
i = input("Enter a point __number(0, 1 or 2) to get its height value: ")
print(f"Height[{i}] = {t.height(int(i)):.2f}")

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.


class Three_equal_sides_trapezoid:
    def __init__(self, A, B, C, D):
        self.points = (A, B, C, D)

    def lengths(self):
        return (
            ((self.points[0][0] - self.points[1][0]) ** 2 + (self.points[0][1] - self.points[1][1]) ** 2) ** (1 / 2),
            ((self.points[1][0] - self.points[2][0]) ** 2 + (self.points[1][1] - self.points[2][1]) ** 2) ** (1 / 2),
            ((self.points[2][0] - self.points[3][0]) ** 2 + (self.points[2][1] - self.points[3][1]) ** 2) ** (1 / 2),
            ((self.points[3][0] - self.points[0][0]) ** 2 + (self.points[3][1] - self.points[0][1]) ** 2) ** (1 / 2)
        )

    def three_equal_sides_check(self):
        no_unique_side_lengths = list(self.lengths())
        no_unique_side_lengths.remove(max(self.lengths()))

        return no_unique_side_lengths[0] == no_unique_side_lengths[1] == no_unique_side_lengths[2]

    def perimeter(self):
        result = 0

        for i in self.lengths():
            result += i

        return result

    def square(self):
        if self.three_equal_sides_check():
            side = min(self.lengths())
            unique_side = max(self.lengths())
            perimeter_half = self.perimeter() / 2

            return ((perimeter_half - unique_side) * (perimeter_half - side) ** 3) ** (1 / 2)
        else:
            print("The figure isn't the Three_equal_sides_trapezoid. Can't get a correct result")
            return -1


figure = Three_equal_sides_trapezoid([0, 0], [3, 4], [8, 4], [11, 0])
figure1 = Three_equal_sides_trapezoid([0, 0], [0, 5], [4, 8], [4, -3])
figure2 = Three_equal_sides_trapezoid([1, 0], [0, 5], [4, 8], [4, -3])

print(f"Parameters of trapezoid with points {figure.points[0]}, {figure.points[1]}, {figure.points[2]},"
      f"{figure.points[3]}")
print(f"Perimeter = {figure.perimeter():.2f}")
print(f"Square = {figure.square():.2f}")
