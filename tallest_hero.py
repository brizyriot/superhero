import requests


def get_tallest_hero(gender: str, has_work: bool) -> dict:
    """
    Функция для получения самого высокого супергероя из API,
    отфильтрованного по полу и наличию работы.

    :param gender: Пол героя ("Male" или "Female").
    :param has_work: Наличие профессии (True, если должна быть профессия; False — если нет).
    :return: Данные самого высокого героя (dict) или сообщение об ошибке.
    """
    # URL для получения списка героев
    url = "https://akabab.github.io/superhero-api/api/all.json"

    # Отправляем GET-запрос для получения данных об героях
    response = requests.get(url)
    response.raise_for_status()  # Проверяем, успешно ли выполнен запрос
    heroes = response.json()  # Преобразуем ответ в формат JSON

    # Фильтруем список героев по заданным критериям
    filtered_heroes = [
        hero for hero in heroes
        if hero.get("appearance", {}).get("gender") == gender  # Пол совпадает
           and bool(hero.get("work", {}).get("occupation")) == has_work  # Проверяем наличие работы
    ]

    # Если подходящих героев не найдено, возвращаем сообщение об ошибке
    if not filtered_heroes:
        return {"error": "Герои, соответствующие критериям, не найдены"}

    # Ищем самого высокого героя из отфильтрованного списка
    tallest_hero = max(
        filtered_heroes,
        key=lambda x: x.get("appearance", {}).get("height", [0])[1] or 0  # Берём второй элемент height
    )
    return tallest_hero  # Возвращаем данные самого высокого героя
