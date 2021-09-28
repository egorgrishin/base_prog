def get_hash_text(surname, name, email):
    min_len = 5

    data = get_data(surname, name, email)
    data = get_transform_data(data, min_len)

    return (data[0] + data[1] * 2 + data[2] * 3).lower()


def get_data(surname, name, email):
    return [
        {
            'text': surname,
            'len': len(surname),
        },
        {
            'text': name,
            'len': len(name),
        },
        {
            'text': email,
            'len': len(email),
        },
    ]


def get_transform_data(data, minLen):
    new_data = []

    for element in data:
        if element['len'] < minLen:
            need_symbols = minLen - element['len']
            element['text'] = 'n' * need_symbols + element['text']
        else:
            element['text'] = element['text'][0: minLen]

        new_data.append(element['text'])

    return new_data


surname = input("Введите вышу фамилию >> ")
name = input("Введите ваше имя >> ")
group = input("Введите вашу группу >> ")
print('Привет,', surname, name, 'из группы', group)

email = input("Введи свою электронную почту? ")

print(get_hash_text(surname, name, email))
