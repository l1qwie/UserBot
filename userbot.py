import datetime
import db
import markups as nav
import re

def failingNamer(name: str, nick:str):
    assert(False)


namer = failingNamer 


class User:
#ID
    id: int

#Contact Inf
    name: str
    surname: str
    username: str

#Reg to Games
    sport_reg_to_game: str
    date_reg_to_game: int
    time_reg_to_game: int
    seats_reg_to_game: int
    payment_reg_to_game: str
    payment_status_reg_to_game: bool

#Inf For Me
    act: str
    level: int


NEGATIVE = -1
START = 0
LEVEL1 = 1
LEVEL2 = 2
LEVEL3 = 3
OPTIONS = 3
LEVEL4 = 4
LEVEL5 = 5
LEVEL6 = 6


def DispatchPhrase (id: int, phrase: str):
    u = RetrieveUser(id)
    print('level =', u.level, 'phrase =', phrase, 'action =', u.act)
    if phrase == "MainMenu" or phrase == "/menu":
        text = "Главное меню"
        kbd = nav.MenuOptions
        halt = None
        u.level = OPTIONS
        u.act = "divarication"
        prmode = None
        address = None
        img = None
    elif u.act == "registration":
        (text, kbd, halt, prmode, address, img) = Welcome(u, phrase)
    elif u.act == "divarication":
        (text, kbd, halt, prmode, address, img) = Options(u, phrase)
    elif u.act == "reg to games":
        (text, kbd, halt, prmode, address, img) = RegToGames(u, phrase)
    RetainUser(u)
    print("TEXT =", text)
    return text, kbd, halt, prmode, address, img

def Options(u: User, phrase: str):
    if phrase == "Reg to games":
        u.level = START
        u.act = "reg to games"
        text, kbd, halt, prmode, address, img = RegToGames(u, phrase)
    return text, kbd, halt, prmode, address, img

def RegToGames(u: User, phrase: str):
    text = None
    kbd = None
    halt = None
    prmode = None
    address = None
    img = None
    if u.level == START:
        text, kbd = KindOfSport(u)
    elif u.level == LEVEL1:
        text, kbd, halt = DateSelection(u, phrase)
    elif u.level == LEVEL2:
        text, kbd, halt = TimeSelection(u, phrase)
    elif u.level == LEVEL3:
        text, kbd, halt = FreeSeats(u, phrase)
    elif u.level == LEVEL4:
        text, kbd, halt = PaymentMethod(u, phrase)
    elif u.level == LEVEL5:
        text, kbd, halt, prmode, address, img = CardPayment(u, phrase)
    elif u.level == LEVEL6:
        text, kbd, halt, prmode, address = BestWishes(u)
    return text, kbd, halt, prmode, address, img

def KindOfSport(u: User):
    text = "Выберите вид спорта."
    kbd = nav.KindOfSport
    u.level = LEVEL1
    return text, kbd

def DateSelection(u: User, phrase: str):
    if phrase in ("volleyball", "fooball"):
        halt = True
        u.sport_reg_to_game = phrase
        text = "Выберите дату."
        kbd = nav.kbdata(CreateDateList(db.SelectingDateWithThisSport(phrase))) # list of int
        u.level = LEVEL2
    else:
        halt = False
        text = "Пожалуйста, нажмите на кнопку!\n\nВыберите вид спорта."
        kbd = nav.KindOfSport
    return text, kbd, halt

def TimeSelection(u: User, phrase: str):
    print(db.SelectingDateWithThisSport2(u.id))
    if phrase in list(map(str, db.SelectingDateWithThisSport2(u.id))):
        halt = True
        text = "Выберите время."
        kbd = nav.kbtime(CreateTimeList(db.SelectionTimeWithThisSportAndDate(int(phrase)))) # list of
        u.level = LEVEL3
        u.date_reg_to_game = int(phrase)
    else:
        halt = False
        text = "Пожалуйста, нажмите на кнопку!\n\nВыберите дату."
        kbd = nav.kbdata(CreateDateList(list(map(str, db.SelectingDateWithThisSport2(u.id))))) # list
    return text, kbd, halt

def FreeSeats(u: User, phrase: str):
    if phrase in list(map(str, db.SelectionTimeWithThisSportAndDate(int(phrase)))):
        halt = True
        text = "Выберите или введите желаемое количество мест."
        kbd = nav.FrequentChoice
        u.level = LEVEL4
        u.time_reg_to_game = int(phrase)
    else:
        halt = False
        text = "Пожалуйста, нажмите на кнопку!\n\nВыберите время."
        kbd = nav.kbtime(CreateTimeList(db.SelectionTimeWithThisSportAndDate(int(u.date_reg_to_game)))) # list
    return text, kbd, halt

def PaymentMethod(u: User, phrase: str):
    halt = None
    if IntCheck(phrase):
        halt, upd_seats  = RemainingSeats(u.id, int(phrase))
        if halt is True:
            u.seats_reg_to_game = int(phrase)
            text = "Выберите способ оплаты."
            kbd = nav.KbPay
            u.level = LEVEL5
            db.BalanceOfTheUniverse(upd_seats, u.id)
        else:
            text = "Вы ввели не цифру или ввели цифру, которая больше, чем количество свободных мест на эту игру.\n\n\nВыберите или введите желаемое количество мест."
            kbd = nav.FrequentChoice
    else:
        text = "Я жду от вас нажатия на кнопку или сообщение, состоящее только из числа.\n\n\nВыберите или введите желаемое количество мест."
        kbd = nav.FrequentChoice
    return text, kbd, halt

def CardPayment(u: User, phrase: str):
    prmode = None
    address = None
    img = None
    if phrase in ("card", "cash"):
        halt = True
        u.payment_reg_to_game = phrase
        if phrase == "card":
            text = "Выше я выслал вам QR-code, по которому вы можете перейти и оплатить или же нажмите на кнопку ниже 'Оплатить'."
            kbd = nav.Papara
            with open('qr.jpg', 'rb') as photo:
                img = photo
            u.level = LEVEL6
        else:
            text, kbd, prmode, address = BestWishes(u)
    else:
        halt = False
        text = "Пожалуйста, нажмите на кнопку!\n\nВыберите способ оплаты."
        kbd = nav.KbPay
    return text, kbd, halt, prmode, address, img



def BestWishes(u: User):
    sport, date, time, address, payment = InfAboutNewGameUser(u)
    text = f"""Прекрасно! Теперь вы зарегестрированны на игру. 
1. Вид спорта: <b>{sport}</b>
2. Дата: <b>{date}</b>
3. Время: <b>{time}</b>
4. Вы записали <b>{u.seats_reg_to_game}</b> персон на эту игру
5. Оплата: <b>{payment}</b>

***Вы можете изменить некоторые данные Вашей записи 
или же удалить ее в Главном Меню нажав на "Посмотреть мои записи".***

❤️❤️❤️Ждем вас по адресу:
https://www.google.com/maps?q={address[0]},{address[1]}"""
    prmode = "HTML"
    kbd = nav.GoTo
    db.ComNewRegGameUser(u.id)
    return text, kbd, prmode, address



def InfAboutNewGameUser(u: User):
    if u.sport_reg_to_game == "volleyball":
        sport = "Волейбол"
    else:
        sport = "Футбол"
    if u.payment_reg_to_game == "card":
        payment = "Карта (онлайн)"
    else:
        payment = "Наличка (организатору)"
    date = CreateDateStr(u.date_reg_to_game)
    time = CreateTimeStr(u.time_reg_to_game)
    address = db.SelectAdressGame(u.id)
    return sport, date, time, address, payment


def Welcome(u: User, phrase):
    text = None
    kbd = None
    halt = None
    prmode = None
    address = None
    img = None
    print(START)
    if u.level == START:
        text, kbd = GreetingsToUser(u)
    elif u.level == LEVEL1:
        text, kbd = WarningRules(u, phrase)
    elif u.level == LEVEL2:
        text, kbd = GoToOptions(u, phrase)
    return text, kbd, halt, prmode, address, img

def GreetingsToUser(u: User):
    text = "Добро пожаловать в нашего бота! Этот бот предназначен для регистрации на спортивные игры в Стамбуле, но для начала вам нужно зарегистрироваться у нас!"
    kbd = nav.Registration
    u.level = LEVEL1
    return text, kbd

def WarningRules(u: User, phrase: str):
    if phrase == "GoReg":
        text = """Добро Пожаловать в нашу дружную компанию! Далее я вам напишу некоторые правила, и рекомендации как пользоваться ботом:
1. Просмотр расписания.
    - Предельно просто. Вы сможете посмтореть полное расписание всех возможных игр.
2. Регистрация на игру.
    - Бот поможет вам записаться на интересующую вас игру.
3. Посмотреть фотографии.
    - Тут будут храниться все фотографии, видео, гифки и все остальное, что будут выкладывать другие пользователи с уже прошедших игр.
4. Посмототреть мои записи.
    - Нажав сюда, вы сможете посмотреть игры, которые вы ожидаете. Так же тут вы сможете отменить запись.
5. Связаться с администратором.
    - Бот пришлет вам тг профиль Администратора и нажав на имя (оно будет подствечено синим) вы перейдете в диалог с ним.
    
    
P.S. Если что, то у бота есть волшебная команда /menu. Эта команда всегда сможет вас вернуть в главное меню. 
Естесвенно, если вы пришлете ее, когда у вас есть какой то незаконченный процес в боте, то прогресс не сохраниться."""
        kbd = nav.Further
        u.level = LEVEL2
    else:
        text = "Добро пожаловать в нашего бота! Этот бот предназначен для регистрации на спортивные игры в Стамбуле, но для начала вам нужно зарегистрироваться у нас!"
        kbd = nav.Registration
    return text, kbd


def GoToOptions(u: User, phrase):
    if phrase == "GoNext":
        db.CompletionOfRegistration(u.id)
        text = "Выберите интересующую вас опцию."
        kbd = nav.Options
        u.level = OPTIONS
        u.act = "divarication"
    else:
        text = """Пожалуйста, для продолжения нажмите на кнопку\n\n\nДобро Пожаловать в нашу дружную компанию! Далее я вам напишу некоторые правила, и рекомендации как пользоваться ботом:
1. Просмотр расписания.
    - Предельно просто. Вы сможете посмтореть полное расписание всех возможных игр.
2. Регистрация на игру.
    - Бот поможет вам записаться на интересующую вас игру.
3. Посмотреть фотографии.
    - Тут будут храниться все фотографии, видео, гифки и все остальное, что будут выкладывать другие пользователи с уже прошедших игр.
4. Посмототреть мои записи.
    - Нажав сюда, вы сможете посмотреть игры, которые вы ожидаете. Так же тут вы сможете отменить запись.
5. Связаться с администратором.
    - Бот пришлет вам тг профиль Администратора и нажав на имя (оно будет подствечено синим) вы перейдете в диалог с ним.
    
    
P.S. Если что, то у бота есть волшебная команда /menu. Эта команда всегда сможет вас вернуть в главное меню. 
Естесвенно, если вы пришлете ее, когда у вас есть какой то незаконченный процес в боте, то прогресс не сохраниться."""
        kbd = nav.Further
    return text, kbd









def CreateTimeList(times: list) -> list:
    times_ready = []
    for time in times:
        times_ready.append(CreateTimeStr(time))
    return times_ready

def CreateDateList(days: list) -> list:
    list_for_dates = []
    for day in days:
        list_for_dates.append(CreateDateStr(day))
    return list_for_dates

def CreateDateStr(day_int: int) -> str:
    year = day_int//10000
    month = (day_int-(year*10000))//100
    day = (day_int-(year*10000)-(month*100))//1
    date_str = f"{day}-{month}-{year}"
    return date_str

def CreateTimeStr(time_int: int) -> str:
    hour = time_int//100
    minute = (time_int-(hour*100))//1
    time_str = f"{hour}:{minute}"
    return time_str


def IntCheck(mes) -> bool:
    if isinstance(mes, str):
        halt = IntCheck2(mes)
    else:
        new_mes= str(mes)
        halt = IntCheck2(new_mes)
    return halt

def IntCheck2(mes: str) -> bool:
    if re.fullmatch(r'^\d{1,2}$', mes):
        halt = True
    else:
        halt = False
    return halt

def RemainingSeats(id: int, seat: int) -> bool:
    free_seats = db.HowMutchSeats(id)
    update_seats = None
    if seat > free_seats:
        halt = False
    else:
        update_seats = free_seats - seat
        halt = True
    return halt, update_seats

def RetrieveUser(uid: int) -> User:
#ID    
    u = User()
    u.id = uid

#Contact Inf
    u.name = None
    u.surname = None
    u.username = None

#Reg to Game
    u.sport_reg_to_game = None
    u.date_reg_to_game = None
    u.time_reg_to_game = None
    u.seats_reg_to_game = None
    u.payment_reg_to_game = None
    u.payment_status_reg_to_game = None

#Inf for me
    u.act = None
    u.level = None

    (u.id, 
    u.name, u.surname, u.username, 
    u.sport_reg_to_game, u.date_reg_to_game, u.time_reg_to_game, u.seats_reg_to_game, u.payment_reg_to_game, u.payment_status_reg_to_game, 
    u.act, u.level) = db.RecallUser(uid)
    if u.level == NEGATIVE:
        u.level = START
    return u

def RetainUser(u: User):
    db.RetainUser(u.id, u.name, u.surname, u.username, u.act, u.level)

def EvPrevMsgId(uid: int, name: str, lname: str, usname: str):
    mes_id = db.RecognizeExMesID(uid, name, lname, usname)
    return mes_id

def RetainPrevMsgId(uid: int, m_id: int):
    db.AddNewMesID(uid, m_id)