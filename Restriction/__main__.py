import asyncio
import importlib
from pyrogram import idle
from Restriction.modules import ALL_MODULES


# ----------------------------Bot-Start---------------------------- #


async def sumit_boot():
    for all_module in ALL_MODULES:
        importlib.import_module("Restriction.modules." + all_module)
    print("»»»» ʙᴏᴛ ᴅᴇᴘʟᴏʏ sᴜᴄᴄᴇssғᴜʟʟʏ ✨ 🎉")
    await idle()
    print("»» ɢᴏᴏᴅ ʙʏᴇ ! sᴛᴏᴘᴘɪɴɢ ʙᴏᴛ.")


if __name__ == "__main__":
    asyncio.run(sumit_boot())

# ------------------------------------------------------------------ #
