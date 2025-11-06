#Task1
from datetime import datetime

def get_days_from_today(date: str) -> int:

    try:
        input_date = datetime.strptime(date, "%Y-%m-%d").date()
        today = datetime.today().date()
        return (today - input_date).days
    except ValueError:
        raise ValueError("Неправильний формат дати. Використовуйте 'YYYY-MM-DD'.")

if __name__ == "__main__":
    print(get_days_from_today("2021-10-09"))  
    print(get_days_from_today("2030-01-01"))  


#Task2
import random

def get_numbers_ticket(min: int, max: int, quantity: int) -> list:

    if (
        not isinstance(min, int) or not isinstance(max, int) or not isinstance(quantity, int)
        or min < 1
        or max > 1000
        or min > max
        or quantity <= 0
        or quantity > (max - min + 1)
    ):
        return []

    numbers = random.sample(range(min, max + 1), quantity)

    return sorted(numbers)


if __name__ == "__main__":
    print(get_numbers_ticket(1, 49, 6))   
    print(get_numbers_ticket(10, 20, 5))  
    print(get_numbers_ticket(1, 5, 10))   




#Task3
import re

def normalize_phone(phone_number: str) -> str:

    cleaned = re.sub(r"[^\d+]", "", phone_number)

    if cleaned.startswith("+38"):
        return cleaned

    if cleaned.startswith("380"):
        return "+" + cleaned

    if cleaned.startswith("+380"):
        return cleaned

    return "+38" + cleaned


if __name__ == "__main__":
    raw_numbers = [
        "067\t123 4567",
        "(095) 234-5678\n",
        "+380 44 123 4567",
        "380501234567",
        "    +38(050)123-32-34",
        "     0503451234",
        "(050)8889900",
        "38050-111-22-22",
        "38050 111 22 11   ",
    ]

    sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
    print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)



#Task4

from datetime import datetime, date, timedelta

def get_upcoming_birthdays(users: list[dict]) -> list[dict]:

    today = date.today()
    end_date = today + timedelta(days=7)
    result = []

    for user in users:
        try:
            birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        except (KeyError, ValueError):
            continue 

        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        if today <= birthday_this_year <= end_date:
            congratulation_date = birthday_this_year

            if congratulation_date.weekday() == 5:
                congratulation_date += timedelta(days=2)
            elif congratulation_date.weekday() == 6:
                congratulation_date += timedelta(days=1)

            result.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })

    result.sort(key=lambda item: item["congratulation_date"])
    return result


if __name__ == "__main__":
    users = [
        {"name": "John Doe", "birthday": "1985.01.23"},
        {"name": "Jane Smith", "birthday": "1990.01.27"},
        {"name": "Bob Marley", "birthday": "1980.01.28"},
        {"name": "Anna Baron", "birthday": "2000.01.30"},
    ]

    upcoming_birthdays = get_upcoming_birthdays(users)
    print("Список привітань на цьому тижні:", upcoming_birthdays)




