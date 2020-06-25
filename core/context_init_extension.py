from external_modules.context.models import (Chat, Infs)
import logging
import tortoise


async def context_init(message):
    """
            1. Если данный инф не найден то выходим из обработки сразу.
            2. Если передавался индефикатор чата, то проверяем есть ли он базе. Если нет выходим
            3. Если индефикатор чата не передавался, то создаем его для инфа.
        :return:
    :param message:
    :return:
    """
    if message.get('uuid') is None:
        message['error'] = {"error": "There is not set uuid"}
        return message
    try:
        inf = await Infs.get(uuid=message['uuid'])
        logging.debug(f"Inf нашли при инциализации {inf}")
    except tortoise.exceptions.DoesNotExist as err:
        message['error'] = {"error": f"uuid {err.__str__()}"}
        return message

    if message.get('cuid'):
        try:
            chat = await Chat.get(inf=inf, cuid=message.get('cuid'))
            message['cuid'] = str(chat.cuid)
        except tortoise.exceptions.DoesNotExist as err:
            message['error'] = {"error": f"ciud {err.__str__()}"}
            return message
    else:
        try:
            chat = Chat(inf=inf)
            await chat.save()
            message['cuid'] = str(chat.cuid)
        except tortoise.exceptions.DoesNotExist as err:
            logging.error(f"Ошибка при создании чата {err}")
            message['error'] = {"error": err.__str__()}
            return message
    return message