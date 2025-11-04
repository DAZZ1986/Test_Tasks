class TestClass:
    def __init__(self, numbers):
        self.numbers = numbers  # список чисел
        self.results = []

    def sum_numbers(self):
        """Суммирует все числа в списке с помощью цикла for."""
        total = 0
        for num in self.numbers:
            total += num
        return total

    def multiply_numbers(self):
        """Перемножает все числа с помощью цикла while."""
        product = 1
        index = 0
        while index < len(self.numbers):
            product *= self.numbers[index]
            index += 1
        return product

    def find_max(self):
        """Находит максимум с помощью цикла for и условия if."""
        max_num = self.numbers[0]
        for num in self.numbers:
            if num > max_num:
                max_num = num
        return max_num

    def process_numbers(self):
        """Обрабатывает числа: любит циклы и функции."""
        for num in self.numbers:
            if num % 2 == 0:
                self.results.append(f"{num} четное")
            else:
                self.results.append(f"{num} нечетное")
        return self.results

    def recursive_sum(self, index=0):
        """Рекурсивный метод для суммирования элементов."""
        if index == len(self.numbers):
            return 0
        return self.numbers[index] + self.recursive_sum(index + 1)

# Создаем объект класса
obj = TestClass([1, 2, 3, 4, 5])

print("Сумма чисел:", obj.sum_numbers())
print("Произведение чисел:", obj.multiply_numbers())
print("Максимальное число:", obj.find_max())
print("Обработка чисел:", obj.process_numbers())
print("Рекурсивная сумма:", obj.recursive_sum())