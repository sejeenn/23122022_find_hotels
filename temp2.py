import json

with open('get_summary.json', 'r', encoding='utf-8') as f:
    data = json.load(f)


    hotel_data = {
        'id': data['data']['propertyInfo']['summary']['id'], 'name': data['data']['propertyInfo']['summary']['name'],
        'address': data['data']['propertyInfo']['summary']['location']['address']['addressLine'],
        'coordinates': data['data']['propertyInfo']['summary']['location']['coordinates']
                  }
    hotel_images = {}
    count_img = 0
    for i in data['data']['propertyInfo']['propertyGallery']['images']:
        hotel_images[count_img] = i['image']['url']
        count_img += 1
