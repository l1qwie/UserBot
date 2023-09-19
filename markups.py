from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import re
import datetime


def KbCreateTime(time: list) -> list:
    times_ready = []
    tm = 0
    while tm < len(time):
        hour = time[tm]//100
        minute = (time[tm]-(hour*100))//1
        time_str = f"{hour}:{minute}"
        times_ready.append(time_str)
        tm += 1
    return times_ready

def KbCreateDate(days: list) -> list:
    list_for_dates = []
    dy = 0
    while dy < len(days):
        year = days[dy]//10000
        month = (days[dy]-(year*10000))//100
        day = (days[dy]-(year*10000)-(month*100))//1
        date_str = f"{day}-{month}-{year}"
        list_for_dates.append(date_str)
        dy += 1
    return list_for_dates

def KbDateCheck(date) -> str:
    date_pattern = r'\d{1,2}[^0-9]+\d{1,2}[^0-9]+\d{4}'
    match = re.search(date_pattern, date)
    date_match = match.group(0)
    components = re.findall(r'\d+', date_match)
    day, month, year = map(int, components)
    dbdate = str((day*1)+(month*100)+(year*10000))
    return dbdate

def KbTimeCheck(time) -> str:
    time_pattern = r'\d{1,2}[^0-9]+\d{1,2}'
    match = re.search(time_pattern, time)
    time_match = match.group(0)
    components = re.findall(r'\d+', time_match)
    hour, minute = map(int, components)
    dbtime = str((hour * 100) + minute)
    return dbtime


defualtkb = []
#1
Registration = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Зарегистрироваться", callback_data="GoReg")]])

Further = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Все понятно!", callback_data="GoNext")]])

Options = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Просмотр расписания", callback_data="Looking Schedule")],
    [InlineKeyboardButton(text="Регистрация на игру", callback_data="Reg to games")],
    [InlineKeyboardButton(text="Наши фото и видео", callback_data="Photo&Video")],
    [InlineKeyboardButton(text="Посмотреть мои записи", callback_data="My records")]
])

KindOfSport = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Воллейбол", callback_data="volleyball")],
    [InlineKeyboardButton(text="Футбол", callback_data="football")]
])

def kbdata(days):
    keyboard = []
    for day in days:
        dbdate = KbDateCheck(day)
        button = InlineKeyboardButton(text=f"{day}", callback_data=f"{dbdate}")
        keyboard.append([button])
    inkb1 = InlineKeyboardMarkup(inline_keyboard=keyboard)
    return inkb1

def kbtime(times, seats):
    keyboard = []
    for count, item in zip(times, seats):
        dbtime = KbTimeCheck(count)
        button = InlineKeyboardButton(text=f"{count}  ({item} мест)", callback_data=f"{dbtime}")
        keyboard.append([button])
    inkb2 = InlineKeyboardMarkup(inline_keyboard=keyboard)
    return inkb2

FrequentChoice = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Я буду один", callback_data="1")],
    [InlineKeyboardButton(text="Нас будет двое", callback_data="2")],
    [InlineKeyboardButton(text="Нас будет трое", callback_data="3")]
])

KbPay = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Онлайн оптала", callback_data="card")],
    [InlineKeyboardButton(text="Наличкой, по прибытию - администратору", callback_data="cash")]
])

Papara = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Оплатить', url="https://www.papara.com/personal/qr?karekod=7502100102120204082903122989563302730612230919141815530394954120000000000006114081020219164116304DDE3", callback_data="payment completed")],
    [InlineKeyboardButton(text="Дальше", callback_data="Next")]
])

GoTo = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="В главное меню", callback_data="MainMenu")]
])



btnreg = InlineKeyboardButton(text='Регистрация', callback_data="yes")
kb = InlineKeyboardMarkup(row_width=2,inline_keyboard=[[btnreg]])

#kb.add(btnreg)

#2

btnVB = KeyboardButton(text='🏐 ВОЛЕЙБОЛ')
btnFB = KeyboardButton(text='⚽️ ФУТБОЛ')
defualtkb.append([btnVB])
defualtkb.append([btnFB])
mainGames = ReplyKeyboardMarkup(resize_keyboard=True,keyboard=defualtkb)
defualtkb.clear()
#mainGames = ReplyKeyboardMarkup(resize_keyboard=True,keyboard=[[KeyboardButton(text='🏐 ВОЛЕЙБОЛ'), KeyboardButton(text='⚽️ ФУТБОЛ')]])
#mainGames.add(btnVB, btnFB)




btnBack = KeyboardButton(text='◀️ Назад')
kbback = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[[btnBack]])

#3

btnRul = KeyboardButton(text='📋 Правила')
btnRecom = KeyboardButton(text='🤙 Рекомендации к тренировке')
btnMakeing = KeyboardButton(text='😎 Записаться')
btnSchedule = KeyboardButton(text='🗓 Расписание')
defualtkb.append([btnRul])
defualtkb.append([btnRecom])
defualtkb.append([btnMakeing])
defualtkb.append([btnSchedule])

detalis = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=defualtkb)

defualtkb.clear()
#detalis.add(btnRul, btnRecom, btnMakeing, btnSchedule, btnBack)

#5
def inkb(data, days):

    keyboard = []
    day = 0
    for day, date in zip(days, data):
        button = InlineKeyboardButton(text=f"{day} ({date})", callback_data=f"*{date}")
        keyboard.append([button])
        
        
    inkb1 = InlineKeyboardMarkup(inline_keyboard=keyboard)
    days.clear()
    data.clear()

    return inkb1
    

#6
def timekb(time: list, place: list):

    keyboard = []
    i = 0
    while i < len(time):
        button = InlineKeyboardButton(text=f"{time[i]} (мест на эту игру: {place[i]})", callback_data=f"9{time[i]} {place[i]}")
        keyboard.append([button])
        i += 1


    intimekb = InlineKeyboardMarkup(inline_keyboard=keyboard)
    time.clear()
    return intimekb


#5

btnCash = KeyboardButton(text='💷 Наличные')
btnCard = KeyboardButton(text='💳 Перевод')
defualtkb.append([btnCash])
defualtkb.append([btnCard])

choisePay = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=defualtkb)
defualtkb.clear()
#choisePay.add(btnCash, btnCard, btnBack)

#6

btnInf = KeyboardButton(text='Узнать информацию о себе')
defualtkb.append([btnInf])
defualtkb.append([btnBack])

kbINFO = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=defualtkb)
#kbINFO.add(btnInf, btnBack)
defualtkb.clear()

btnyes = KeyboardButton(text='Да')
btnno = KeyboardButton(text='Нет')
kbwat = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[[btnyes, btnno]])
#kbwat.add(btnyes, btnno)

#7

def choicekb(choice_time, choice_data_us):
    keyboard = []
    i = 0
    while i < len(choice_time):
        button = InlineKeyboardButton(text=f"{choice_data_us[i]} (Время проведения игры: {choice_time[i]})", callback_data=f"7{choice_data_us[i]}{choice_time[i]}")
        keyboard.append([button])
        i += 1
    
    data_timekb = InlineKeyboardMarkup(inline_keyboard=keyboard)
    choice_time.clear()
    choice_data_us.clear()
    return data_timekb





btnDel = InlineKeyboardButton(text="Информация по записям", callback_data="game")
btnDel2 = InlineKeyboardButton(text="Вся информация обо мне", callback_data="all")

kbDEL = InlineKeyboardMarkup(row_width=2, inline_keyboard=[[btnDel, btnDel2]])

#kbDEL.add(btnDel, btnDel2)


btnfoot = InlineKeyboardButton(text="Футбол", callback_data="football")
btnvoll = InlineKeyboardButton(text="Волейбол", callback_data="volleyball")

kbgames = InlineKeyboardMarkup(row_width=2, inline_keyboard=[[btnfoot, btnvoll]])

#kbgames.add(btnfoot, btnvoll)

btnBack2 = KeyboardButton(text='◀️ Назад')
defualtkb.append([btnBack2])
back = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=defualtkb)
defualtkb.clear()

#back.add(btnBack2)

btncom = KeyboardButton(text='Завершить регистрацию')
defualtkb.append([btncom, btnBack])
kbcom = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[[btncom, btnBack]])
defualtkb.clear()

btnSolo = KeyboardButton(text='Я буду один')
btnDuo = KeyboardButton(text='Нас будет двое')
btnTrio = KeyboardButton(text='Нас будет трое')
defualtkb.append([btnSolo])
defualtkb.append([btnDuo])
defualtkb.append([btnTrio])

Kbofseats = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=defualtkb)
defualtkb.clear()



peremennaya = 1