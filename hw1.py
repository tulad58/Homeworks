def get_meals_from_file():
    with open('reciepts.txt', encoding="utf-8") as file:
        reciepts = {}
        for line in file:
            meal = line.strip()
            count_ingridients = int(file.readline())
            ingr_list = []
            for _ in range(count_ingridients):
                ingridient, count, measure = file.readline().strip().split(' | ')
                ingridients = {"ingridient": ingridient,
                               "count": int(count),
                               "measure": measure}
                ingr_list.append(ingridients)
            file.readline()
            reciepts[meal] = ingr_list
    return reciepts


def get_shop_list_by_dishes(dishes, person_count):
    reciepts = get_meals_from_file()
    shop_list_by_dishes = {}
    for dish in dishes:
        for _ in range(len(reciepts[dish])):
            some_ingr_name = reciepts[dish][_]['ingridient']
            some_ingr_count = reciepts[dish][_]['count'] * person_count
            some_ingr_measure = reciepts[dish][_]['measure']
            if some_ingr_name not in shop_list_by_dishes:
                shop_list_by_dishes[some_ingr_name] = {"measure": some_ingr_measure, "count": some_ingr_count}
            else:
                some_ingr_count += reciepts[dish][_]['count'] * person_count
                shop_list_by_dishes[some_ingr_name] = {"measure": some_ingr_measure, "count": some_ingr_count}
    return shop_list_by_dishes


get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
