from pyrogram import filters
from pyrogram.types import Message

from AnonXMusic import app
from AnonXMusic.core.call import Anony
from AnonXMusic.utils.database import set_loop
from AnonXMusic.utils.decorators import AdminRightsCheck
from AnonXMusic.utils.inline import close_markup
from config import BANNED_USERS



@app.on_message(
    filters.command(["اتمام", "اتمام", "cend", "cstop"],prefixes=['']) & filters.group & ~BANNED_USERS
)
@AdminRightsCheck
async def stop_music(cli, message: Message, _, chat_id):
    if not len(message.command) == 1:
        return
    await Onix.stop_stream(chat_id)
    await set_loop(chat_id, 0)
    await message.reply_text(
        _["admin_5"].format(message.from_user.mention), reply_markup=close_markup(_)
    )

@app.on_message(
    filters.command(["شارژ"],prefixes=['']) & filters.group & ~BANNED_USERS
)
async def group_charge(cli, message: Message, _, chat_id):
    if not len(message.command) == 1:
        return
    month = message.command[1]
    print('month',month)
    await message.reply_text(
        f"گروه با موفقیت {month} روز شارژ شد ."
    )
