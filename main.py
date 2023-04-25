# исходный массив фамилий
first_name = [
    "2_Комарова",
    "5_Леонова",
    "10_Фадеева",
    "6_Соколова",
    "4_Назаров",
    "7_Дроздова",
    "8_Гордеева",
    "3_Смирнов",
    "9_Николаев",
    "1_Калашников",
]

# исходный массив имен
last_name = [
    "2_Варвара",
    "6_Алина",
    "9_Владислав",
    "4_Владислав",
    "5_Анастасия",
    "3_Антон",
    "1_Марк",
    "8_Амелия",
    "7_Василиса",
    "10_София",
]

# исходный массив даты рождения
dat_of_birth = [
    "1_1985",
    "3_1978",
    "4_2001",
    "10_1982",
    "5_1970",
    "6_1990",
    "8_1963",
    "7_2004",
    "2_1996",
    "9_1966",
]

# сортируем массивы по элементу id
first_name.sort(key=lambda id: int(id.split("_")[0]))
last_name.sort(key=lambda id: int(id.split("_")[0]))
dat_of_birth.sort(key=lambda id: int(id.split("_")[0]))

# здесь проходимся по массивам и делим на две части, на ключ и значение массива
for i in range(len(first_name)):
    splitted_first_name = first_name[i].split("_")
    splitted_last_name = last_name[i].split("_")
    splitted_dat_of_birth = dat_of_birth[i].split("_")

    # создал отдельные словари на основании разделения на подмассивы
    first_name_dict = {"id": splitted_first_name[0], "surname": splitted_first_name[1]}
    last_name_dict = {"id": splitted_last_name[0], "name": splitted_last_name[1]}
    dat_of_birth_dict = {
        "id": splitted_dat_of_birth[0],
        "date of birth": splitted_dat_of_birth[1],
    }

    users_array = []  # массив для словаря

    # создаю общий словарь пользовтаеля и указываю формат, в какой виде будет словарь, соотношение ключа и значения
    users_dict = {
        "id": splitted_first_name[0],
        "first_name": splitted_first_name[1],
        "last_name": splitted_last_name[1],
        "date of dirth": splitted_dat_of_birth[1],
    }
    users_array.append(users_dict)
    print(users_array)
