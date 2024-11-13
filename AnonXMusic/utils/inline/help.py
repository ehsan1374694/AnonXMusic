from typing import Union

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from AnonXMusic import app


def help_pannel(_, START: Union[bool, int] = None):
    first = [InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data=f"close")]
    second = [
        InlineKeyboardButton(
            text=_["BACK_BUTTON"],
            callback_data=f"settingsback_helper",
        ),
    ]
    mark = second if START else first
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="📗 پخش موزیک",
                    callback_data="help_callback play",
                ),
                InlineKeyboardButton(
                    text="📕 مدیریت پلیر",
                    callback_data="help_callback manage",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="📘 دسترسی پلیر",
                    callback_data="help_callback auth",
                ),
              
            ],
            
            mark,
        ]
    )
    return upl


def price_back(_):

    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["BACK_BUTTON"],
                    callback_data=f"settingsback_helper",
                ),
            ]
        ]
    )
    return upl

def help_back_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["BACK_BUTTON"],
                    callback_data=f"settings_back_helper",
                ),
            ]
        ]
    )
    return upl


def private_help_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_4"],
                url=f"https://t.me/{app.username}?start=help",
            ),
        ],
    ]
    return buttons
