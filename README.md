
## Homework 26 ##
* Добавить в ваше приложение URI /api/v1/<имя сервиса>/health_check которое просто отдаёт 200 на любой GET запрос
* С помощью docker-compose настроить связку nginx -> наш сервис
  • nginx должен быть доступен на 80 порту сервера и проксировать все запросы на наш сервис
  • при запросе на /api/v1/<имя сервиса>/health_check nginx не должен писать никаких логов
* Логи  nginx надо писать в json формате. Со следующей информацией
  *  host
  * ip address с которого послали запрос
  * статус запроса (200,400,500...)
  * размер тела запроса
  * user agent
  * cам запрос (GET / HTTP/1.1)
  * cколько всего запрос занял времени
  * сколько отвечал на запрос наш сервис

## Homework 25 ##
* Cоздать Dockerfile для нашего приложения (процесс в контейнере должен выполнятся не от root)
* Build/Push образа на dockerhub
* Cоздать docker-compose файл который запускает наше приложение
* Переписать ansible role на запуск приложения через docker-compose



## Homework 20-22 ##
* Задеплоить ваше приложение (authn/authz/bank) на Ubuntu 22.04 c помощью ansible
* Создать пользователя authn/authz/bank
* Установить git, 2.40.1
* Установить python 3.11
* Установить poetry
* Склонить репозиторий 
* poetry install
* poetry run flask —app main.py run
* Cделать с помощью Ansible  роль которая устанавливает Docker на Ubuntu 22.04


## Homework 19 ##
* Переименовываем entity_id в client_id во всех классах
* Переименовываем class Entity в Client
* Прочитать данные из файлов users.json, apps.yaml, roles.yaml и создать на основании их объекты 
* Устанавливаем Flask через poetry
* Наш сервис должен иметь следующий http интерфейс
  * GET /api/v1/users/<client_id> - получить данные о пользователе
    * Перед тем как получить данные посмотреть есть ли у пользователя права на чтение users
      * Найти заголовок token
        * Если его нет ошибка 400 {"status": "error", "message": f"Token header not found"}
      * В заголовке должен быть json {"client_id": <client_id>}
      * По id найти объект и проверить есть ли у роли такой доступ
    * Если не нашли пользователя с таким client_id то возвращаем {"status": "error", "message": f"No user with id = {client_id}"}
  * GET /api/v1/organisations/<client_id> - получить данные об организации 
    * Перед тем как получить данные посмотреть есть ли у пользователя права на чтение organisations
      * Найти заголовок token
        * Если его нет ошибка 400 {"status": "error", "message": f"Token header not found"}
      * В заголовке должен быть json {"client_id": <client_id>}
      * По id найти объект и проверить есть ли у роли такой доступ
    * Если не нашли организацию с таким client_id то возвращаем {"status": "error", "message": f"No organisation with id = {client_id}"}
  * GET /api/v1/users - получить данные о всех пользователях
    * Перед тем как получить данные посмотреть есть ли у пользователя права на чтение users
      * Найти заголовок token
        * Если его нет ошибка 400 {"status": "error", "message": f"Token header not found"}
      * В заголовке должен быть json {"client_id": <client_id>}
      * По id найти объект и проверить есть ли у роли такой доступ
  * GET /api/v1/organisations - получить данные о всех организациях
    * Перед тем как получить данные посмотреть есть ли у пользователя права на чтение organisations
      * Найти заголовок token
        * Если его нет ошибка 400 {"status": "error", "message": f"Token header not found"}
      * В заголовке должен быть json {"client_id": <client_id>}
      * По id найти объект и проверить есть ли у роли такой доступ
  * PUT /api/v1/users - создать пользователя используя {"first_name": "...", "role": "...", "last_name": "...", "fathers_name": "...", "date_of_birth": "..."}
    * Перед тем как получить данные посмотреть есть ли у пользователя права на запись users
      * Найти заголовок token
        * Если его нет ошибка 400 {"status": "error", "message": f"Token header not found"}
      * В заголовке должен быть json {"client_id": <client_id>}
      * По id найти объект и проверить есть ли у роли такой доступ
    * Пишем в файл users.json
  * PUT /api/v1/organisations - создать организацию используя {"role": "", "creation_date": "", "unp": "", "name": ""}
    * Перед тем как получить данные посмотреть есть ли у пользователя права на запись organisations
      * Найти заголовок token
        * Если его нет ошибка 400 {"status": "error", "message": f"Token header not found"}
      * В заголовке должен быть json {"client_id": <client_id>}
      * По id найти объект и проверить есть ли у роли такой доступ
    * Пишем в файл users.json
  * GET /api/v1/credits/authz/{create,read,update,delete}
  * GET /api/v1/deposits/authz/{create,read,update,delete}
  * GET /api/v1/debitaccounts/authz/{create,read,update,delete}
  * GET /api/v1/creditaccounts/authz/{create,read,update,delete}
  * GET /api/v1/users/authz/{create,read,update,delete}
  * GET /api/v1/organisations/authz/{create,read,update,delete}
  * GET /api/v1/identities/authz/{create,read,update,delete}
    * Для каждого из этих URI
      * Найти заголовок token
        * Если его нет ошибка 400 {"status": "error", "message": f"Token header not found"}
      * В заголовке должен быть json {"client_id": <client_id>}
      * По id найти объект и проверить есть ли у роли такой доступ
      * Если есть 200 и {"status": "success", "message": "authorized"}
        * Если нет или, что то пошло не так то  403 {"status": "error", "message": "not authorized"}

## Homework 18 ##
* Создать класс Permissions
  * cоздать boolean свойства на чтение запись - create,read,update,delete
* Cоздать класс Role
  * создать свойство только на чтение строку name
  * cоздать свойство role которое является словарём где ключ
    имена наших классов выполняющие бизнес логику (Credit,Deposit,DebitAccount,CreditAccount,User,Organisation,Identity)
    а значение объекты Permissions
  ** Либо класс Role должен принемать как ключ имена выше указанных классов и выдовать 
     в качестве значений объекты Permissions
     >> a = Role("default",**dict_with_permissions)
     >> a.name
     default
     >> a["Credit].create
     False
     >> a["DebitAccount"].update
     False
* Создать класс Entity
  * Создать свойство только на чтение - entity_id (оно должно быть int)
  * Cоздать свойcтво на чтение/запись - role с типом Role.
* Создать класс User
  * Унаследоваться от Entity
  * добавить свойства только на чтение first_name, last_name, fathers_name, date_of_birth
  * добавить свойство только на чтение age, которое высчитывается из date_of_birth
* Создать класс Organisation
  * Унаследоваться от Entity
  * добавить свойства creation_date, unp, name
* Создать класс App
  * Унаследоваться от Entity
  * добавить свойства name
* Прочитать данные из файлов users.json, apps.yaml, roles.yaml и создать на основании их объекты
* В функции сreate_user из предыдущего задания создаём не словарь а объект
