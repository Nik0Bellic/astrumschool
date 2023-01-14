from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton

pupil = "Школьник"
student = "Студент"

kb_who = ReplyKeyboardMarkup(resize_keyboard=True)
kb_who.row(pupil, student)

grade_5 = "5 класс"
grade_6 = "6 класс"
grade_7 = "7 класс"
grade_8 = "8 класс"
grade_9 = "9 класс"
grade_10 = "10 класс"
grade_11 = "11 класс"

kb_grade = ReplyKeyboardMarkup(resize_keyboard=True)
kb_grade.row(grade_5, grade_6).row(grade_7, grade_8).row(grade_9, grade_10, grade_11)

university_first = "1 курс"
university_second = "2 курс"
university_third = "3 курс"
university_fourth = "4 курс"

kb_ugrade = ReplyKeyboardMarkup(resize_keyboard=True)
kb_ugrade.row(university_first, university_second).row(university_third, university_fourth)

maths = KeyboardButton("Математика")
russian = KeyboardButton("Русский язык")
english = KeyboardButton("Английский язык")
literature = KeyboardButton("Литература")
physics = KeyboardButton("Физика")
chemistry = KeyboardButton("Химия")
biology = KeyboardButton("Биология")
history = KeyboardButton("История")
geography = KeyboardButton("География")
social_studies = KeyboardButton("Обществознание")
economics = KeyboardButton("Экономика")
art = KeyboardButton("Искусство")
linear_algebra = KeyboardButton("Линейная алгебра")
algebra = KeyboardButton("Алгебра")
geometry = KeyboardButton("Геометрия")
computer_science = KeyboardButton("Информатика")

kb_subjects = InlineKeyboardMarkup(row_width=3).add(InlineKeyboardButton(text='Математика', callback_data='maths'),
                                                InlineKeyboardButton(text='Русский язык', callback_data='russian'),
                                                InlineKeyboardButton(text='Английский язык', callback_data='english'),
                                                InlineKeyboardButton(text='Литература', callback_data='literature'),
                                                InlineKeyboardButton(text='Физика', callback_data='physics'),
                                                InlineKeyboardButton(text='Химия', callback_data='chemistry'),
                                                InlineKeyboardButton(text='Биология', callback_data='biology'),
                                                InlineKeyboardButton(text='История', callback_data='history'),
                                                InlineKeyboardButton(text='География', callback_data='geography'),
                                                InlineKeyboardButton(text='Обществознание', callback_data='social_studies'),
                                                InlineKeyboardButton(text='Экономика', callback_data='economics'),
                                                InlineKeyboardButton(text='Искусство', callback_data='art'),
                                                InlineKeyboardButton(text='Алгебра', callback_data='algebra'),
                                                InlineKeyboardButton(text='Геометрия', callback_data='geometry'),
                                                InlineKeyboardButton(text='Информатика', callback_data='informatics'),
                                                InlineKeyboardButton(text='Я всё выбрал, что дальше?', callback_data='next'))


search = KeyboardButton("Поиск учеников")
request = KeyboardButton("Нужна помощь с каким-то предметом")
edit = KeyboardButton("Изменить данные")

kb_menu = ReplyKeyboardMarkup(resize_keyboard=True)
kb_menu.row(search, request).add(edit)
