from p22.web.models import Some
from random import random

def test_edit(app, client):
    """
    В идеале - создавать тестовую БД, заполнять данными через скрипт utils fill_database
    Но для семестровой для тестов достаточно использовать "продакшен" БД
    """
    with app.app_context():
        # берем первый объект из БД и будем использовать его для теста
        initial_obj: Some = Some.query.first()
        if not initial_obj:
            assert False, "Нет ни одной записи в БД"

        data = {'text': str(random())}     # любые данные для POST запроса
        res = client.post(f'/edit/{initial_obj.id}', data=data)

        # ищем вновь наш объект по ID
        updated_obj: Some = Some.query.filter_by(id=initial_obj.id).one()
        # если данные совпадают, значит редактирование прошло успешно
        assert updated_obj.text == data.get('text')

def test_create(app, client):
    # простая провека на успешный возврат страницы
    res = client.get('/create')
    assert res.status_code == 200

    # проверка POST запроса
    data = {"text": "primer"}
    res = client.post('/create', data=data)
    """
    у меня в коде идет редирект, при успешном создании объекта
    в вашем коде, нужно использовать готовые методы в routes для проверки на существование этого объекта в БД!
    пример:
    пост запрос на создание объекта => client.post('/create', data=...)
    проверка, что такой объект создан, у меня это Some => assert Some.query.filter_by(...).one() 
    """
    assert res.status_code == 302



