from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.filters import Command, CommandStart

router = Router()

@router.message(CommandStart(deep_link=True))
async def main_starterLinker(message: Message, command: CommandStart):
    try:
        type_args = command.args
        message_link = type_args.split('&')
        if message_link:
            if len(message_link) => 1
                for arguments in message_link:

            

        