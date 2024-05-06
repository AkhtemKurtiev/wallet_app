from datetime import datetime
import json
from pprint import pprint

from validations import (event_validation, number_validation,
                         search_event_validation)


with open('wallet.json', 'w+', encoding='utf-8') as file:
    big_data: dict = {}
    json.dump(big_data, file)


class Wallet():
    """Класс, описывающий приложение Кошелёк."""

    def __init__(self, money: int, income: int, expenses: int) -> None:
        self.money: int = money
        self.income: int = income
        self.expenses: int = expenses

    def show_money(self) -> None:
        """Показывает баланс.
         Пример вызова:
            person.show_money()
        """
        print(f'Текущий баланс: {self.money}')

    def show_income(self) -> None:
        """Показывает общую сумму доходов.
        Пример вызова:
            person.show_income()
        """
        print(f'Доходы {self.income}')

    def show_expenses(self) -> None:
        """Показывает общую сумму расходов.
        Пример вызова:
            person.show_expenses()
        """
        print(f'Расходы {self.expenses}')

    def show_events(self) -> None:
        """Показывает весь список записей.
        Пример вызова:
            person.show_events().
        """
        with open('wallet.json', 'r+', encoding='utf-8') as file:
            main_data = json.load(file)
            pprint(main_data)

    def add_event(self, amount: int, category: int, about: str) -> None:
        """Добавление записи.
        Аргументы:
            amount: int - сумма
            category: int - 1="Доход" 0="Расход"
            about:str - Описание
        Пример вызова:
            person.add_event(100, 0, 'Кофе').
        """
        category_name: str = 'Доход' if category else 'Расход'
        self.expenses += amount if not category else 0
        self.income += amount if category else 0
        self.money -= amount if not category else -amount

        data: dict = {
            'Дата': datetime.today().date().isoformat(),
            'Категория': category_name,
            'Сумма': amount,
            'Описание': about
        }

        with open('wallet.json', 'r+', encoding='utf-8') as file:
            main_data: dict[str, dict] = json.load(file)
            index: int = max(map(int, main_data.keys()), default=0) + 1
            main_data[str(index)] = data
            file.seek(0)
            json.dump(main_data, file, ensure_ascii=False)

    def update_event(self, number: str, amount: int,
                     category: int, about: str) -> None:
        """Редактирование записи.
        Аргументы:
            number: str - Номер записи
            amount: int - сумма
            category: int - 1="Доход" 0="Расход"
            about:str - Описание
        Пример вызова:
            person.update_event('1', 200, 0, 'Торт').
        """
        category_name: str = 'Доход' if category else 'Расход'

        with open('wallet.json', 'r+', encoding='utf-8') as file:
            main_data: dict[str, dict] = json.load(file)
            old_data: dict = main_data[number]

            if old_data['Категория'] != category_name:
                if category_name == 'Доход':
                    self.expenses -= old_data['Сумма']
                    self.income += amount
                    self.money += amount + old_data['Сумма']
                else:
                    self.income -= old_data['Сумма']
                    self.expenses += amount
                    self.money -= old_data['Сумма'] + amount
            else:
                if category_name == 'Доход':
                    self.income += amount - old_data['Сумма']
                    self.money += amount - old_data['Сумма']
                else:
                    self.expenses += amount - old_data['Сумма']
                    self.money += old_data['Сумма'] - amount

            new_data: dict = {
                'Дата': old_data['Дата'],
                'Категория': category_name,
                'Сумма': amount or old_data['Сумма'],
                'Описание': about or old_data['Описание']
            }
            main_data[number] = new_data
            file.seek(0)
            file.truncate()
            json.dump(main_data, file, ensure_ascii=False)

    def search_event(self, parameter: str, value: str) -> None:
        """Поиск записей по параметрам.
        Аргументы:
            parameter: str - По какому паметру вести поиск:
                    (Дата, Категория, Сумма, Описание)
            value: str - Какое значение:
                    (Дата: в формате YYYY-MM-DD;
                    Категория: 'Доход', 'Расход';)
        Пример вызова:
            person.search_event('Категория', 'ДоХОд').
        """
        with open('wallet.json', 'r+', encoding='utf-8') as file:
            main_data: dict[str, dict] = json.load(file)
            parameter = parameter.capitalize()
            value = value.capitalize()
            search_events = ([main_data[str(i+1)]
                             for i in range(len(main_data))
                             if main_data[str(i+1)][parameter] == value]
                             )
            for event in search_events:
                print(event)


def main():
    """Логика работы приложения Кошелёк."""
    person = Wallet(0, 0, 0)

    while True:
        try:
            print(("""
                Пожалуйста, введите цифру, желаемого действия:
                            1: Показать текущий баланс,
                            2: Показать доходы,
                            3: Показать расходы,
                            4: Показать весь список записей
                            5: Добавить запись,
                            6: Редактировать запись,
                            7: Поиск по записям
                """))
            action = number_validation(input())

            if action == '1':
                person.show_money()

            elif action == '2':
                person.show_income()

            elif action == '3':
                person.show_expenses()

            elif action == '4':
                person.show_events()

            elif action == '5':
                print("""
                    Пожалуйста, введите через ПРОБЕЛ: сумму,
                    категорию: 0 - Расход, 1 - Доход,
                    описание
                    """)

                amount, category, about = input().split(' ')
                event_validation(number=None, amount=amount, category=category)

                person.add_event(int(amount), int(category), about)

            elif action == '6':
                person.show_events()
                print("""
                    Пожалуйста, введите через ПРОБЕЛ: номер записи,
                    сумму, категорию: 0 - Расход, 1 - Доход,
                    описание.
                    """)

                number, amount, category, about = input().split(' ')
                event_validation(number=number, amount=amount,
                                 category=category)

                person.update_event(number, int(amount), int(category), about)

            elif action == '7':
                print("""
                    Пожалуйста, введите через ПРОБЕЛ
                    1. По какому паметру вести поиск:
                    (Дата, Категория, Сумма, Описание)
                    2. Какое значение:
                    (Дата: в формате YYYY-MM-DD;
                    Категория: 'Доход', 'Расход';)
                    """)

                parameter, value = input().split(' ')
                search_event_validation(parameter)

                person.search_event(parameter, value)

        except KeyError:
            print('Не существующий номер записи!')
        except ValueError:
            print('Пожалуйста, вводите все необходимые значения!')
        except Exception as error:
            print(f'Сбой работы программы: ошибка - {error}')


if __name__ == '__main__':
    main()
