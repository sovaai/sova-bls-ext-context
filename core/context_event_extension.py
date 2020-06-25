import logging
from external_modules.context.models import (Chat,)
import tortoise


async def context_event(message):

    logging.debug(f"Происходит обработка внутри внешнего модуля для контекста {message}")
    try:
        chat = await Chat.get(cuid=message.get("cuid")).prefetch_related('inf')
        message['technical_info'].update({
            "session_id": chat.id,
            "inf_id": chat.inf.id,
            "technical_context": chat.technical_context,
            "inf_profile": chat.inf.inf_profile
        })
        message['db_context'] = chat.context
        logging.debug(f"Get inf infomation {chat.__dict__} chat.inf.inf_profile {chat.inf.inf_profile}")
    except tortoise.exceptions.DoesNotExist as err:
        message['error'] = {"error": f" Chat {err}"}
        return message

    logging.debug(f"Нашли чат {chat.__dict__}")
    return message
