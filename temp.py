# import datetime
#
# now = datetime.datetime.now().strftime('%Y%m%d')
# data = {'command': '/lowprice', 'date_time': '24.12.2022 10:54:51', 'telegram_id': 732418186,
#         'chat_id': 732418186, 'input_city': 'rome', 'destination_id': '3023', 'quantity_hotels': '3',
#         'price_min': '5', 'price_max': '7', 'photo_need': 'no', 'photo_count': '0',
#         'checkInDate': {'day': '24', 'month': '12', 'year': '2022'},
#         'checkOutDate': {'day': '31', 'month': '12', 'year': '2022'}}
#
#
# print(data['checkInDate']['day'] + '-' + data['checkInDate']['month'] + '-' + data['checkInDate']['year'])
#
temp = Call
import datetime
year, month, day = datetime.datetime.now().strftime('%Y.%m.%d').split('.')
# print(datetime.datetime(year, month, 1))
now = datetime.datetime.now()
print(datetime.datetime.now().strftime('%Y.%m.%d'))
print(year, month, day)
