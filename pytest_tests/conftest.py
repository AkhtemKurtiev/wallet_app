import json

import pytest

from wallet import Wallet


@pytest.fixture(autouse=True)
def clean_wallet_json():
    """Фикстура отчищает json-файл перед тестами."""
    with open('wallet.json', 'w+', encoding='utf-8') as file:
        test_data = {}
        json.dump(test_data, file)


@pytest.fixture(scope="session", autouse=True)
def clean_wallet_after_test():
    """Фикстура отчищает json-файл после тестов."""
    yield
    with open('wallet.json', 'w', encoding='utf-8') as file:
        json.dump({}, file)


@pytest.fixture
def wallet():
    """Фикстура создаёт экземпяр класса Wallet"""
    return Wallet(0, 0, 0)


@pytest.fixture
def event(wallet):
    """Фикстура создаёт запись экземпляра Wallet"""
    wallet.add_event(100, 1, 'Тест')


@pytest.fixture
def events(wallet):
    """Фикстура создаёт записи экземпляра Wallet"""
    wallet.add_event(100, 1, 'Тест')
    wallet.add_event(400, 1, 'Тест3')
    wallet.add_event(500, 0, 'Тест5')
