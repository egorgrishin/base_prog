""" Форум. Удаление ветви """


def setMessages():
    """ Возвращает словарь - таблицу сообщений """
    messages = {}

    for i in range(messages_count):
        temp = list(map(int, input().split()))
        if temp[1] in messages.keys():
            messages[temp[1]].append(temp[0])
        else:
            messages[temp[1]] = [temp[0]]

    return messages


def deleteMessages(messages, message_number, deleted_count):
    """ Рекурсивно удаляет сообщения, принадлежащие данному """
    if message_number in messages.keys():
        for i in messages[message_number]:
            deleted_count = deleteMessages(messages, i, deleted_count) + 1
    return deleted_count


messages_count = int(input('Введите количество сообщений на форуме >> '))
messages = setMessages()
message_number = int(input('Удалить сообщение с номером >> '))
deleted_count = deleteMessages(messages, message_number, 0)
print(deleted_count)
