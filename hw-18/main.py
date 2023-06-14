import json
import yaml
from datetime import date

class Permissions:
    def __init__(self, create=False, read=False, update=False, delete=False):
        self.create = create
        self.read = read
        self.update = update
        self.delete = delete


class Role:
    def __init__(self, name, **kwargs):
        self.name = name
        self.role = {}
        for key, value in kwargs.items():
            self.role[key] = Permissions(**value)

    def __getitem__(self, key):
        return self.role[key]

class Entity:
    def __init__(self, entity_id):
        self._entity_id = entity_id

    @property
    def entity_id(self):
        return self._entity_id

class User(Entity):
    def __init__(self, entity_id, first_name, last_name, fathers_name, date_of_birth, role):
        super().__init__(entity_id)
        self.first_name = first_name
        self.last_name = last_name
        self.fathers_name = fathers_name
        self.date_of_birth = date_of_birth
        self.role = role

    @property
    def age(self):
        today = date.today()
        return today.year - self._date_of_birth.year
    
class Organisation(Entity):
    def __init__(self, entity_id, creation_date, unp, name, role):
        super().__init__(entity_id)
        self.creation_date = creation_date
        self.unp = unp
        self.name = name
        self.role = role

class App(Entity):
    def __init__(self, entity_id, name, role):
        super().__init__(entity_id)
        self.name = name
        self.role = role

#функция для загрузки список пользователей (users) из файла 'users.json'.
def load_users():
    with open('users.json', 'r', encoding="utf8") as f:
        data = json.load(f)
    users = []
    for user_data in data['Users']:
        role_name = user_data.pop('role')
        role_data = roles[role_name]
        role = Role(role_name, **role_data)
        user = User(role=role, **user_data)
        users.append(user)
    return users

#функция для загрузки список организаций (organizations) из файла 'users.json'
def load_organization():
    with open('users.json', 'r', encoding="utf8") as f:
        data = json.load(f)
    organizations = []
    for organization_data in data['Organisations']:
        role_name = organization_data.pop('role')
        role_data = roles[role_name]
        role = Role(role_name, **role_data)
        organization = Organisation(role=role, **organization_data)
        organizations.append(organization)
    return organizations

#функция для загрузки  список ролей (roles) из файла 'roles.yaml'.
def load_roles():
    with open('roles.yaml', 'r', encoding="utf8") as f:
        data = yaml.safe_load(f)
    return data

#функция для загрузки список приложений (apps) из файла 'app.yaml'
def load_apps():
    with open('app.yaml', 'r', encoding="utf8") as f:
        data = yaml.safe_load(f)
    apps = []
    for app_data in data['Apps']:
        role_name = app_data.pop('role')
        role_data = roles[role_name]
        role = Role(role_name, **role_data)
        app = App(role=role, **app_data)
        apps.append(app)
    return apps

# функция добавления нового пользователя
def user_add(first_name, last_name, fathers_name, date_of_birth):
    # Проверка наличия всех данных
    if not all([first_name, last_name, fathers_name, date_of_birth]):
        print("Ошибка: не все данные введены")
        return None
    
    users_sorted = sorted(users, key=lambda x: x.entity_id, reverse=True)
    last_id = users_sorted[0].entity_id if users_sorted else 0
    entity_id = last_id + 1
    role = default_role
    user = User(entity_id=entity_id,
                first_name=first_name,
                last_name=last_name,
                fathers_name=fathers_name,
                date_of_birth=date_of_birth,
                role=role)
    users.append(user)
    print("Пользователь успешно добавлен")
    return user

# Загрузка данных из файлов
roles = load_roles()
default_role_data = roles['default']
default_role = Role('default', **default_role_data)
users = load_users()
organization = load_organization()
apps = load_apps()


new_user = user_add(
         first_name = input("first_name:"),
         last_name = input("last_name:"),
         fathers_name = input("fathers_name:" ),
         date_of_birth = input("date_of_birth:"),

)
if not new_user:
    print("Пользователь не был добавлен")

# Сохранение пользователей и прав доступа в файл new_users.json

# Cоздаем словарь data с тремя ключами: 'Users', 'Organisations' и 'Apps'. Проходимся по всем объектам, которые находятся в списке users + organization + apps. 
# Кпирует их атрибуты в новый словарь d и удаляет из него атрибут role.
# Для каждого объекта получаю имя его роли (role_name) и разрешения, связанные с этой ролью (permissions). 
# Затем преобразую эти разрешения в словарь, где каждый ключ  содержит значение True или False, указывающее, может ли пользователь выполнять соответствующее действие.
# После этого данные о роли (role_data) объединяю с копией атрибутов объекта (d) путем добавления словаря role_data в d под ключом 'role'.
# Добавляю объект в список в data, который соответствует типу.

data = {'Users': [], 'Organisations': [], 'Apps': []}
for obj in (users + organization + apps):
    d = obj.__dict__.copy()
    d.pop('role')
    role_name = obj.role.name
    permissions = obj.role.role.copy()
    permissions_dict = {}
    for k, v in permissions.items():
        permissions_dict[k] = {"create": v.create,
                               "read": v.read,
                               "update": v.update,
                               "delete": v.delete}
    role_data = {"name": role_name, "permissions": permissions_dict}
    d['role'] = role_data
    if isinstance(obj, User):
        data['Users'].append(d)
    elif isinstance(obj, Organisation):
        data['Organisations'].append(d)
    elif isinstance(obj, App):
        data['Apps'].append(d)

with open('all_users.json', 'w', encoding="utf8") as f:
    json.dump(data, f, ensure_ascii=False, indent=3)
