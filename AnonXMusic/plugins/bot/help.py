from typing import Union

from pyrogram import filters, types
from pyrogram.types import InlineKeyboardMarkup, Message

from AnonXMusic import app
from AnonXMusic.utils import help_pannel
from AnonXMusic.utils.database import get_lang
from AnonXMusic.utils.decorators.language import LanguageStart, languageCB
from AnonXMusic.utils.inline.help import help_back_markup, private_help_panel
from config import BANNED_USERS, START_IMG_URL, SUPPORT_CHAT
from strings import get_string, helpers


@app.on_message(filters.command(["راهنما"],prefixes=['']) & filters.private & ~BANNED_USERS)
@app.on_callback_query(filters.regex("settings_back_helper") & ~BANNED_USERS)
async def helper_private(
    client: app, update: Union[types.Message, types.CallbackQuery]
):
    is_callback = isinstance(update, types.CallbackQuery)
    if is_callback:
        try:
            await update.answer()
        except:
            pass
        chat_id = update.message.chat.id
        language = await get_lang(chat_id)
        _ = get_string(language)
        keyboard = help_pannel(_, True)
        await update.edit_message_text(
            _["help_1"].format(SUPPORT_CHAT), reply_markup=keyboard
        )
    else:
        try:
            await update.delete()
        except:
            pass
        language = await get_lang(update.chat.id)
        _ = get_string(language)
        keyboard = help_pannel(_)
        await update.reply_photo(
            photo=START_IMG_URL,
            caption=_["help_1"].format(SUPPORT_CHAT),
            reply_markup=keyboard,
        )

@app.on_callback_query(filters.regex("about_text") & ~BANNED_USERS)
@languageCB
async def lispti(client, CallbackQuery, _):
    keyboard = price_back(_)
    print('jere')
    await CallbackQuery.edit_message_text(helpers.about_text, reply_markup=keyboard)



@app.on_message(filters.command(["راهنما"],prefixes=['']) & filters.group & ~BANNED_USERS)
@LanguageStart
async def help_com_group(client, message: Message, _):
    keyboard = private_help_panel(_)
    await message.reply_text(_["help_2"], reply_markup=InlineKeyboardMarkup(keyboard))


@app.on_callback_query(filters.regex("help_callback") & ~BANNED_USERS)
@languageCB
async def helper_cb(client, CallbackQuery, _):
    callback_data = CallbackQuery.data.strip()
    cb = callback_data.split(None, 1)[1]
    keyboard = help_back_markup(_)
    if cb == "play":
        await CallbackQuery.edit_message_text(helpers.help_play, reply_markup=keyboard)
    elif cb == "manage":
        await CallbackQuery.edit_message_text(helpers.help_manage, reply_markup=keyboard)
    elif cb == "auth":
        await CallbackQuery.edit_message_text(helpers.help_auth, reply_markup=keyboard)
