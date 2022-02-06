import asyncio

from pytgcalls import idle

from config import SUPPORT, bot
from config import call_py
from RockUb.quote import arq


async def main():
    await call_py.start()
    await bot.join_chat("Rockerz_Support")            
    await bot.send_message(
            SUPPORT,
            "<b>Congrats!! RoCkErZ🥌 Music Bot has started successfully!</b>",
        )
    print(
        """
    ------------------
   | Userbot Started! POWERED BY @Rockerz_Updates |
    ------------------
"""
    )
    await idle()
    await arq.close()


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
