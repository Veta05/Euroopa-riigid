from module1 import*

countries_dict={"Австрия": "Вена", "Бельгия": "Брюссель", "Великобритания": "Лондон", "Германия": "Берлин", "Ирландия": "Дублин", "Лихтенштейн": "Вадуц", "Нидерладны": "Амстердам", 
           "Франция": "Париж", "Белоруссия": "Минск", "Болгария": "София", "Польша": "Варшава", "Чехия": "Прага", "Албания": "Тирана", "Босния и Герцеговина": "Сараево",
           "Северная Македония": "Скопье", "Сербия": "Белград"}
print(countries_dict )
while True:
    print("Привет! Пройдёмся по странам и их столицам!")
    print("1 - Узнать столицу страны или наоборот,\n2 - Добавить новую страну и столицу,\n3 - Исправить ошибку,\n4 - Проверь свои знания")
    menu=input()
    if menu=="1":
        v=input("Будем искать страну по стoлице(1) или стoлицу по стране(2)? ")
        countries(countries_dict,v)
    elif menu=="2":
        new_key_value(countries_dict)
        