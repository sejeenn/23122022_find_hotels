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
        CREATE TABLE USER (
            id integer NOT NULL PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER
        );
    """)

sql = 'INSERT INTO USER (id, name, age) values(?, ?, ?)'
data = [
        (1, 'Alice', 21), 
        (2, 'Bob', 22),
        (3, 'Chris', 23)
]
with connect:
    connect.executemany(sql, data)

