cook_book = {}
with open('test.txt') as f:
    # Читаем файл test.txt и возвращаем список
    data = f.read().split('\n\n')
    for food in data:
        # Сохраняем в переменную key название блюда по индексу и возвращаем список
        key = food.split('\n')[0]
        # Сохраняем в переменную values ингредиенты, количество, единицу измерения и возвращаем список
        values = food.split('\n')[2:]
        # Создаем список ингредиентов
        cb_ingridients = []

        for value in values:
            ingridient = {}
            value = value.split('|')
            ingridient['ingridient_name'] = value[0]
            ingridient['quantity'] = value[1]
            ingridient['measure'] = value[2]
            cb_ingridients.append(ingridient)
        cook_book[key] = cb_ingridients

print(cook_book)
