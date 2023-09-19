import userbot
import markups as nav
import db
import random




def TestingNamer (name: str, nick: str) -> str:
    return name + nick

def GlobalT():
    userbot.namer = TestingNamer
    db.ConnectTo("..\\bot_user\\test_database.db")


def TestReg():
    userbot.namer = TestingNamer
    db.ConnectTo("..\\bot_user\\test_database.db")
    db.ResetAll(738070596)
    first = ["akhjdashjksd", 121, 2, "12311, ", 'assda'] 
    second = ["hjk23hjk123hjkuhjk", "12312312513", 2323131, 2, "GoReg"]
    thierd = ["ajkldjklasjkld", 1231231231, "123123123", 2, "GoNext"]
    Welcome(first)
    RulesOfBot(second)
    Penultimate(thierd)

def Welcome(f: list):
    for item in f:
        db.DataFitting("registration", 0, 738070596)
        (text, kbd, halt, prmode, address, img) = userbot.DispatchPhrase(738070596, item)
        assert(text == "Добро пожаловать в нашего бота! Этот бот предназначен для регистрации на спортивные игры в Стамбуле, но для начала вам нужно зарегистрироваться у нас!")
        assert(kbd == nav.Registration)


def RulesOfBot(s: list):
    for item in s:
        db.DataFitting("registration", 1, 738070596)
        (text, kbd, halt, prmode, address, img) = userbot.DispatchPhrase(738070596, item)
        if item == "GoReg":
            assert(text == """Добро Пожаловать в нашу дружную компанию! Далее я вам напишу некоторые правила, и рекомендации как пользоваться ботом:
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
Естесвенно, если вы пришлете ее, когда у вас есть какой то незаконченный процес в боте, то прогресс не сохраниться.""")
            assert(kbd == nav.Further)
        else:
            assert(text == "Добро пожаловать в нашего бота! Этот бот предназначен для регистрации на спортивные игры в Стамбуле, но для начала вам нужно зарегистрироваться у нас!")
            assert(kbd == nav.Registration)

def Penultimate(th: list):
    for item in th:
        db.DataFitting("registration", 2, 738070596)
        (text, kbd, halt, prmode, address, img) = userbot.DispatchPhrase(738070596, item)
        if item == "GoNext":
            assert(text == "Выберите интересующую вас опцию.")
            assert(kbd == nav.Options)
        else:
            assert(text == """Пожалуйста, для продолжения нажмите на кнопку\n\n\nДобро Пожаловать в нашу дружную компанию! Далее я вам напишу некоторые правила, и рекомендации как пользоваться ботом:
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
Естесвенно, если вы пришлете ее, когда у вас есть какой то незаконченный процес в боте, то прогресс не сохраниться.""")
            assert(kbd == nav.Further)


def TestRegToGame():
    userbot.namer = TestingNamer
    db.ConnectTo("..\\bot_user\\test_database.db")
    first = ["pofig"]
    second = ["ajkldjklasjkld", 1231231231, "123123123", 2, "volleyball"]
    thierd = ["akhjdashjksd", 121, 2, "12311,", '20-02-2024']
    fourth = ["hjk23hjk123hjkuhjk", "12312312513", 2323131, 2, "12 00"]
    fifth =  ["231sss", "12312312513", 2323131, 5, "4"]
    sixth = ["ahhhhhh", 1231231231, "123123123", 8, "card"]
    seventh = ["asdwwwwww", 1231, "123123123", 3, "payment completed"]
    testKindOfSport(first)
    testDateSelection(second)
    #testTimeSelection(thierd) PROBLEM HERE AND I DON"T KNOW WHERE IS DATA OF NAME SURNAME AND USERNAME
    #testFreeSeats(fourth)
    #testPaymentMethod(fifth)
    #testCardPayment(sixth)
    #if fifth[4] == "card":
    #    db.DataFitting("reg to games", 5, 738070596)
    #    (text, kbd, halt, prmode, address, img) = userbot.DispatchPhrase(738070596, seventh[4])
    #    testBestWishes(sixth[4], text, kbd)

def testKindOfSport(f: list):
    for item in f:
        db.DataFitting("reg to games", 0, 738070596)
        (text, kbd, halt, prmode, address, img) = userbot.DispatchPhrase(738070596, item)
        assert(text == "Выберите вид спорта.")
        assert(kbd == nav.KindOfSport)

def testDateSelection(sec: list):
    for item in sec:
        db.DataFitting("reg to games", 1, 738070596)
        (text, kbd, halt, prmode, address, img) = userbot.DispatchPhrase(738070596, item)
        if halt:
            assert(text == "Выберите дату.")
            assert(kbd == nav.kbdata(userbot.CreateDateList(db.SelectingDateWithThisSport(item))))
        else:
            assert(text == "Пожалуйста, нажмите на кнопку!\n\nВыберите вид спорта.")
            assert(kbd == nav.KindOfSport)

def testTimeSelection(th: list):
    for item in th:
        db.DataFitting("reg to games", 2, 738070596)
        (text, kbd, halt, prmode, address, img) = userbot.DispatchPhrase(738070596, item)
        print("halt =", halt)
        if halt:
            assert(text == "Выберите время.")
            assert(kbd ==nav.kbtime(userbot.CreateTimeList(db.SelectionTimeWithThisSportAndDate(int(item)))))
        else:
            assert(text == "Пожалуйста, нажмите на кнопку!\n\nВыберите дату.")
            assert(kbd == nav.kbdata(userbot.CreateDateList(db.SelectingDateWithThisSport(738070596))))

def testFreeSeats(fourth: list):
    for item in fourth:
        db.DataFitting("reg to games", 3, 738070596)
        (text, kbd, halt, prmode, address, img) = userbot.DispatchPhrase(738070596, item)
        if halt:
            assert(text == "Выберите или введите желаемое количество мест.")
            assert(kbd == nav.FrequentChoice)
        else:
            assert(text == "Пожалуйста, нажмите на кнопку!\n\nВыберите время.")
            assert(kbd == nav.kbtime(userbot.CreateTimeList(db.SelectionTimeWithThisSportAndDate(int(db.SelDateRegToGame(738070596))))))
    
def testPaymentMethod(fif: list):
    for item in fif:
        db.DataFitting("reg to games", 4, 738070596)
        (text, kbd, halt, prmode, address, img) = userbot.DispatchPhrase(738070596, item)
        if userbot.IntCheck(item):
            if halt:
                assert(text == "Выберите способ оплаты.")
                assert(kbd == nav.KbPay)
            else:
                assert(text == "Вы ввели не цифру или ввели цифру, которая больше, чем количество свободных мест на эту игру.\n\n\nВыберите или введите желаемое количество мест.")
                assert(kbd == nav.FrequentChoice)
        else:
            assert(text == "Я жду от вас нажатия на кнопку или сообщение, состоящее только из числа.\n\n\nВыберите или введите желаемое количество мест.")
            assert(kbd == nav.FrequentChoice)

def testCardPayment(six: list):
    for item in six:
        db.DataFitting("reg to games", 5, 738070596)
        (text, kbd, halt, prmode, address, img) = userbot.DispatchPhrase(738070596, item)
        if halt:
            if item == "card":
                assert(text == "Выше я выслал вам QR-code, по которому вы можете перейти и оплатить или же нажмите на кнопку ниже 'Оплатить'.")
                assert(kbd == nav.Papara)
            else:
                testBestWishes(item, text, kbd)

def testBestWishes(paymod: str, text: str, kbd):
    sport, date, time, address, payment = testInfAboutNewGameUser(738070596, paymod)
    assert(text == f"""Прекрасно! Теперь вы зарегестрированны на игру. 
1. Вид спорта: <b>{sport}</b>
2. Дата: <b>{date}</b>
3. Время: <b>{time}</b>
4. Вы записали <b>{db.SelSeatsRegToGame}</b> персон на эту игру
5. Оплата: <b>{payment}</b>

***Вы можете изменить некоторые данные Вашей записи 
или же удалить ее в Главном Меню нажав на "Посмотреть мои записи".***

❤️❤️❤️Ждем вас по адресу:
https://www.google.com/maps?q={address[0]},{address[1]}""")
    assert(kbd == nav.GoTo)
    db.DelGameTestUser(738070596)

def testInfAboutNewGameUser(id: int, odeme: str):
    if db.SelSportRegToGame == "volleyball":
        sport = "Волейбол"
    else:
        sport = "Футбол"
    if odeme == "card":
        payment = "Карта (онлайн)"
    else:
        payment = "Наличка (организатору)"
    date = userbot.CreateDateStr(db.SelDateRegToGame(id))
    time = userbot.CreateTimeStr(db.SelTimeRegToGame(id))
    address = db.SelectAdressGame(id)
    return sport, date, time, address, payment
