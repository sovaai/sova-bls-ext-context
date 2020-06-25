from external_modules.context.core import (context_init, context_request, context_event)


async def main(message: dict) -> dict:
    if message['type'] == 'init':
        await context_init(message)
    elif message['type'] == 'request':
        await context_request(message)
    elif message['type'] == 'event':
        await context_event(message)
    return message
