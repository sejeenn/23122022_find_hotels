any_dict = {'12345': {'any_key': 123, 'and_key': 456, 'and_key3': 789}}
link = ['www.ya.ru', 'www.github.com']
any_dict['654'] = {'any': 123, 'and': 456, 'key3': 789}
any_dict['12345']['link'] = link

print(any_dict)