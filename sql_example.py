import sqlite3

# DB 연결
conn = sqlite3.connect('C:\sql_output\example.db')
cur = conn.cursor()

print(conn)
print(cur)
# DB에서 코드 정보 가져오기
# cur.execute('SELECT * from Product WHERE id=KE5901')
# rows = cur.fetchall()
# for row in rows:
#     print(row)

# DB 연결종료
conn.close()
