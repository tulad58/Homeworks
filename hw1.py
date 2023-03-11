from pprint import pprint
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
pprint(reciepts, sort_dicts=False)
