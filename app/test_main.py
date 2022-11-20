"""тесты для генератора приветствий."""
import pytest
from main import greeting


@pytest.mark.parametrize(
    'name,expected',
    [
     ('Никита', 'Привет, Никита'), ('Ольга', 'Привет, Ольга'),
    ])
def test_greeting(name: str, expected: str):
    """Текст приветствия зависит от имени.

    Args:
        name (str): Имя пользователя
        expected (str): Текст приветствия

    Raises:
        RuntimeError: if greeting(name) != expected
    """
    if greeting(name) != expected:
        raise RuntimeError


def test_capitalize():
    """Все слова в имени начинаются с большой буквы.

    Raises:
        RuntimeError: if greeting(name) != 'Привет, Яндекс Практикум'
    """
    name = 'яндекс практикум'
    if greeting(name) != 'Привет, Яндекс Практикум':
        raise RuntimeError
