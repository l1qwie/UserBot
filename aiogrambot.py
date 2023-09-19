from aiogram import Bot, Dispatcher, Router, types
import asyncio
from aiogram.utils.markdown import hlink
from aiogram.types import BufferedInputFile
import db
import userbot

TOKEN = "5898243671:AAEgODtzGWkIHW3Sf5kBdY0QrLdzLKsHq9o"

bot = Bot(token=TOKEN)
dp = Dispatcher()
router = Router()

def Namer(name: str, nick: str) -> str:
    return hlink(name, nick)



@router.message()
async def all_mes(message: types.Message):
    db.ConnectTo("..\\bot_user\\database.db")
    if message.text == '/reset':
        db.ResetAll(message.from_user.id)
    await VecMess(message)

async def VecMess(message: types.Message):
    db.ConnectTo("..\\bot_user\\database.db")
    userbot.namer = Namer
    prev = userbot.EvPrevMsgId(message.from_user.id, message.from_user.first_name, message.from_user.last_name, message.from_user.username)    # Evaluate Previous Message ID
    if prev != None:
        await bot.delete_message(chat_id=message.from_user.id, message_id=prev)
    (text, kbd, halt, prmode, address, img) = userbot.DispatchPhrase(message.from_user.id, message.text)
    if img is None:
        if address is None:
            reply = await bot.send_message(message.from_user.id, text=text, parse_mode=prmode ,reply_markup=kbd)
        else:
            location = types.Location(latitude=address[0], longitude=address[1])
            reply = await bot.send_location(message.from_user.id, location=location, caption=text, parse_mode=prmode, reply_markup=kbd)
    else:
        reply = await bot.send_photo(message.from_user.id, img, caption=text, parse_mode=prmode, reply_markup=kbd)
    userbot.RetainPrevMsgId(message.from_user.id, reply.message_id)
    print(message.from_user.id)
        

@router.callback_query()
async def VecCallBack(query: types.CallbackQuery):
    db.ConnectTo("..\\bot_user\\database.db")
    userbot.namer = Namer
    prev = userbot.EvPrevMsgId(query.from_user.id, query.from_user.first_name, query.from_user.last_name, query.from_user.username)    # Evaluate Previous Message ID
    if prev != None:
        await bot.delete_message(chat_id=query.from_user.id, message_id=prev)
    print(query.data)
    (text, kbd, halt, prmode, address, img) = userbot.DispatchPhrase(query.from_user.id, query.data)
    if img is None:
        if address is None:
            reply = await bot.send_message(query.from_user.id, text=text, parse_mode=prmode ,reply_markup=kbd)
        else:
            location = types.Location(latitude=address[0], longitude=address[1])
            reply = await bot.send_location(query.from_user.id, location=location, caption=text, parse_mode=prmode, reply_markup=kbd)
    else:
        reply = await bot.send_photo(query.from_user.id, img, caption=text, parse_mode=prmode, reply_markup=kbd)
    userbot.RetainPrevMsgId(query.from_user.id, reply.message_id)
    print(query.from_user.id)


async def main():
    print("Запустился")
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot, skip_updates=True)


if __name__ == "__main__":
    print("...")
    asyncio.run(main())