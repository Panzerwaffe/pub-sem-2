def test_create(app, client):
    res = client.get('/create')
    assert res.status_code == 200

    data = {"text": "primer"}
    res = client.post('/create', data=data)
    assert res.status_code == 302

