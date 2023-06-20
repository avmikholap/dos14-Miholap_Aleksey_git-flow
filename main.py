import json
import yaml
from datetime import date


class Permissions:
    def __init__(self, create=False, read=False, update=False, delete=False):
        self._create = create
        self._read = read
        self._update = update
        self._delete = delete

    @property
    def create(self):
        return self._create

    @property
    def read(self):
        return self._read

    @property
    def update(self):
        return self._update

    @property
    def delete(self):
        return self._delete

    @property
    def get_obj(self):
        return {
            "create": self._create,
            "read": self._read,
            "update": self._update,
            "delete": self._delete,
        }


class Role:
    def __init__(self, name, **kwargs):
        self._name = name
        self._role = {}
        for key, value in kwargs.items():
            self._role[key] = Permissions(**value)

    @property
    def name(self):
        return self._name

    @property
    def role(self):
        return self._role

    def __getitem__(self, key):
        return self._role[key]

    @property
    def get_obj(self):
        permissions = {}
        for key, value in self.role.items():
            permissions[key] = value.get_obj()
        return {"name": self.name, "permissions": permissions}


class Entity:
    def __init__(self, entity_id, role):
        self._entity_id = entity_id
        self._role = role

    @property
    def entity_id(self):
        return self._entity_id

    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, role):
        self._role = role


class User(Entity):
    def __init__(
        self,
        entity_id,
        first_name,
        last_name,
        fathers_name,
        date_of_birth,
        role,
    ):
        super().__init__(entity_id, role)
        self._first_name = first_name
        self._last_name = last_name
        self._fathers_name = fathers_name
        self._date_of_birth = date_of_birth

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    @property
    def fathers_name(self):
        return self._fathers_name

    @property
    def date_of_birth(self):
        return self._date_of_birth

    @property
    def age(self):
        today = date.today()
        return today.year - self._date_of_birth.year

    @property
    def get_obj(self):
        return {
            "entity_id": self._entity_id,
            "first_name": self._first_name,
            "last_name": self._last_name,
            "fathers_name": self._fathers_name,
            "date_of_birth": self._date_of_birth,
            "role": self._role.get_obj,
        }


class Organisation(Entity):
    def __init__(self, entity_id, creation_date, unp, name, role):
        super().__init__(entity_id, role)
        self._creation_date = creation_date
        self._unp = unp
        self._name = name

    @property
    def creation_date(self):
        return self._creation_date

    @property
    def unp(self):
        return self._unp

    @property
    def name(self):
        return self._name

    @property
    def get_obj(self):
        return {
            "entity_id": self._entity_id,
            "role": self._role.get_obj,
            "creation_date": self._creation_date,
            "unp": self._unp,
            "name": self._name,
        }


class App(Entity):
    def __init__(self, entity_id, name, role):
        super().__init__(entity_id, role)
        self._name = name

    @property
    def name(self):
        return self._name

    @property
    def get_obj(self):
        return {
            "entity_id": self._entity_id,
            "role": self._role.get_obj,
            "name": self._name,
        }


# функция для загрузки  список ролей (roles) из файла 'roles.yaml'.
def load_roles():
    with open("roles.yaml", "r", encoding="utf8") as f:
        data = yaml.safe_load(f)
    return data


# функция для загрузки список пользователей (users) из файла 'users.json'.
def load_users():
    with open("users.json", "r", encoding="utf8") as f:
        data = json.load(f)
    users = []
    for user_data in data["Users"]:
        role_name = user_data.pop("role")
        role_data = roles[role_name]
        role = Role(role_name, **role_data)
        user = User(role=role, **user_data)
        users.append(user)
    return users


# функция для загрузки список организаций (organizations) из файла 'users.json'
def load_organization():
    with open("users.json", "r", encoding="utf8") as f:
        data = json.load(f)
    organizations = []
    for organization_data in data["Organisations"]:
        role_name = organization_data.pop("role")
        role_data = roles[role_name]
        role = Role(role_name, **role_data)
        organization = Organisation(role=role, **organization_data)
        organizations.append(organization)
    return organizations


# функция для загрузки список приложений (apps) из файла 'app.yaml'
def load_apps():
    with open("app.yaml", "r", encoding="utf8") as f:
        data = yaml.safe_load(f)
    apps = []
    for app_data in data["Apps"]:
        role_name = app_data.pop("role")
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
    user = User(
        entity_id=entity_id,
        first_name=first_name,
        last_name=last_name,
        fathers_name=fathers_name,
        date_of_birth=date_of_birth,
        role=role,
    )
    users.append(user)
    print("Пользователь успешно добавлен")
    return user


# Загрузка данных из файлов
roles = load_roles()
default_role_data = roles["default"]
default_role = Role("default", **default_role_data)
users = load_users()
organization = load_organization()
apps = load_apps()

# new_user = user_add("Алексей", "Михолап", "Владимирович", "1995")
new_user = user_add(
    first_name=input("first_name:"),
    last_name=input("last_name:"),
    fathers_name=input("fathers_name:"),
    date_of_birth=input("date_of_birth:"),
)

data = {"Users": [], "Organisations": [], "Apps": []}
for obj in users + organization + apps:
    d = {}
    role_name = obj.role.name
    permissions = {k: v.get_obj for k, v in obj.role.role.items()}
    permissions_dict = {}
    if isinstance(obj, User):
        d["entity_id"] = obj.entity_id
        d["first_name"] = obj.first_name
        d["last_name"] = obj.last_name
        d["fathers_name"] = obj.fathers_name
        d["date_of_birth"] = obj.date_of_birth
        data["Users"].append(d)

    elif isinstance(obj, Organisation):
        d["entity_id"] = obj.entity_id
        d["creation_date"] = obj.creation_date
        d["unp"] = obj.unp
        d["name"] = obj.name
        data["Organisations"].append(d)

    elif isinstance(obj, App):
        d["entity_id"] = obj.entity_id
        d["name"] = obj.name
        data["Apps"].append(d)

    for k, v in permissions.items():
        permissions_dict[k] = v

    role_data = {"name": role_name, "permissions": permissions_dict}
    d["role"] = role_data

with open("all_users.json", "w", encoding="utf8") as f:
    json.dump(data, f, ensure_ascii=False, indent=3)
