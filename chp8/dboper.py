import sqlite3
import uuid


def sqlite3test():
    conn = sqlite3.connect("/Users/frank/Documents/Ex/sqlite.db")
    cursor = conn.cursor()

    cursor.execute('''create table zoo 
    (critter varchar(20) primary key ,
    count  int ,
    damages float ) ''')

    print(cursor)


def sqliteInsert():
    conn = sqlite3.connect("/Users/frank/Documents/Ex/sqlite.db")
    cur = conn.cursor()

    print('写入数据')
    seteuid = str(uuid.uuid1())
    sql = "insert into zoo values ('" + seteuid + "' , 3, 34.5)"
    print(sql)
    count = cur.execute(sql)
    print(count.rowcount)
    conn.commit()

    cur.execute('select * from zoo')
    rows = cur.fetchall()
    print(len(rows))

    row = cur.execute('select count(1) from zoo').fetchall()
    print(row)


if __name__ == "__main__":
    print('Action>>>>>>>')
#    ##sqlite3test()
    sqliteInsert()
