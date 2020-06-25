import logging
from external_modules.context.models import Chat


async def store(message: dict):
    logging.debug(f"Store message {message}")
    chat = await Chat.get(cuid=message['cuid'])
    chat.context = message['context']
    if message['type'] == 'request':
        chat.technical_context = {"last_response": {
            "text": message['response']['text'],
            "cntx": message['technical_info']['resp_cntx']
        }
    }
    await chat.save()