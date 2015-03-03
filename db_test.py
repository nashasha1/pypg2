import psycopg2
import time
conn = psycopg2.connect(database="mathilde", user="mathilde", password="123456", host="52.10.189.238", port="1234")
print "connect success"
cur = conn.cursor()
# cur.execute("CREATE TABLE test(id serial PRIMARY KEY, num integer,data varchar);")
#  
# cur.execute("INSERT INTO test(num, data)VALUES(%s, %s)", (1, 'aaa'))
# cur.execute("INSERT INTO test(num, data)VALUES(%s, %s)", (2, 'bbb'))
# cur.execute("INSERT INTO test(num, data)VALUES(%s, %s)", (3, 'ccc'))
cur.execute("SELECT * FROM test;")
rows = cur.fetchall()        # all rows in table
print(rows)
for i in rows:
    print(i)
conn.commit()
cur.close()
conn.close()

