from app import Figure  # Замість цього використовуйте правильний шлях до файлу
import pytest


def test_get_angles():
    """Тестуємо чи правильно повертається кількість кутів фігури."""
    fig = "трикутник"
    triangle = Figure(fig, 1)
    assert triangle.get_angles == 3, f"У {fig} є 3 кути!"
