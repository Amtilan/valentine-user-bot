from dataclasses import dataclass
from typing import Optional
from telethon import TelegramClient
from os import getenv
from dotenv import load_dotenv

load_dotenv()


@dataclass
class TelegramConfig:
    api_id: str = getenv('API_ID')
    api_hash: str = getenv('API_HASH')
    bot_token: str = None 
    session_name: str = "default_session"


class TelegramService:
    def __init__(self, config: TelegramConfig):
        self.config = config
        self.client: TelegramClient = None
    async def start(self):
        if self.config.bot_token:
            self.client = await TelegramClient(
                self.config.session_name,
                self.config.api_id,
                self.config.api_hash,
                
            ).start(bot_token=self.config.bot_token)
        else:
            self.client = await TelegramClient(
                self.config.session_name,
                self.config.api_id,
                self.config.api_hash
            ).start()

    async def send_message(self, recipient: str, message: str):
        try:
            await self.client.send_message(recipient, message)
        except Exception as e:
            print(f"Ошибка при отправке сообщения: {e}")

    async def send_file_or_msg(
        self,
        username: str,
        message: str,
        photo_path: Optional[str] = None  
    ):
        try:
            await self.start()
            
            # Красивое оформление валентинки
            decorated_message = (
                "💌 Вам пришла валентинка ! ❤️✨\n"
                "💕 Валентинка 💕\n"
                f"{message}\n"
                "Хочешь радовать и удивлять любимого человека ?"
                "💖 Используй этот сайт, чтобы подарить капельку магии и романтики."
                "https://v0-valentine-9gik5e.vercel.app/"
            )
            
            if photo_path:
                await self.client.send_file(username, photo_path, caption=decorated_message)
                print(f"Фото с подписью отправлено контакту с юзер тегом: {username}")
            else:
                await self.client.send_message(username, decorated_message)
                print(f"Текстовое сообщение отправлено контакту с юзер тегом: {username}")
        
        except Exception as e:
            print(f"Ошибка при работе с контактом: {e}")
        
        finally:
            await self.client.disconnect()
