from datetime import datetime


def test_show_money(wallet, capsys):
    """Тест метода show_money."""
    wallet.show_money()
    text = capsys.readouterr()
    assert 'Текущий баланс: 0' in text.out


def test_show_income(wallet, capsys):
    """Тест метода show_income."""
    wallet.show_income()
    text = capsys.readouterr()
    assert 'Доходы 0' in text.out


def test_show_expenses(wallet, capsys):
    """Тест метода show_expenses."""
    wallet.show_expenses()
    text = capsys.readouterr()
    assert 'Расходы 0' in text.out


def test_show_event(wallet, capsys):
    """Тест метода show_events."""
    wallet.show_events()
    text = capsys.readouterr()
    assert '{}' in text.out


def test_add_event(wallet, event, capsys):
    """Тест метода add_event."""
    wallet.show_events()
    text = capsys.readouterr()
    time = datetime.today().date().isoformat()
    data = (f"""{{'1': {{'Дата': '{time}',
       'Категория': 'Доход',
       'Описание': 'Тест',
       'Сумма': 100}}}}""")
    assert data in text.out
    assert wallet.income == 100
    assert wallet.money == 100
    assert wallet.expenses == 0


def test_clean_event(wallet, event, capsys):
    wallet.clean_wallet()
    wallet.show_events()
    text = capsys.readouterr()
    data = '{}'
    assert data in text.out
    assert wallet.income == 0
    assert wallet.money == 0
    assert wallet.expenses == 0


def test_update_event_same_status(wallet, event, capsys):
    """Тест метода update_event: статус записи не изменяется."""
    wallet.update_event('1', 200, 1, 'Тест2')
    wallet.show_events()
    text = capsys.readouterr()
    time = datetime.today().date().isoformat()
    data = (f"""{{'1': {{'Дата': '{time}',
       'Категория': 'Доход',
       'Описание': 'Тест2',
       'Сумма': 200}}}}""")
    assert data in text.out
    assert wallet.income == 200
    assert wallet.money == 200
    assert wallet.expenses == 0


def test_update_event_changed_status(wallet, event, capsys):
    """Тест метода update_event: статус записи изменяется."""
    wallet.update_event('1', 200, 0, 'Тест2')
    wallet.show_events()
    text = capsys.readouterr()
    time = datetime.today().date().isoformat()
    data = (f"""{{'1': {{'Дата': '{time}',
       'Категория': 'Расход',
       'Описание': 'Тест2',
       'Сумма': 200}}}}""")
    assert data in text.out
    assert wallet.income == 0
    assert wallet.money == -200
    assert wallet.expenses == 200


def test_search_event(wallet, events, capsys):
    """Тест метода search_event."""
    wallet.search_event('Категория', 'ДоХод')
    text = capsys.readouterr()
    time = datetime.today().date().isoformat()
    data = (
       f"{{'Дата': '{time}', 'Категория': 'Доход', 'Сумма': 100, "
       f"'Описание': 'Тест'}}\n"
       f"{{'Дата': '{time}', 'Категория': 'Доход', 'Сумма': 400, "
       f"'Описание': 'Тест3'}}"
    )
    assert data.strip() == text.out.strip()
