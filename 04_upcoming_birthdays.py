from datetime import datetime

def get_upcoming_birthdays(users: list) -> list:
    """Функція визначає користувачів,
    у яких дні народження випадають вперед на 7 днів включаючи поточний день.
    Якщо день народження припадає на вихідний, дата привітання переноситься на наступний понеділок.

    Параметри:
    users (list): Список користувачів з іменами та датами народження

    Повертає:
    list: Список користувачів з датами привітань, якщо дні народження на найближчі 7 днів."""
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        # Перетворення дати народження в об'єкт datetime, (без часу)->.date()
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        # Перенесення дати дня народження на поточний рік
        birthday_this_year = birthday.replace(year=today.year)

        # Якщо день народження цього року вже пройшов, переносимо на наступний рік
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year +1)

        # Якщо день народження у межах 7 днів від сьогоднішнього дня
        if 0 <= (birthday_this_year - today).days <=7:
            # Вираховуєм субота або неділя
            if birthday_this_year.weekday() >=5:
                # Якщо день народження випадає на вихідний, переносимо на понеділок
                birthday_this_year += timedelta(days=(7 - birthday_this_year.weekday()))

            upcoming_birthdays.append({
                'name': user['name'],
                'congratulation_date': birthday_this_year.strftime("%Y.%m.%d")
            })
            
    return upcoming_birthdays

# Параметри запиту
users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]
upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
