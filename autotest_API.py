import create_order_and_receiving_track

# Сергей Пронькин, 10-я когорта — Финальный проект. Инженер по тестированию плюс
def test_create_order():
    response = create_order_and_receiving_track.get_receiv_order(str)
    assert response.status_code == 200
