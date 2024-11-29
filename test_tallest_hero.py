import pytest
import requests
from tallest_hero import get_tallest_hero


# Тест для нахождения самого высокого мужского героя с работой
def test_get_tallest_hero_valid_male_with_work():
    result = get_tallest_hero("Male", True)
    # Проверка на наличие ошибки
    if "error" in result:
        assert result == {"error": "Герои, соответствующие критериям, не найдены"}, \
            "Ожидается сообщение об ошибке при отсутствии подходящих героев"
    else:
        # Проверка на пол и наличие профессии
        assert result["appearance"]["gender"] == "Male", "Пол героя должен быть 'Male'"
        assert result["work"]["occupation"], "У героя должна быть профессия"


# Тест для нахождения самого высокого мужского героя без работы
def test_get_tallest_hero_valid_male_without_work():
    result = get_tallest_hero("Male", False)

    # Проверка на наличие ошибки (если она есть)
    if "error" in result:
        assert result == {"error": "Герои, соответствующие критериям, не найдены"}, \
            "Ожидается сообщение об ошибке при отсутствии подходящих героев"
    else:
        # Проверка на пол и отсутствие профессии
        assert result["appearance"]["gender"] == "Male", "Пол героя должен быть 'Male'"
        assert not result["work"]["occupation"], "У героя не должно быть профессии"


# Тест для нахождения самого высокого женского героя с работой
def test_get_tallest_hero_valid_female_with_work():
    result = get_tallest_hero("Female", True)

    # Проверка, если ошибка
    if "error" in result:
        assert result == {"error": "Герои, соответствующие критериям, не найдены"}, \
            "Ожидается сообщение об ошибке при отсутствии подходящих героев"
    else:
        # Проверки на пол и наличие профессии
        assert result["appearance"]["gender"] == "Female", "Пол героя должен быть 'Female'"
        assert result["work"]["occupation"], "У героя должна быть профессия"


# Тест для нахождения самого высокого женского героя без работы
def test_get_tallest_hero_valid_female_without_work():
    result = get_tallest_hero("Female", False)

    # Проверка, если ошибка
    if "error" in result:
        assert result == {"error": "Герои, соответствующие критериям, не найдены"}, \
            "Ожидается сообщение об ошибке при отсутствии подходящих героев"
    else:
        # Проверки на пол и отсутствие профессии
        assert result["appearance"]["gender"] == "Female", "Пол героя должен быть 'Female'"
        assert not result["work"]["occupation"], "У героя не должно быть профессии"


# Тест для случая, когда пол не указан (gender == '-') с работой
def test_get_tallest_hero_gender_dash_with_work():
    result = get_tallest_hero("-", True)

    # Проверка на наличие ошибки (если она есть)
    if "error" in result:
        assert result == {"error": "Герои, соответствующие критериям, не найдены"}, \
            "Ожидается сообщение об ошибке при отсутствии подходящих героев"
    else:
        # Проверки на наличие работы и на пол
        assert result["appearance"]["gender"] == "-", "Пол героя должен быть '-'"
        assert result["work"]["occupation"], "У героя должна быть профессия"


# Тест для случая, когда пол не указан (gender == '-') без работы
def test_get_tallest_hero_gender_dash_without_work():
    result = get_tallest_hero("-", False)

    # Проверка на наличие ошибки (если она есть)
    if "error" in result:
        assert result == {"error": "Герои, соответствующие критериям, не найдены"}, \
            "Ожидается сообщение об ошибке при отсутствии подходящих героев"
    else:
        # Проверки на отсутствие работы и на пол
        assert result["appearance"]["gender"] == "-", "Пол героя должен быть '-'"
        assert not result["work"]["occupation"], "У героя не должно быть профессии"

