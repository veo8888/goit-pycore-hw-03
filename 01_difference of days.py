from datetime import datetime
    
def get_days_from_today(date: str) ->int:
    """
    Функція обчислює кількість днів, ігноруючи час (години, хвилини, секунди)
    від зазначеної дати до сьогоднішнього дня.

    Параметри:
    date (str): Дата у форматі 'YYYY-MM-DD'

    Повертає:
    int: Кількість днів між сьогоднішнім днем та вказаною датою.
         У випадку неправильної дати повертається повідомлення про помилку.
    """
    try:
        # Перетворення рядка дати на об'єкт datetime
        given_date = datetime.strptime(date, '%Y-%m-%d').date()
        # Отримання поточної дати
        today = datetime.today().date()
        # Обчислення різниці в днях
        delta = today - given_date
        return delta.days
    # Якщо неправильний формат дати
    except ValueError:
        return "Невірный формат даты. Используйте формат 'YYYY-MM-DD'."
    
# Виведення результату   
print(get_days_from_today("2021-10-09"))