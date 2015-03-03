import psycopg2
import time
import os

def dead_loop(cur):
    a = time.time()
    print a
    count = 0
    while True:
        b=time.time()
        if b - a > 10:
            print 'sleep 1s'
            print a,'---',count
            count = 0
            cur.execute("SELECT flag FROM auto_test;")
            row =cur.fetchone()
            flag = row[0]
            if flag:
                break
            time.sleep(0.01)
            a=time.time()
        count += 1

if __name__ == '__main__':
    database = os.getenv("POSTGRES_USER")
    if database is None:
        database = 'postgres'
    user = database
    password = os.getenv("POSTGRES_PASSWORD")
    host = os.getenv("PG_HOST")
    port = os.getenv("PG_PORT")
    if host is None:
        host = '127.0.0.1'
    if port is None:
        port = '5432'

    try:
        conn = psycopg2.connect(database=database,
                                user=user,
                                password=password,
                                host=host,
                                port=port)
        cur = conn.cursor()
        dead_loop(cur)
        print time.time()
        cur.close()
        conn.close()
    except Exception, ex:
        print ex
