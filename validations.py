from constants import CATEGORIES, PARAMETERS
from exeptions import NotValidDate, NotValidNumber, NotValidParameter
from service import number_isdigit


def number_validation(number: str) -> str:
    """Валидатор цифры - выбор из списка действий."""
    number_isdigit(number, 'Пожалуйста, вводите число')
    if int(number) < 0 or int(number) > 8:
        raise NotValidNumber('Пожалуйста, вводите число от 1 до 7')
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
    if category not in CATEGORIES:
        raise NotValidNumber("""Пожалуйста, вводите число 0 - Расход
                              или 1 - доход""")


def search_event_validation(parameter: str, value: str) -> None:
    parameter = parameter.capitalize()
    value = value.capitalize()
    if parameter not in PARAMETERS:
        raise NotValidParameter("""Такого парметра не существует,
                                пожалуйста используйте следующие параметры:
                                Дата, Категория, Сумма, Описание""")
    if parameter == 'Дата':
        if len(value) != 10 or value.count('-') != 2:
            raise NotValidDate("""Пожалуйста, вводите дату
                               в формате YYYY-MM-DD""")
    if parameter == 'Категория':
        if value not in CATEGORIES:
            raise NotValidParameter(("""Такой категории не существует,
                                пожалуйста, используйте следующие категории:
                                Доход или Расход"""))
    if parameter == 'Сумма':
        number_isdigit(value, 'Пожалуйста, вводите для суммы - число')
