import sqlite3
import pars


# Создание БД и Таблицы
def CreateTable():
    """
    Создание БД, в случае её отсутствия и создание таблицы
    :return:
    """
    con = sqlite3.connect("Test.db")
    cur = con.cursor()
    cur.execute('CREATE TABLE ARTICLE (id_article integer primary key autoincrement, title varchar(50), author varchar('
                '50), journal varchar(50), year varchar(50), '
                'pages varchar(50), volume varchar(50))')
    con.commit()
    con.close()
    return


def insertTable(dict_attr):
    """
    Вычленяем из словаря атрибуты в список, и вставляем его в нашу таблицу
    :param dict_attr: словарь
    :return:
    """
    con = sqlite3.connect("Test.db")
    cur = con.cursor()
    DataList = [dict_attr['Title'], dict_attr['Author'], dict_attr['Journal'], dict_attr['Year'], dict_attr['Pages'],
                dict_attr['Volume']]
    cur.execute('INSERT INTO ARTICLE(title, author, journal, year, pages, volume) values(?, ?, ?, ?, ?, ?)', DataList)
    con.commit()
    return


def selectAuthor(author):
    """
    Ищем автора в базе данных
    :param author: ФИО автора(Обязательно нужно начинать с фамилии и прописывать ее полностью)
    :return:
    """
    con = sqlite3.connect("Test.db")
    cur = con.cursor()
    
    AuthList = [(author)]
    cur.executemany("SELECT * FROM ARTICLE WHERE AUTHOR LIKE '?%'", AuthList)
    print(cur.fetchall())
    con.close()
    return
