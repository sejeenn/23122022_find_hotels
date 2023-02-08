import sqlite3

my_data = {
    'command': '/lowprice', 'sort': 'PRICE_LOW_TO_HIGH', 'date_time': '07.02.2023 11:06:27', 'chat_id': 732418186,
    'input_city': 'rome', 'destination_id': '553248633938945217', 'quantity_hotels': '3', 'price_min': '30',
    'price_max': '80', 'photo_need': 'yes', 'photo_count': '3', 'checkInDate': {
        'day': '17', 'month': '02', 'year': '2023'}
}

connect = sqlite3.connect('user_input.db')
with connect:
    connect.execute("""
        CREATE TABLE IF NOT EXISTS user_input (
            id integer NOT NULL PRIMARY KEY AUTOINCREMENT,
            command TEXT,
            sort TEXT,
            date_time TEXT,
            chat_id INTEGER
        );
    """)

sql = 'INSERT INTO user_input (id, command, sort, date_time, chat_id) values(?, ?, ?, ?, ?)'
data = [
        (1, my_data['command'], my_data['sort'], my_data['date_time'], my_data['chat_id'])

]
with connect:
    connect.executemany(sql, data)

