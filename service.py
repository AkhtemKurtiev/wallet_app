import json
from typing import Union, Any

from exeptions import NotNumberValue


def number_isdigit(number: str, text: str) -> None:
    """Функция проверяет, что строка содержит число."""
    if not number.isdigit():
        raise NotNumberValue(text)


def account_recovery(file_name) -> tuple[int, int, int]:
    """Восстанавливает данные пользователя после возобновления работы."""
    with open(file_name, 'r', encoding='utf8') as file:
        data: dict[str, dict[str, Union[int, Any]]] = json.load(file)
    income: int = 0
    expenses: int = 0
    money: int = 0

    for event in data.values():
        if event['Категория'] == 'Доход':
            income += event['Сумма']
        elif event['Категория'] == 'Расход':
            expenses += event['Сумма']

    money = income - expenses

    return money, income, expenses


def create_file_json(file_name: str) -> None:
    """Создаёт файл file_name.json."""
    with open(file_name, 'w') as file:
        json.dump({}, file, ensure_ascii=False)


def empty_file_json(file_name: str) -> None:
    """Если файл file_name.json пуст, добавляет в него: {}"""
    with open(file_name, 'r+') as file:
        try:
            json.load(file)
        except Exception:
            json.dump({}, file, ensure_ascii=False)
