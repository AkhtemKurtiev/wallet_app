from exeptions import NotNumberValue


def number_isdigit(number: str, messsage: str) -> None:
    """Функция проверяет """
    if not number.isdigit():
        raise NotNumberValue(messsage)
