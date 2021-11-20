documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
    {"type": "insurance", "number": "12556", "name": "Анастасия Прохорова"},
    {"type": "invoice", "number": "22-5", "name": "Анна Тихоновна"}
]
directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006', '22-5'],
    '3': ['12556']
}

help_doc = '''
p - выводит имя владельца документа по его номеру
s - выводит номер полки хранения по номеру документа
a - добавляет новый документ в список и на полку хранения
l - выводит список всех хранящихся документов
d - удаляет документ из списка по его номеру
m - перемещает документ с одной полки хранения на введенную
as - создает новую полку хранения
sp - выводит все имеющиеся полки с хранящимися внутри документами
e - завершает программу
'''


def people(my_list, document_number):
    for document in my_list:
        if document_number == document["number"]:
            return document["name"]
    return 'Данный документ не обнаружен.'


def number_shelf(my_dict, document_number):
    for key, value in my_dict.items():
        for val in value:
            if document_number == val:
                return key
    return 'Данный документ не обнаружен.'


def save_shelf(document_number, my_dict):
    while True:
        shelf_doc = input('Введите номер полки для хранения: ')
        if shelf_doc in my_dict:
            directories[shelf_doc].append(document_number)
            return 'Запись успешно добавлена!'
        else:
            return f'Введите полку из существующих: {my_dict.keys()}'


def append(my_list, my_dict, document_number, type_document, name_user):
    save_shelf(document_number, my_dict)
    new_entry = {"type": type_document, "number": document_number, "name": name_user}
    my_list.append(new_entry)
    return new_entry


def delete_shelf(document_number, my_dict):
    for key, value in my_dict.items():
        if document_number in value:
            return value.remove(document_number)
    return 'Документ не найден!'


def delete(my_list, my_dict, document_number):
    id = 99
    delete_shelf(document_number, my_dict)
    for id, document in enumerate(my_list):
        if document_number == document["number"]:
            id = id
            my_list.pop(id)
            return 'Документ удален'
    return 'Документ не найден'


def move(my_dict, document_number):
    if delete_shelf(document_number, my_dict) == 'Документ не найден!':
        return 'Документ в перечне отсутствует.'
    else:
        save_shelf(document_number, my_dict)
        return 'Документ перемещен'


def append_shelf(my_dict):
    shelf_new = input('Введите номер новой полки: ')
    if shelf_new in my_dict:
        return 'Данная полка уже существует.'
    else:
        my_dict[shelf_new] = []
        return shelf_new


if __name__ == '__main__':
    while True:
        command = input("Введите команду: ")
        if command == "p":
            document_number = input('Введите номер документа: ')
            print(people(documents, document_number))
        elif command == "s":
            document_number = input('Введите номер документа: ')
            print(number_shelf(directories, document_number))
        elif command == "l":
            for doc in documents:
                print(list(doc.values()))
        elif command == "a":
            document_number = input('Введите номер документа: ')
            type_doc = input('Введите тип документа: ')
            name = input('Введите имя: ')
            print(append(documents, directories, document_number, type_doc, name))
        elif command == "d":
            document_number = input('Введите номер документа: ')
            print(delete(documents, directories, document_number))
        elif command == "m":
            document_number = input('Введите номер документа: ')
            print(move(directories, document_number))
        elif command == "as":
            print(append_shelf(directories))
        elif command == "ps":
            print(directories)
        elif command == "e":
            print('Спасибо за работу. До свидания.')
            break
        else:
            print('Данная команда не существует. Выберите другую команду:')
            print(help_doc)
