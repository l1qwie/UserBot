import sqlite3

import sqlite3

import logging



connection = None
cursor = None

#Routine
def ConnectTo (filename: str):
    global connection, cursor
    connection = sqlite3.connect(filename)
    cursor = connection.cursor()

def ResetAll(id: int):
    with connection:
        cursor.execute("DELETE FROM Users WHERE user_id = ?", (id,))

def RecallUser(id: int):
    with connection:
        cursor.execute("SELECT level FROM Users WHERE user_id = ?", (id,))
        level = cursor.fetchone()
        if level is None:
            res = -1
            cursor.execute("INSERT INTO Users (user_id, action, setup_reg, level) VALUES (?, 'registration', 'start', ?)", (id, res+1,))
        else:
            res = int(level[0])
        cursor.execute("""SELECT user_id, 
                       name, last_name, username, 
                       sport_reg_to_game, date_reg_to_game, time_reg_to_game, seats_reg_to_game, payment_reg_to_game, payment_status_reg_to_game,
                       action, level FROM Users WHERE user_id = ?""", (id,))
        (user_id, 
         name, last_name, username, 
         sport_reg_to_game, date_reg_to_game, time_reg_to_game, seats_reg_to_game, payment_reg_to_game, payment_status_reg_to_game,
         action, level) = cursor.fetchone()
        return (user_id, 
                name, last_name, username, 
                sport_reg_to_game, date_reg_to_game, time_reg_to_game, seats_reg_to_game, payment_reg_to_game, payment_status_reg_to_game,
                action, level)

def RetainUser(id: int, 
               name: str, 
               lastname: str, 
               username: str,
               act: str,
               level: int):
    with connection:
        cursor.execute("""UPDATE Users SET user_id = ?, name = ?, last_name = ?, username = ?, action = ?, level = ? WHERE user_id = ?""", 
                        (id, name, lastname, username, act, level, id))

#Reg            
def CompletionOfRegistration(id: int):
    with connection:
        cursor.execute("UPDATE Users SET setup_reg = 'completed' WHERE user_id = ?", (id,))


#Reg to Game
def SelectingDateWithThisSport(sport: str) -> list:
    with connection:
        cursor.execute("SELECT date FROM Schedule WHERE sport = :sport AND status IS NOT 'DELETE'", ({"sport": sport}))
        dates = [row[0] for row in cursor.fetchall()]
        return dates
    
def SelectingDateWithThisSport2(id: int) -> list:
    with connection:
        cursor.execute("SELECT date FROM Schedule JOIN Users ON Schedule.sport = Users.sport_reg_to_game WHERE Users.user_id = ? AND Schedule.status IS NOT 'DELETE'", (id,))
        dates = [row[0] for row in cursor.fetchall()]
        return dates

def SelectionTimeWithThisSportAndDate(date: int):
    with connection:
        cursor.execute("""SELECT time FROM Schedule 
                       JOIN Users ON Schedule.sport = Users.sport_reg_to_game
                       WHERE date = :date""", ({"date": date}))
        times = [row[0] for row in cursor.fetchall()]
        return times

def HowMutchSeats(id: int) -> int:
    with connection:
        cursor.execute("""SELECT seats
                            FROM Schedule
                            JOIN Users ON Users.sport_reg_to_game = Schedule.sport and Users.date_reg_to_game = Schedule.date and Users.time_reg_to_game = Schedule.time
                            WHERE Users.user_id = :id AND Schedule.status IS NOT 'DELETE'""", ({"id": id}))
        seats = int(cursor.fetchone()[0])
        return seats

def BalanceOfTheUniverse(seat: str, id: int):
    with connection:
        cursor.execute("""
            UPDATE Schedule
            SET seats = :st
            WHERE EXISTS (
                SELECT 1
                FROM Users
                WHERE Users.sport_reg_to_game = Schedule.sport
                AND Users.date_reg_to_game = Schedule.date
                AND Users.time_reg_to_game = Schedule.time
                AND Users.user_id = :id
            )
        """, {"st": seat, "id": id})

def SelectAdressGame(id: int):
    with connection:
        cursor.execute("""SELECT latitude, longitude 
                       FROM Schedule
                       JOIN Users ON Schedule.sport = Users.sport_reg_to_game AND
                       Schedule.date = Users.date_reg_to_game AND
                       Schedule.time = Users.time_reg_to_game 
                       WHERE Users.user_id = ?""", (id,))
        address = cursor.fetchone()
        return address

def ComNewRegGameUser(id: int):
    with connection:
        cursor.execute("""SELECT game_id 
                       FROM Schedule 
                       JOIN Users ON Schedule.sport = Users.sport_reg_to_game AND
                       Schedule.date = Users.date_reg_to_game AND
                       Schedule.time = Users.time_reg_to_game
                        WHERE Users.user_id = ?""", (id,))
        gid = cursor.fetchone()[0]
        cursor.execute("SELECT seats_reg_to_game, payment_reg_to_game FROM Users WHERE user_id = ?", (id,))
        seat, pay = cursor.fetchone()
        cursor.execute("INSERT INTO WatingForGamesUsers (user_id, game_id, seats, payment, setup_reg) VALUES (:id, :gid, :seat, :pay, 'READY')", ({"id": id, "gid": gid, "seat": seat, "pay": pay}))

#Del Mes
def RecognizeExMesID(id: int, n: str, ln: str, un: str):
    with connection:
        cursor.execute("SELECT exmess FROM Users WHERE user_id = :id", ({"id": id}))
        res = cursor.fetchone()
        if res == None:
            return res
        else:
            cursor.execute("UPDATE Users SET name = :n, last_name = :ln, username = :un WHERE user_id = :id", ({"n": n, "ln": ln, "un": un, "id": id}))
            return res[0]

def AddNewMesID(id: int, mid: int):
    with connection:
        cursor.execute("UPDATE Users SET exmess = :mid WHERE user_id = :id", ({"mid": mid, "id": id}))

#TEST PART
def DataFitting(act: str, lvl: int, id: int):
    with connection:
        cursor.execute("UPDATE Users SET action = :act, level = :lvl WHERE user_id = :id", ({"act": act, "lvl": lvl, "id": id}))

def SelSportRegToGame(id: int) -> str:
    with connection:
        cursor.execute("SELECT sport_reg_to_game FROM Users WHERE user_id = ?", (id,))
        return cursor.fetchone()[0]

def SelDateRegToGame(id: int) -> int:
    with connection:
        cursor.execute("SELECT date_reg_to_game FROM Users WHERE user_id = ?", (id,))
        return cursor.fetchone()[0]

def SelTimeRegToGame(id: int) -> int:
    with connection:
        cursor.execute("SELECT time_reg_to_game FROM Users WHERE user_id = ?", (id,))
        return cursor.fetchone()[0]

def SelSeatsRegToGame(id: int) -> int:
    with connection:
        cursor.execute("SELECT seats_reg_to_game FROM Users WHERE user_id = ?", (id,))
        return cursor.fetchone()[0]
    
def DelGameTestUser(id: int):
    with connection:
        cursor.execute("DELETE FROM WatingForGamesUsers WHERE user_id = ?", (id,))