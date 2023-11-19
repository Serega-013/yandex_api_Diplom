import requests
import configuration
import data


#Создание заказа
def create_order():
    return requests.post(url=configuration.URL + configuration.CREATE_ORDER, json=data.create_body).status_code


#Сохранение номера заказа
def ger_track():
    track_order = create_order.json()['trak']
    return track_order


#Получение заказа
def get_receiv_order(track_order):
    return requests.get(configuration.URL + configuration.CREATE_RECEIVING + str(track_order))


print(get_receiv_order(str))
