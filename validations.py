from exeptions import NotValidNumber, NotValidParameter
from service import number_isdigit


def number_validation(number: str) -> str:
    """Валидатор цифры - выбор из списка действий."""
    number_isdigit(number, 'Пожалуйста, введите число')
    if int(number) < 0 or int(number) > 8:
        raise NotValidNumber('Пожалуйста, введите число от 1 до 7')
    return number


def event_validation(number: str | None, amount: str,
                     category: str) -> None:
    """Валидатор данных при создание и редактировании записи."""
    if number:
        number_isdigit(number, """Пожалуйста, вводите
                                 значение для номера записи - число""")

    number_isdigit(amount, """Пожалуйста, вводите
                                 значение для суммы - число""")

    number_isdigit(category, """Пожалуйста, вводите
                                 значение для категории - число
                   (0 - Расход, 1 - Доход)""")

    categories = ['0', '1']
    if category not in categories:
        raise NotValidNumber("""Пожалуйста, вводите число 0 - Расход
                              или 1 - доход""")


def search_event_validation(parameter: str) -> None:
    parameters = ['Дата', 'Категория', 'Сумма', 'Описание']
    parameter = parameter.capitalize()
    if parameter not in parameters:
        raise NotValidParameter("""Такого парметра не существует,
                                пожалуйста используйте следующие параметры
                                Дата, Категория, Сумма, Описание""")
