def search_person(id): # кукла функуции берущей id vk и отдающей список id vk подобных персонажей (для закидывания в базу на рассмотрение)
   new_id = (id, '123453', '23456', '36812', '23145', '76237')
   return new_id

def users_DB(id, status_code): #add_persons() Функция добавляет в БД найденных "персонажей"
    pass

def get_user_fromDB(): #post_user() Функция возвращает id случайного (можно и не случайного) "персонажа"
    pass    # Условие, функция при последующем вызове возвращает нового пользователя с статусом 0

def restatus(id, num_status): # Функция меняет у пользователя с переданным id статус код на указанный num_status
    pass

# Примечание, после функции указано альтернативное название функции