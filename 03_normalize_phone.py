import re

def normalize_phone(phone_number: str) -> str:
    """
    Функція нормалізує телефонні номери, додаючи міжнародний код України (+38), 
    якщо він відсутній. Видаляє всі зайві символи.

    Аргументи:
    phone_number (str): Вхідний телефонний номер у будь-якому форматі.

    Повертає:
    str: Нормалізований телефонний номер з міжнародним кодом.
    """
    # Видалення всіх символи, крім цифр та '+', видалення пробілів на початку і в кінці
    numbers_cleaned = re.sub(r"[^\d+]", "", phone_number.strip())
    # Додавання міжнародного коду України, якщо він відсутній
    numbers_cleaned = re.sub(r"^\+?(38)?", "+38", numbers_cleaned)
    return numbers_cleaned

raw_numbers = [
    "067\t123 4567", "(095) 234-5678\n", "+380 44 123 4567", 
    "380501234567", "+38(050)123-32-34", "0503451234"
]
# Нормалізує номери телефону зі списку raw_numbers та зберігає до нового списку sanitized_numbers
sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані телефонні номери:", sanitized_numbers)