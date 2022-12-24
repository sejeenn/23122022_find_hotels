import datetime

now = datetime.datetime.now().strftime('%Y%m%d')
data = {'command': '/lowprice', 'date_time': '24.12.2022 10:54:51', 'telegram_id': 732418186,
        'chat_id': 732418186, 'input_city': 'rome', 'destination_id': '3023', 'quantity_hotels': '3',
        'price_min': '5', 'price_max': '7', 'photo_need': 'no', 'photo_count': '0',
        'checkInDate': {'day': '24', 'month': '12', 'year': '2022'},
        'checkOutDate': {'day': '31', 'month': '12', 'year': '2022'}}
if data['command'] == '/lowprice':
    data['sort'] = "PRICE_LOW_TO_HIGH"

print(data)
