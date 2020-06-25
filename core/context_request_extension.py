import logging
from external_modules.context.models import (Infs, Chat)
import tortoise


async def context_request(message):

    logging.debug(f"Обработка сообщения внутри внешнего модуля для контекста {message}")
    try:
        chat = await Chat.get(cuid=message.get("cuid")).prefetch_related('inf')
        logging.debug(f"Get inf infomation {dir(chat.inf)} chat.inf.inf_profile {chat.inf.inf_profile}")
        tmp_dict = {
            "session_id": chat.id,
            "inf_id": chat.inf.id,
            "inf_profile": chat.inf.inf_profile,
            "technical_context": chat.technical_context,
        }
        message['technical_info'].update(tmp_dict)
        message['db_context'] = chat.context

    except tortoise.exceptions.DoesNotExist as err:
        message['error'] = {"error": f" Chat {err}"}
        return message

    logging.debug(f"Нашли чат {chat.__dict__}")
    return message
