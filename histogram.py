import sys
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

input = sys.argv[1].split(",")
num1,num2 = int(input[0]), int(input[1])

conn = psycopg2.connect(database="tcount", user="postgres", password="password", host="localhost", port="5432")
cur = conn.cursor()

cur.execute("SELECT word, count FROM Tweetwordcount WHERE count>= %s and count <=%s;" %  (num1, num2) )

records = cur.fetchall()
for rec in records:
    print(rec[0], rec[1] )

cur.close()
conn.close()


