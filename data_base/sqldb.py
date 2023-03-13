import sqlite3 as sq
from create_bot import bot


def sql_start():
    global base, cur
    base = sq.connect("mainbase.db")
    cur = base.cursor()
    if base:
        print('DATA BASE WAS CONNECTED SUCCSESSFUL')
    base.execute("CREATE TABLE IF NOT EXISTS {}(name TEXT, age TEXT, contact TEXT PRIMARY KEY, information TEXT)".format("menu"))
    base.commit()

async def insert_data_command(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO menu VALUES (?, ?, ?, ?)', tuple(data.values()))
        base.commit()

async def sql_read(ID):
    for ret in cur.execute('SELECT * FROM menu').fetchall():
        await bot.send_message(ID, f'Имя: {ret[0]}\nВозраст: {ret[1]}\nКонтакт: {ret[2]}\nИнформация: {ret[-1]}')

async def sql_read2():
    return cur.execute('SELECT * FROM menu').fetchall()

async def sql_delete_command(data):
    cur.execute('DELETE FROM menu WHERE name == ?', (data,))
    base.commit()