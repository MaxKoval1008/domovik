from aiogram.dispatcher.filters.state import State, StatesGroup


class UserTel(StatesGroup):
    Tel = State()


class Service(StatesGroup):
    Service = State()


class Skills(StatesGroup):
    Skills = State()
