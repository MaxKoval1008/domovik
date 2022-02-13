from aiogram.dispatcher import FSMContext
from bot import dp
from aiogram import types
import keyboards as kb
from data_base import UsersBase
from states import UserTel as ut
from states import Service, Skills

db = UsersBase('users.db')


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    db.create_table_users()
    await message.reply(f"Привет! Для регистрации нажмите кнопку ниже.", reply_markup=kb.markup_start)


@dp.callback_query_handler(lambda c: c.data == 'start')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await callback_query.message.answer("Введите контактный номер телефона.")
    await ut.Tel.set()


@dp.message_handler(state=ut.Tel)
async def process_start_command(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Tel'] = message.text
    data = await state.get_data()
    if db.exists_user(message.from_user.id):
        await message.answer('Вы уже зарегистрированы.', reply_markup=kb.markup_main)
    else:
        db.add_to_db_users(message.from_user.id, list(data.values())[0])
        await message.answer('Добро пожаловать!', reply_markup=kb.markup_main)
    await state.finish()


@dp.message_handler(lambda message: message.text == 'Зарегистрировать заявку на помощь')
async def process_start_command(message: types.Message):
    db.create_table_help()
    await message.answer('Опишите в какой услуге вы нуждаетесь.')
    await Service.Service.set()


@dp.message_handler(state=Service.Service)
async def process_start_command(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Service'] = message.text
    data = await state.get_data()
    tel = db.telephone_user(message.from_user.id)
    db.add_application_help(list(data.values())[0], tel[0])
    await message.answer('Вас наберут в ближайший будний день с 9 до 18.')
    await state.finish()


@dp.message_handler(lambda message: message.text == 'Зарегистрироваться как помощник')
async def process_start_command(message: types.Message):
    db.create_table_helpers()
    await message.answer('Какие услуги Вы можете оказать?')
    await Skills.Skills.set()


@dp.message_handler(state=Skills.Skills)
async def process_start_command(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Skills'] = message.text
    data = await state.get_data()
    tel = db.telephone_user(message.from_user.id)
    db.add_application_helper(list(data.values())[0], tel[0])
    await message.answer('Благодарим за участие.')
    await state.finish()


@dp.message_handler(commands=['allhelp'])
async def process_start_command(message: types.Message):
    await message.reply(db.get_all_help())


@dp.message_handler(commands=['allhelper'])
async def process_start_command(message: types.Message):
    await message.reply(db.get_all_helper())