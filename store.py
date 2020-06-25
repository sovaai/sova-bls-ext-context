from external_modules.context.core import (store,)


async def save(message: dict) -> dict:
    await store(message)
    return message
