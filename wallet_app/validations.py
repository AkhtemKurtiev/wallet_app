from wallet_app.exeptions import (NotNumberValue, NotValidNumber,
                                  NotValidParameter)


def number_isdigit(number: str, messsage: str) -> None:
    if not number.isdigit():
        raise NotNumberValue(messsage)


def number_validation(number: str) -> None:
    """Валидатор цифры - выбор из списка действий."""
    number_isdigit(number, 'Пожалуйста, введите число')
    if int(number) < 0 or int(number) > 8:
        raise NotValidNumber('Пожалуйста, введите число от 1 до 7')


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

    if int(category) != 0 or int(category) != 1:
        raise NotValidNumber("""Пожалуйста, вводите число от 0 - Расход
                             1 - доход""")


def search_event_validation(parameter: str, value: str):
    parameters = ['Дата', 'Категория', 'Сумма', 'Описание']
    if parameter not in parameters:
        raise NotValidParameter("""Такого парметра не существует,
                                пожалуйста используйте следующие параметры
                                Дата, Категория, Сумма, Описание""")
