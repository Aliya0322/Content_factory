import asyncio
from telethon import TelegramClient

from config import Config

async def do_post(cfg: Config):
    tele_client = TelegramClient(cfg.session_name, cfg.api_id, cfg.api_hash)
    await tele_client.start()

    await tele_client.disconnect()

async def main():
   cfg = Config()
   print("Бот запустился")

   print("Выполняется поиск...")
   await do_post(cfg)

if __name__ == '__main__':
    asyncio.run((main()))



