def caching_fibonacci():
    # Створюємо порожній словник для кешування
    cache = {}

    # Внутрішня функція для обчислення числа Фібоначчі
    def fibonacci(n):
        # Базовий випадок: n <= 0
        if n <= 0:
            return 0
        # Базовий випадок: n == 1
        elif n == 1:
            return 1
        # Якщо значення вже є в кеші — повертаємо його
        if n in cache:
            return cache[n]
        # Інакше — обчислюємо, додаємо до кешу і повертаємо
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    # Повертаємо функцію fibonacci із замиканням на cache
    return fibonacci

# Отримуємо функцію fibonacci з кешем
fib = caching_fibonacci()

# Обчислюємо кілька чисел Фібоначчі
print(fib(10))  # Результат: 55
print(fib(15))  # Результат: 610