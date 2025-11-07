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





