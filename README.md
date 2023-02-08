# Документация к VKinderBot:
### VKinderAPI - модуль для взаимодейстсвия с VK API и получения информации о пользователях включая фотографии на их страницах.

```python

class VKinderAPI.VKinderAPI(token=TOKEN_VK_API)

```

### Параметры:
* token(str) - Токен приложения необходимый для работы с VK API.

### Методы:
```python
VKinderAPI.get_myself(id) - Метод get_myself(id) получает на вход id пользователя VK. На выходе определяет пол, дату рождения и город пользователя. Метод возвращает имя переданного пользователя.
```

```python
VKinderAPI._get_users() - Метод _get_users() является приватным. Возвращает список словарей с размером в 1000 пользователей в соответсвии с параметрами полученными после вызова метода get_myself()
```

```python
VKinderAPI.get_photos(user: dict) - Метод get_photos() принимает словарь одного пользователя, которого мы можем получить при вызовае функции _get_users(). Возвращает словарь {'url': link, 'id': id, 'owner_id': owner_id, 'likes': likes} для получения фотографии пользователя.
```

```python
VKinderAPI._sorted_photo(self, photos_info: list) - Метод _sorted_photo() является приватным. Принимает словарь метода get_photos(). Возвращает отсортированные список фотографии пользователя по лайкам.
```

### VkBot(VKinderAPI) - модуль для взаимодействия с группой VK. Для работы необходимо объявить VKinderAPI с TOKEN_VKAPI.

```python

class VkBot.VkBot(token=TOKEN_BOT)

```

### Параметры:
* token(str) - Токен группы VK от именни которой будет рабоать бот.

### Методы:
```python
VkBot.run() - Метод запускающий в работу бота на прослушивание личных сообщений и реакции на переданные команды.
```

### Команды бота:
* /старт (старт) - команда запускает первое взаимодесвтие с пользователем вконтакте. Бот запоминает id пользователя обращения и получает необходимые данные для работы VKinderAPI;
* /показать (показать) - команда призывает бота вывести первого пользователя из списка пользователей выводя его ссылку на страницу ВК, имя и фамилию, три самые популярные фотографии;
* /далее (далее) - команда показывает следующего пользователя с данными и фотографиями;
* /добавить (добавить) - команда просит бота запомнить последнего выведенного пользователя. Получить список добавленных пользователей можно через команду /история (история);
* /убрать (убрать) - команда просит бота убрать последнего пользователя из списка пользователей, чтобы больше с этим пользователем не взаимодействовать;
* /история (история) - команда просит бота вывести ссылки на страницы всех пользователей которых мы добавили и не внесли в список убранных.