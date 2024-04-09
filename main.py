def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for my_dish in dishes:
        if my_dish in cook_book:
            my_ingredients = cook_book[my_dish]
            for ingredient in my_ingredients:
                name = ingredient['ingredient_name']
                measure = ingredient['measure']
                quantity = int(ingredient['quantity']) * person_count
                if name in shop_list:
                    shop_list[name]['quantity'] += quantity
                else:
                    shop_list[name] = {'measure': measure, 'quantity': quantity}
    return shop_list


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
        cb_ingredients = []

        for value in values:
            ingredient = {}
            value = value.split('|')
            ingredient['ingredient_name'] = value[0]
            ingredient['quantity'] = value[1]
            ingredient['measure'] = value[2]
            cb_ingredients.append(ingredient)
        cook_book[key] = cb_ingredients


result = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
print(result)