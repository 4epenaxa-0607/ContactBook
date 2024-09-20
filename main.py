import random
import pickle
import os

Contact = {
    'id': 1,
    'name': 'Smith Adam',
    'phone': 123456,
    'email': 'adam@testmail.test',
}

Contact_list = [Contact]

Storage_filename = "storage.pickle"

if not os.path.exists(Storage_filename):
    with open(Storage_filename, "wb") as f:
        pickle.dump(Contact_list, f)
else:
    with open(Storage_filename, "rb") as f:
        Contact_list = pickle.load(f)


def spam(contact_list: list, all_contact: bool):
    if all_contact == 1:
        for i in contact_list:
            print('Call on ', i['phone'])

    elif all_contact == 0:
        count_number = random.randint(0, contact_list.count() - 1)
        while count_number >= 0:
            rnd_number = random.randint(0, contact_list.count() - 1)
            print('Call on ', contact_list[rnd_number]['phone'])
            count_number -= 1


def get_phone(name: str):
    for i in Contact_list:
        if name in i['name']:
            print(i['name'], i['phone'])


def add_contact(name: str, phone: int, email: str | None):
    rnd_id = random.randrange(1000000)
    while True:
        if any(rnd_id == i['id'] for i in Contact_list):
            rnd_id = random.randrange(1000000)
        else:
            new_contact = {
                'id': rnd_id,
                'name': name,
                'phone': phone,
                'email': email or None,
            }
            Contact_list.append(new_contact)
            with open(Storage_filename, "wb") as f:
                pickle.dump(Contact_list, f)
            break


def remove_contact(id: int):
    for i in Contact_list:
        if id == i['id']:
            Contact_list.remove(i)
            with open(Storage_filename, "wb") as f:
                pickle.dump(Contact_list, f)


def control():
    print('Список команд:')
    print('1) Спам')
    print('2) Найти контакт')
    print('3) Добавить контакт')
    print('4) Удалить контакт')
    print('5) Посмотреть контакты')

    while 1:
        try:
            number_command = int(input('\nВведите номер команды: '))
        except:
            print('Некоректный ввод')
            control()

        if number_command == 1:
            try:
                bool_spam = bool(input('Спамить на все номера? (1 - да / 0 - нет) (введите число): '))
                spam(Contact_list, bool_spam)
            except:
                print('Некоректный ввод')
                control()
        elif number_command == 2:
            try:
                name_contact = input('Имя контакта: ')
                get_phone(name_contact)
            except:
                print('Некоректный ввод')
                control()
        elif number_command == 3:
            try:
                name_contact = input('Введите имя контакта (обязательно): ')
                phone_contact = int(input('Введите номер контакта (обязательно): '))
                email_contact = input('Введите email контакта (не обязательно): ')
                add_contact(name_contact, phone_contact, email_contact)
                print('Контакт создан')
            except:
                print('Некоректный ввод')
                control()
        elif number_command == 4:
            try:
                id_contact = int(input('Введите id контакта: '))
                remove_contact(id_contact)
                print('Контакт удален')
            except:
                print('Некоректный ввод')
                control()
        elif number_command == 5:
            print(Contact_list)


control()