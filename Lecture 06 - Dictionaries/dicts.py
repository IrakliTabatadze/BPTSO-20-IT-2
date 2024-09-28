####################################
# Dict Creation
####################################

# empty_dict = {}
# empty_dict2 = dict()
#
# print(type(empty_dict))
# print(type(empty_dict2))


# filled_dict = {'name': 'John', 'age': 25, 'profession': 'Developer'}
# print(filled_dict['profession'])
# print(filled_dict['age'])
# print(filled_dict['name'])

# filled_dict['courses'] = ['Python', 'Java', 'C++']
# print(filled_dict)
# filled_dict['courses'] = ['Python', 'C++']
# filled_dict['courses'].append('IT Step')
# print(filled_dict)



####################################
# Dict Methods
####################################

# filled_dict = {'name': 'John', 'age': 25, 'profession': 'Developer'}

# print(filled_dict['courses'])
# print(filled_dict.get('names', 'Key doesn\'t exist'))
# print("Hello")

# filled_dict.setdefault('courses', ['Python', 'Java', 'C++'])
# filled_dict.setdefault('courses', 'This is courses')
# print(filled_dict)

# print(filled_dict.keys())

# for key in filled_dict.keys():
#     print(filled_dict[key])

# print(filled_dict.values())


# print(filled_dict.items())

# key, value = ['name', 'John']
# print(key)
# print(value)

# for key, value in filled_dict.items():
#     if key == 'name':
#         print(key, value)




# filled_dict1 = {'name': 'John', 'age': 25, 'profession': 'Developer'}
# filled_dict2 = {'name': 'Kate', 'salary': 1000, 'location': 'New York'}
#
# filled_dict1.update(filled_dict2)
# print(filled_dict1)


# print(filled_dict1.pop('profession'))
# print(filled_dict1.popitem())

# filled_dict1.clear()
# print(filled_dict1)


# filled_dict2 = filled_dict1.copy()
# filled_dict1.clear()
# print(filled_dict1)
# print(filled_dict2)


####################################
# Nested Dicts
####################################

products = {
    'technology': {
        'laptops': {
            '1001': {'brand': 'Apple', 'price': 6000, 'quantity': 2},
            '1002': {'brand': 'HP', 'price': 2000, 'quantity': 10},
        },
        'phones': {
            '2001': {'brand': 'Apple', 'price': 5000, 'quantity': 5},
            '2002': {'brand': 'Samsung', 'price': 3000, 'quantity': 5},
        },
    },
    'clothes': {
        'pants': {
            '3001': {'brand': 'Levi\'s', 'price': 1000, 'quantity': 2},
            '3002': {'brand': 'Lee', 'price': 1000, 'quantity': 2},
        },
        'shirts': {
            '4001': {'brand': 'Adidas', 'price': 5000, 'quantity': 2},
            '4002': {'brand': 'Nike', 'price': 5000, 'quantity': 2},
        }
    }
}

# print(products['technology']['laptops']['1001']['price'])

full_price = 0

for key, value in products.items():
    # print(key, value)
    for key1, value1 in value.items():
        # print(key1, value1)
        for key2, value2 in value1.items():
            # print(key2, value2)
            for key3, value3 in value2.items():
                if key3 == 'quantity':
                    full_price += value2['price'] * value2['quantity']
                if key3 == 'price':
                    full_price += value3
                    print(key3, value3)

print(full_price)