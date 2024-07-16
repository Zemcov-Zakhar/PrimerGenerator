import test_config
import logging
import filters
import random
 
from aiogram import Bot, Dispatcher, executor, types, castom
from aiogram.types.message import ContentType
    
a = 0
b = 0
vi = False
d = False
mat = "плохое слово"
t = 0
Primer = False
MIN = 0
MAX = 20



logging.basicConfig(level=logging.INFO)
bot = Bot(token=test_config.TOKEN)
dp = Dispatcher(bot)
PRICE = types.LabeledPrice(label="Подписка на 1 месяц", amount=100*100)


@dp.message_handler()
async def filter_message(message: types.Message):
    if mat in message.text:
        await message.delete()
        await message.answer("Это запрещённое слово.")


@dp.message_handler()
async def sisrets(message: types.Message):
    if "5847" in message.text:
        await message.delete()
        await message.answer("Токен: "+test_config.TOKEN)


@dp.message_handler()
async def anti_spam(message: types.Message):
    if last_message == message.text:
        await message.delete()
        if time == 0:
            await message.answer("Нельзя отсылать много одинаковых сообщений.")
        time = 10
    last_message = message.text


@dp.message_handler(commands = ["primers"])
async def primer(message: types.Message):
    await message.answer("Сколько примеров хотите решить?(25/50/100)")
    Primer = True

@dp.message_handler()
async def cal_primer(message: types.Message):
	if Primer == True:
		if "25" in message.text:
			call_primer = 25
			CALL_PRIMER = True
		elif "50" in message.text:
			call_primer = 50
			CALL_PRIMER = True
		elif "100" in message.text:
			call_primer = 100
			CALL_PRIMER = True

@dp.message_handler()
async def genprimers(message: types.Message):
    if CALL_PRIMER == True: 
    	if bprim == True:
    		if otvet in message.text:
    			await message.answer("Ответ правильный!")
    		else:
    			await message.answer("Ответ неверны")
    			await message.answer(f"Ответ: {otvet}")
    	a = random.randint(MIN,MAX)
    	b = random.randint(MIN,MAX-a)
    	if a >= 0:
    		av = f"{a}"
    	else:
    		av = f"({a})"
    	if b >= 0:
    		bv = f"{a}"
    	else:
    		bv = f"({a})"
    	await message.answer(f"{av}+{bv}=")
    	bprim = True


"""@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)"""

    
if __name__ == "__main__":
        executor.start_polling(dp, skip_updates=False)

while 1:
    if time > 0:
        time.sleep(t)
    else:
        t = 0
        time.sleep(0.5)
# log
logging.basicConfig(level=logging.INFO)
 
# init
bot = Bot(token=test_config.TOKEN)
dp = Dispatcher(bot)
 


# buy
 
 
 

@dp.message_handler(is_admin=True, commands=["ban"])
async def cmd_ban(message: types.Message):
    if not message.reply_to_message:
        await message.reply("1")
        return

    await message.bot.delete_message(message.message_id,chat_id=test_config.GROUP_ID)
    await message.bot.kick_chat_member(chat_id=test_config.GROUP_ID, user_id=message.reply_to_message.from_user.id)

    await message.reply_to_message.reply("Пользователь удалён.")




# run long-polling
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=False)