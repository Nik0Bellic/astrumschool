from aiogram import types, Bot, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text

from keyboards.client_kb import kb_who, kb_grade, kb_ugrade, kb_subjects, kb_menu
from lexicon.lexicon import LEXICON
from config_data.config import Config, load_config
from database.database import db_tutor

config: Config = load_config()
    
bot: Bot = Bot(token=config.tg_bot.token, parse_mode='HTML')

class FSMClient(StatesGroup):
    name = State()
    subjects = State()
    grade = State()

# subjects = ["Математика", "Русский язык", "Английский язык", "Литература", "Физика", "Химия", "Биология", "История", "География", "Обществознание", "Экономика", "Искусство", "Линейная алгебра", "Алгебра", "Геометрия", "Информатика"]
subjects = ["maths", "russian", "english", "literature", "physics", "chemistry", "biology", "history", "geography", "social_studies", "economics", "art", "algebra", "geometry", "informatics"]
good = []


# @dp.message_handler(commands=['start', 'help'])
async def command_start(message : types.Message, state=None):
    await message.answer(LEXICON[message.text])
    await FSMClient.name.set()
    await message.answer(LEXICON['get_name'])
 
# out from state
# @dp.message_handler(state="*", commands='отмена')
# @dp.message_handler(Text(equals='отмена', ignore_case=True), state="*")
async def cancel_handler(message: types.Message, state=FSMClient):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply('OK')


# @dp.message_handler(state=FSMClient.name)
async def get_name(message: types.Message, state=FSMClient.name):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMClient.next()
    await message.answer(text=LEXICON['get_subjects'], reply_markup=kb_subjects)


# @dp.message_handler(state=FSMClient.subjects)
async def get_subjects(callback : types.CallbackQuery, state=FSMClient.subjects):
    if callback.data in good:
        await callback.answer(f"Этот предмет ты уже выбрал")
    else:
        async with state.proxy() as data:
            good.append(callback.data)
            data.setdefault('subjects', []).append(callback.data)
        await callback.answer(f"Ты выбрал предмет: {callback.data}")


# @dp.callback_query_handler(Text(equals='next'))
async def go_next(callback: types.CallbackQuery, state=FSMClient.subjects):
    await FSMClient.next()
    await bot.delete_message(chat_id=callback.from_user.id, message_id=callback.message.message_id)
    await bot.send_message(callback.from_user.id, text=LEXICON['get_grade'], reply_markup=kb_grade)


async def get_grade(message: types.Message, state=FSMClient.grade):
    async with state.proxy() as data:
        data['grade'] = message.text
        
    
    db_tutor.add_tutor(state, message.from_user.id)
    await state.finish()
    
    await message.answer(text=LEXICON['thanks'], reply_markup=types.ReplyKeyboardRemove())


# @dp.callback_query_handler(Text(equals='next'))
# async def search(message: types.Message):
#     await bot.send_message(message.from_user.id, str(good))
#     await bot.send_message(message.from_user.id, str(res))
#     await bot.send_message(message.from_user.id, 'Меню', reply_markup=kb_menu)


def register_user_handlers(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start'])
    dp.register_message_handler(cancel_handler, state="*", commands='отмена')
    dp.register_message_handler(cancel_handler, Text(equals='отмена', ignore_case=True), state="*")
    dp.register_message_handler(get_name, state=FSMClient.name)
    dp.register_callback_query_handler(get_subjects, lambda callback: callback.data in subjects, state=FSMClient.subjects)
    dp.register_callback_query_handler(go_next, Text(equals='next'), state=FSMClient.subjects)
    dp.register_message_handler(get_grade, state=FSMClient.grade)
    # dp.register_callback_query_handler(search, Text(equals='next'))