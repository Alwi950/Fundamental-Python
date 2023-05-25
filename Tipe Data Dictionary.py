'''
Tipe Data Dictionary
'''

Users= {
    'id': 1,
    'name': 'Alexander Messi',
    'username': 'Messi',
    'email': 'messi@barca.sp',
    'address': {
      'street': 'Kulas Light',
      'suite': 'Apt. 556',
      'city': 'Gwenborough',
      'zipcode': '92998-3874',
      'geo' : {
        'lat': '-37.3159',
        'lng': '81.1496'
      }
    }
}


print(Users)
print(Users['id'])
print(Users['name'])
print(Users['username'])
print(Users['email'])
print(f"Jalan: {Users['address']['street']}")