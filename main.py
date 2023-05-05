import csv
import yaml
import json
from datetime import date


users_csv = []

# открываем файл .csv в режиме чтения
with open("users.csv", "r") as f:
    csv_reader = csv.DictReader(f)
    for row in csv_reader:  # проходимся циклом по файлу и записываем в словарь
        user_csv_dict = {
            "id": int(row["id"]),
            "first_name": row["first_name"],
            "last_name": row["last_name"],
            "fathers_name": row["fathers_name"],
            "date_of_birth": row["date_of_birth"],
        }
        users_csv.append(user_csv_dict)  # добавляем в массив наш словарь

<<<<<<< HEAD
users_array=[] #массив для словаря

# здесь проходимся по массивам и делим на две части, на ключ и значение массива
for i in range(len(first_name)):
    splitted_first_name = first_name[i].split("_")
    splitted_last_name = last_name[i].split("_")
    splitted_dat_of_birth = dat_of_birth[i].split("_")

    # создал отдельные словари на основании разделения на подмассивы
    #first_name_dict = {"id": splitted_first_name[0], "surname": splitted_first_name[1]}
    #last_name_dict = {"id": splitted_last_name[0], "name": splitted_last_name[1]}
    #dat_of_birth_dict = {
    #    "id": splitted_dat_of_birth[0],
    #    "date of birth": splitted_dat_of_birth[1],
    #}


    # создаю общий словарь пользовтаеля и указываю формат, в какой виде будет словарь, соотношение ключа и значения
    users_dict = {
        "id": splitted_first_name[0],
        "first_name": splitted_first_name[1],
        "last_name": splitted_last_name[1],
        "date of dirth": splitted_dat_of_birth[1],
    }
    users_array.append(users_dict)

print(users_array)
=======
users_yaml = []

# открываем файл .yaml в режиме чтения
with open("users.yaml", "r") as f:
    yaml_reader = yaml.load(f, Loader=yaml.FullLoader)
    # проходимся циклом по файлу и записываем в словарь
    for user in yaml_reader["users"]:
        users_yaml_dict = {
            "id": user["id"],
            "first_name": user["first_name"],
            "last_name": user["last_name"],
            "fathers_name": user["fathers_name"],
            "date_of_birth": user["date_of_birth"],
        }
        users_csv.append(users_yaml_dict)  # добавляем в массив наш словарь
#print(users_csv)
# объединяем массивы, через расширение первого списка, вторым списком
#users_csv.extend(users_yaml)

# функция для расчёта возраста
def users_age(year_of_birth):
    today = date.today()
    age = today.year - int(year_of_birth)
    return age


for user in users_csv:
    age = users_age(user["date_of_birth"])
    user["age"] = age

# открываем файл с режимом записи
with open("users.json", "w") as f:
    json.dump(users_csv, f, indent=3, ensure_ascii=False)

# функция добавления нового пользователя
def user_add(first_name, last_name, fathers_name, date_of_birth):
    with open("users.json", "r") as f:
        data_json = json.load(f)
        # Сортирую по id файл, чтобы далее добавлять нового пользовтаеля, отталкиваясь от последнего номера
        data_json.sort(key=lambda id: int(id["id"]))
        create_user = {
            "id": int(data_json[-1]["id"]) + 1,
            "first_name": first_name,
            "last_name": last_name,
            "fathers_name": fathers_name,
            "date_of_birth": date_of_birth,
            "age": users_age(date_of_birth),
        }
        # добавляем пользователя в нашу переменную, которая содержит в себе данные файла
        data_json.append(create_user)

    # открываем файл с режимом записи
    with open("users.json", "w") as f:
        json.dump(data_json, f, indent=3, ensure_ascii=False)


user_add(
    first_name=input("first_name:"),
    last_name=input("last_name:"),
    fathers_name=input("fathers_name:"),
    date_of_birth=input("date_of_birth:"),
)

>>>>>>> feature-hw-17
