import sys
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

## connect to postgres
conn = psycopg2.connect(database="tcount", user="postgres", password="postgres", host="127.0.0.1", port="5432")
conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
cur = conn.cursor()

if len(sys.argv) ==2:
    word = sys.argv[1]
    cur.execute("SELECT word, count FROM tweetwordcount WHERE word=%s", (word,))
    records = cur.fetchall()
    for rec in records:
       print ("Total number of occurrences of '{0:s}'is : {1:d}".format(rec[0], rec[1]))
elif len(sys.argv) ==1:
    cur.execute("SELECT word, count FROM Tweetwordcount;")
    records = cur.fetchall()
    for rec in records:
        print("Total number of occurrences of '{0:s}'is: {1:d}".format(rec[0], rec[1]))
else:
   
    sys.exit('please input valid parameter')

conn.commit()
conn.close()    

