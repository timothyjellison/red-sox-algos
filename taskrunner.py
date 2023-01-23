import random
import sqlite3
from algos import cointoss, mascotferocity
from utils.teams import *
from sqlite3 import Error


def winOrLoss(bool):
    if bool:
        return "Win"
    else:
        return "Loss"


def create_connection(db_file):
    """create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    """create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def record_run(conn, run):
    sql = """
        INSERT INTO runs(opponent, cointoss, mascotferocity)
        VALUES(?,?,?)
    """
    cur = conn.cursor()
    cur.execute(sql, run)
    conn.commit()


if __name__ == "__main__":
    conn = create_connection(r"./sqlite3.db")
    create_table(
        conn,
        """ CREATE TABLE IF NOT EXISTS runs (
            id integer PRIMARY KEY,
            opponent text,
            cointoss bool,
            mascotferocity bool
        ); """,
    )
    opponent = random.choice(allRivalTeams)
    print("The Red Sox will play " + opponent)
    cointoss_result = cointoss.main()
    print("Cointoss predicts: " + winOrLoss(cointoss_result))
    mascotferocity_result = mascotferocity.main(opponent)
    print("Mascot Ferocity predicts: " + winOrLoss(mascotferocity_result))
    record_run(conn, [opponent, cointoss_result, mascotferocity_result])
