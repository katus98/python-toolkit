import psycopg2

conn = psycopg2.connect(database="testinfo", user="postgres", password="***", host="192.168.1.4", port="5432")
print("Opened database successfully")

cur = conn.cursor()
cur.execute("SELECT id, object_id, ST_AsText(geom) from geo_db")
rows = cur.fetchall()
for row in rows:
    print("NAME = ")
    print("threshhold0 = ")
    print("threshhold0 = ")
print("Operation done successfully")
conn.close()
