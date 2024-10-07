import random

def get_numbers_ticket(min, max, quantity: int) -> list:
    """
    Функція генерує вказану кількість унікальних чисел у заданому діапазоні.

    Параметри:
    min_val (int): мінімальне можливе число у наборі (не менше 1).
    max_val (int): максимальне можливе число у наборі (не більше 1000).
    quantity (int): кількість чисел, які потрібно вибрати (значення між min і max).

    Повертає:
    list: Відсортований список унікальних випадкових чисел.
          Якщо параметри не відповідають заданим обмеженням, функція повертає пустий список."""
    # Перевірка на відповідність параметрів
    if min < 1 or max > 1000 or quantity < 1 or quantity > (max - min + 1):
        return []
    # Генерація унікальних випадкових чисел
    random_numbers = random.sample(range(min, max + 1), quantity)

    return sorted(random_numbers)

# Параметри запиту для виведення
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)
