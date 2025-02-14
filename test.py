from telethon import TelegramClient
import asyncio
from os import getenv
from dotenv import load_dotenv
load_dotenv()
API_ID = getenv('API_ID')  
API_HASH = getenv('API_HASH') 
PHONE_NUMBER = "+77054886530"  
CHAT_USERNAME = "@antilinee"  
MESSAGE_TEXT = "Привет! Это тестовое сообщение от Telethon."


async def main():
    client = TelegramClient("default_session", API_ID, API_HASH)

    await client.start(PHONE_NUMBER)

    await client.send_message(CHAT_USERNAME, MESSAGE_TEXT)
    print(f"✅ Сообщение отправлено в {CHAT_USERNAME}")

    await client.disconnect()

# Запускаем
if __name__ == "__main__":
    asyncio.run(main())


