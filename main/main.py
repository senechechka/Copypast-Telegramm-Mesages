import asyncio
from aiogram import Bot, Dispatcher
from handlers import common, settings
import config

async def main():
    bot = Bot(token=config.MAIN_BOT_TOKEN)
    dp = Dispatcher()
    dp.include_routers(common.router, settings.router)

    try:
        await dp.start_polling(bot, skip_updates=True)
    except Exception:
        pass

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        pass
